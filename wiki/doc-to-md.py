import os
import re
import yaml # 用于解析 mkdocs.yml，需要 pip install PyYAML
from pathlib import Path
import uuid # 用于生成唯一锚点

# --- 配置 (这些现在是默认值，用户可以在交互中覆盖或脚本内部修改) ---
DEFAULT_DOCS_DIR = "docs"
DEFAULT_OUTPUT_FILENAME = "All_In_One_Wiki.md"
DEFAULT_LANGUAGE = "zh" # 默认提取中文
DEFAULT_AUTO_EXCLUDE_TITLE_KEYWORDS = ["更新日志", "release notes", "changelog", "版本历史", "历史版本", "faq", "常见问题"]
MARKDOWN_CLEANUP_PATTERNS = [
    (r'!\[.*?\]\(.*?\)\s*', '', 0),
    (r'\{\{.*?\}\}', '', 0),
    (r'Last updated on .*?\s*', '', 0),
    (r'Edit this page on GitHub', '', re.IGNORECASE),
    (r'Improve this page', '', re.IGNORECASE),
    (r'Found an issue\? Let us know!', '', re.IGNORECASE),
    (r'Contribute to this page', '', re.IGNORECASE),
    (r'View page source', '', re.IGNORECASE),
    (r'Permanent link', '', re.IGNORECASE),
    (r'\[¶\]\(#.*?\s*".*?"\)', '', 0), 
    (r'^\s*-\s*\[.*?\]\(#.*?\)\s*$', '', re.MULTILINE), 
    (r'(?i)^\s*(?:##?#?)\s*(?:Table of Contents|On this page)\s*$', '', re.MULTILINE),
    (r'\n{3,}', '\n\n', 0), 
    (r'^\s*---\s*$', '', re.MULTILINE), 
]

def sanitize_anchor(title: str) -> str:
    """为 TOC 生成干净的锚点链接。"""
    anchor = title.lower()
    anchor = re.sub(r'\s+', '-', anchor)
    anchor = re.sub(r'[^\w\s\u4e00-\u9fff-]+', '', anchor, flags=re.UNICODE)
    anchor = re.sub(r'-+', '-', anchor)
    anchor = anchor.strip('-')
    if not anchor:
        return f"section-{uuid.uuid4().hex[:8]}"
    return anchor

def extract_title_from_markdown(content: str, fallback_title: str) -> str:
    """从 Markdown 内容中提取第一个 H1 标题。"""
    match = re.search(r'^\s*#\s+(.+)', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback_title

def remove_yaml_front_matter(content: str) -> str:
    """移除 Markdown 文件头部的 YAML Front Matter。"""
    match = re.match(r'---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL | re.MULTILINE)
    if match:
        return match.group(2).strip() 
    return content.strip()

def process_markdown_file(file_path: Path, is_excluded_content_page: bool, nav_title: str) -> tuple[str, str]:
    """
    读取并处理单个 Markdown 文件。
    现在接收 nav_title 以便在精简提示中使用。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except FileNotFoundError:
        title_from_path = nav_title if nav_title and nav_title != str(file_path) else file_path.stem.replace('.en', '').replace('.ru', '').replace('.zh', '').replace('_', ' ').title()
        print(f"警告：文件未找到: {file_path}")
        return title_from_path, f"(文件 {file_path.name} 未找到)\n"
    except Exception as e:
        title_from_path = nav_title if nav_title and nav_title != str(file_path) else file_path.stem.replace('.en', '').replace('.ru', '').replace('.zh', '').replace('_', ' ').title()
        print(f"错误：读取文件 {file_path} 失败: {e}")
        return title_from_path, f"(读取文件 {file_path.name} 失败: {e})\n"

    content_no_front_matter = remove_yaml_front_matter(raw_content)
    page_title_to_use = nav_title
    if not page_title_to_use or page_title_to_use == str(file_path): 
        base_title_from_filename = file_path.stem.replace('.en', '').replace('.ru', '').replace('.zh', '').replace('_', ' ').title()
        page_title_to_use = extract_title_from_markdown(content_no_front_matter, base_title_from_filename)

    if is_excluded_content_page:
        return page_title_to_use, f"\n\n(此部分内容 '{page_title_to_use}' 已被用户选择精简)\n\n"

    processed_content = content_no_front_matter
    for pattern, replacement, flags in MARKDOWN_CLEANUP_PATTERNS:
        try:
            processed_content = re.sub(pattern, replacement, processed_content, flags=flags | re.UNICODE)
        except Exception as e_re:
            print(f"警告：应用Markdown清理模式 '{pattern}' 到文件 '{file_path.name}' 时出错: {e_re}")
    
    processed_content = processed_content.strip()
    return page_title_to_use, processed_content


def flatten_nav_structure(nav_list: list, current_path_parts: list, docs_dir: Path, target_lang: str, default_lang_from_config: str, lang_suffix_structure: bool) -> list:
    """
    递归地将 mkdocs.yml 中的 nav 结构扁平化为一个有序的文件列表。
    返回一个列表，每个元素是字典 {'nav_title': str, 'file_path': Path | None, 'is_excluded_content': bool, 'id_for_selection': int}
    """
    flattened_files = []
    if not hasattr(flatten_nav_structure, "page_counter"):
        flatten_nav_structure.page_counter = 0

    for item in nav_list:
        if isinstance(item, str): 
            source_rel_path_str = item
            title_from_filename = Path(source_rel_path_str).stem.replace('.en', '').replace('.ru', '').replace('.zh','').replace('_', ' ').title()
            
            actual_file_path, used_nav_title = resolve_file_path_and_title(
                Path(source_rel_path_str), title_from_filename, docs_dir, target_lang, default_lang_from_config, lang_suffix_structure
            )
            
            flatten_nav_structure.page_counter += 1
            is_auto_excluded = any(keyword.lower() in used_nav_title.lower() for keyword in DEFAULT_AUTO_EXCLUDE_TITLE_KEYWORDS)
            flattened_files.append({
                'nav_title': used_nav_title, 
                'file_path': actual_file_path, 
                'is_excluded_content': is_auto_excluded, 
                'id_for_selection': flatten_nav_structure.page_counter
            })

        elif isinstance(item, dict):
            for nav_title_key, value in item.items(): 
                if isinstance(value, str): 
                    source_rel_path_str = value
                    actual_file_path, used_nav_title = resolve_file_path_and_title(
                        Path(source_rel_path_str), nav_title_key, docs_dir, target_lang, default_lang_from_config, lang_suffix_structure
                    )
                    flatten_nav_structure.page_counter += 1
                    is_auto_excluded = any(keyword.lower() in used_nav_title.lower() for keyword in DEFAULT_AUTO_EXCLUDE_TITLE_KEYWORDS)
                    flattened_files.append({
                        'nav_title': used_nav_title, 
                        'file_path': actual_file_path, 
                        'is_excluded_content': is_auto_excluded,
                        'id_for_selection': flatten_nav_structure.page_counter
                        })
                elif isinstance(value, list): 
                    flattened_files.extend(flatten_nav_structure(value, current_path_parts, docs_dir, target_lang, default_lang_from_config, lang_suffix_structure))
    return flattened_files

def resolve_file_path_and_title(source_rel_path_from_nav: Path, nav_title: str, docs_dir: Path, target_lang: str, default_lang_from_config: str, lang_suffix_structure: bool) -> tuple[Path | None, str]:
    """
    根据目标语言解析实际的文件路径。
    返回 (绝对文件路径对象 | None, 使用的标题)
    """
    resolved_path = None
    title_to_use = nav_title 

    if source_rel_path_from_nav.is_absolute():
        try:
            source_rel_path_from_nav = source_rel_path_from_nav.relative_to(docs_dir)
        except ValueError: 
             print(f"错误：mkdocs.yml 中的绝对路径 '{source_rel_path_from_nav}' 不在 docs 目录 '{docs_dir}' 下。")
             return None, nav_title

    potential_paths_to_try = []
    stem = source_rel_path_from_nav.stem
    suffix = source_rel_path_from_nav.suffix
    parent_dir = source_rel_path_from_nav.parent

    base_stem = stem
    known_lang_suffixes = [f'.{lang_code}' for lang_code in ['en', 'ru', 'zh', target_lang, default_lang_from_config] if lang_code]
    for lang_sfx in known_lang_suffixes:
        if base_stem.endswith(lang_sfx):
            base_stem = base_stem[:-len(lang_sfx)]
            break
    
    if target_lang and lang_suffix_structure:
        potential_paths_to_try.append(docs_dir / parent_dir / f"{base_stem}.{target_lang}{suffix}")
    potential_paths_to_try.append(docs_dir / parent_dir / f"{base_stem}{suffix}")
    if default_lang_from_config and target_lang != default_lang_from_config and lang_suffix_structure:
        potential_paths_to_try.append(docs_dir / parent_dir / f"{base_stem}.{default_lang_from_config}{suffix}")
    potential_paths_to_try.append(docs_dir / source_rel_path_from_nav)

    checked_paths = set()
    for p_path_abs in potential_paths_to_try:
        if p_path_abs not in checked_paths:
            if p_path_abs.exists() and p_path_abs.is_file():
                resolved_path = p_path_abs
                break
            checked_paths.add(p_path_abs)
    
    if not resolved_path:
        return None, nav_title 

    filename_derived_title_for_check = source_rel_path_from_nav.stem.replace('.en', '').replace('.ru', '').replace('.zh','').replace('_', ' ').title()
    # 如果nav_title为空，或者看起来像文件名，则尝试从文件内容更新
    if not nav_title.strip() or nav_title.lower() == filename_derived_title_for_check.lower() or nav_title == str(source_rel_path_from_nav):
        try:
            with open(resolved_path, 'r', encoding='utf-8') as f_title_check:
                temp_content_for_title = remove_yaml_front_matter(f_title_check.read())
                title_from_content = extract_title_from_markdown(temp_content_for_title, nav_title if nav_title.strip() else filename_derived_title_for_check)
                if title_from_content and title_from_content.strip(): 
                    title_to_use = title_from_content
        except Exception: 
            pass 
            
    return resolved_path, title_to_use


# --- 自定义 YAML 加载器，用于处理特殊的 Python 标签 ---
class CustomLoader(yaml.FullLoader): # 继承自 FullLoader 或 SafeLoader 均可，取决于基础需求
    pass

def python_name_constructor(loader, suffix, node):
    """
    处理 !!python/name: 标签。
    我们不实际构造 Python 对象，而是返回标签的后缀（即模块.对象名字符串）
    或者一个更通用的占位符，因为我们通常不关心这些值。
    """
    # print(f"信息：遇到并忽略了 YAML 标签: {node.tag} (值为: {suffix})")
    return f"YAML_PYTHON_TAG_REFERENCE({suffix})" # 返回一个字符串表示遇到了这个标签

CustomLoader.add_multi_constructor('tag:yaml.org,2002:python/name:', python_name_constructor)
# --- 结束自定义 YAML 加载器 ---


def main():
    print("--- 本地 MkDocs 项目 Markdown 合并工具 ---")

    repo_root_str = ""
    while not repo_root_str:
        repo_root_str = input("请输入包含 mkdocs.yml 的仓库根目录路径: ").strip()
        repo_root = Path(repo_root_str)
        if not repo_root.is_dir():
            print(f"错误：路径 '{repo_root_str}' 不是一个有效的目录。请重新输入。")
            repo_root_str = ""
        elif not (repo_root / "mkdocs.yml").is_file():
            print(f"错误：在 '{repo_root_str}' 下未找到 mkdocs.yml 文件。请确保路径正确。")
            repo_root_str = ""
    
    target_lang = input(f"请输入要提取的语言代码 (例如 zh, en, ru, 默认: {DEFAULT_LANGUAGE}): ").strip().lower() or DEFAULT_LANGUAGE
    output_filename = input(f"请输入输出的 All-In-One Markdown 文件名 (默认: {DEFAULT_OUTPUT_FILENAME}): ").strip() or DEFAULT_OUTPUT_FILENAME
    docs_subdir_name = input(f"请输入文档源文件子目录名 (相对于仓库根目录，默认: {DEFAULT_DOCS_DIR}): ").strip() or DEFAULT_DOCS_DIR
    
    docs_abs_dir = repo_root / docs_subdir_name
    if not docs_abs_dir.is_dir():
        print(f"错误：文档子目录 '{docs_subdir_name}' 在 '{repo_root}' 下未找到。")
        return

    print(f"\n配置确认:\n  仓库根目录: {repo_root.resolve()}\n  目标语言: {target_lang}\n  输出文件名: {output_filename}\n  文档子目录: {docs_subdir_name}\n")

    try:
        with open(repo_root / "mkdocs.yml", 'r', encoding='utf-8') as f:
            # 使用自定义加载器 CustomLoader
            mkdocs_config = yaml.load(f, Loader=CustomLoader)
    except yaml.YAMLError as e: 
        print(f"错误：解析 mkdocs.yml 文件失败: {e}")
        if hasattr(e, 'problem_mark'):
            mark = e.problem_mark
            print(f"  错误发生在行 {mark.line+1}, 列 {mark.column+1}")
        print("  请检查 mkdocs.yml 文件格式是否正确。")
        return
    except Exception as e:
        print(f"错误：读取或解析 mkdocs.yml 时发生未知错误: {e}")
        return

    default_lang_from_config = "en" 
    lang_suffix_structure = False 
    nav_source_list = None

    plugins_config = mkdocs_config.get('plugins', [])
    if isinstance(plugins_config, list): 
        i18n_plugin_settings = None
        for plugin_item in plugins_config:
            if isinstance(plugin_item, dict) and 'i18n' in plugin_item:
                i18n_plugin_settings = plugin_item['i18n']
                break
            elif isinstance(plugin_item, str) and plugin_item == 'i18n':
                i18n_plugin_settings = mkdocs_config.get('extra', {}).get('i18n', {}) 
                if not i18n_plugin_settings and 'languages' in mkdocs_config:
                     i18n_plugin_settings = {'languages': mkdocs_config.get('languages')}
                break
        
        if i18n_plugin_settings and isinstance(i18n_plugin_settings, dict): # 确保是字典
            print("信息：检测到 i18n 插件配置。")
            languages_in_config = i18n_plugin_settings.get('languages', [])
            if isinstance(languages_in_config, list):
                for lang_conf in languages_in_config: 
                    if isinstance(lang_conf, dict):
                        if lang_conf.get('default', False):
                            default_lang_from_config = lang_conf.get('locale', default_lang_from_config)
                            break
                    elif isinstance(lang_conf, str) and lang_conf == default_lang_from_config: 
                        pass 
            
            if i18n_plugin_settings.get('docs_structure') == 'suffix':
                lang_suffix_structure = True
            
            nav_source_list = mkdocs_config.get('nav') 
            nav_translations = i18n_plugin_settings.get('nav_translations')
            if nav_translations and isinstance(nav_translations, dict) and target_lang in nav_translations:
                nav_source_list = nav_translations[target_lang]
                print(f"信息：已加载语言 '{target_lang}' 的特定导航。")
            elif target_lang != default_lang_from_config:
                 print(f"警告：未找到语言 '{target_lang}' 的特定导航翻译，将使用默认导航。")
        else: 
            print("信息：未找到详细的 i18n 插件配置，将使用主 'nav' 结构，并根据文件名约定尝试语言匹配。")
            nav_source_list = mkdocs_config.get('nav')
            if target_lang != "en": lang_suffix_structure = True 
            default_lang_from_config = "en" 
    else: 
        nav_source_list = mkdocs_config.get('nav')
        print("警告：MkDocs 配置中未找到 'plugins' 列表或其格式未知。将使用主 'nav' 结构。")
        if target_lang != "en": lang_suffix_structure = True
        default_lang_from_config = "en"

    if not nav_source_list or not isinstance(nav_source_list, list):
        print("错误：mkdocs.yml 中未找到有效的 'nav' 列表结构，无法确定文件顺序。")
        return

    flatten_nav_structure.page_counter = 0 
    print(f"信息：将使用语言 '{target_lang}' (推断的默认语言是 '{default_lang_from_config}', 后缀结构: {lang_suffix_structure})")
    ordered_files_meta = flatten_nav_structure(nav_source_list, [], docs_abs_dir, target_lang, default_lang_from_config, lang_suffix_structure)

    if not ordered_files_meta:
        print("错误：未能从 mkdocs.yml 的导航结构中提取任何有效文件进行处理。")
        return

    print("\n--- 页面内容精简选择 ---")
    print("以下是根据导航结构找到的页面：")
    for item_meta in ordered_files_meta:
        pre_excluded_marker = "[自动精简]" if item_meta['is_excluded_content'] else ""
        print(f"  {item_meta['id_for_selection']}. {item_meta['nav_title']} {pre_excluded_marker}")
    
    excluded_ids_input = input("\n您想选择哪些页面的详细内容进行精简（例如更新日志、FAQ）？\n请输入页面编号，用逗号或空格分隔 (例如: 1, 3, 5-7)，或直接按 Enter 跳过: ").strip()
    
    user_selected_exclusion_ids = set()
    if excluded_ids_input:
        raw_ids = re.split(r'[\s,]+', excluded_ids_input)
        for r_id in raw_ids:
            if r_id.isdigit():
                user_selected_exclusion_ids.add(int(r_id))
            elif '-' in r_id: 
                try:
                    start_id, end_id = map(int, r_id.split('-',1))
                    if start_id <= end_id:
                        user_selected_exclusion_ids.update(range(start_id, end_id + 1))
                    else:
                        print(f"警告：无效的范围 '{r_id}' (起始大于结束)，已忽略。")
                except ValueError:
                     print(f"警告：无效的范围输入 '{r_id}'，已忽略。")

    for item_meta in ordered_files_meta:
        if item_meta['id_for_selection'] in user_selected_exclusion_ids:
            item_meta['is_excluded_content'] = True
            print(f"信息：用户选择精简页面 '{item_meta['nav_title']}' 的内容。")

    all_content_parts = []
    site_name = mkdocs_config.get('site_name', 'Wiki')
    toc_entries = [f"# {site_name} 文档目录 ({target_lang.upper()})\n"]

    print(f"\n将处理 {len(ordered_files_meta)} 个文档页面...")
    for item_meta in ordered_files_meta:
        file_path = item_meta['file_path']
        nav_title = item_meta['nav_title'] 
        is_excluded_content_page = item_meta['is_excluded_content']
        
        if not isinstance(nav_title, str):
            nav_title = str(nav_title) if nav_title is not None else (file_path.stem if file_path else "未知页面")

        if not file_path or not file_path.exists():
            print(f"警告：文件路径 '{file_path}' 无效或文件不存在，为标题 '{nav_title}' 生成占位符。")
            toc_entries.append(f"- [{nav_title} (文件未找到)](#{sanitize_anchor(nav_title)})")
            all_content_parts.append(f"# {nav_title}\n\n(文件未找到或无法访问: {file_path})\n\n")
            continue

        actual_page_title_from_file, md_content = process_markdown_file(file_path, is_excluded_content_page, nav_title)
        
        title_for_toc_and_heading = nav_title # 默认使用nav_title
        # 如果nav_title看起来像文件名，或者为空，则尝试使用从文件提取的标题
        if not nav_title.strip() or \
           nav_title.lower() == file_path.stem.lower().replace(f'.{target_lang}','').replace(f'.{default_lang_from_config}','') or \
           nav_title.lower() == file_path.name.lower():
            if actual_page_title_from_file and actual_page_title_from_file.strip():
                 title_for_toc_and_heading = actual_page_title_from_file


        toc_entries.append(f"- [{title_for_toc_and_heading}](#{sanitize_anchor(title_for_toc_and_heading)})")
        all_content_parts.append(f"# {title_for_toc_and_heading}\n\n{md_content}\n\n")

    output_file_path = repo_root / output_filename 
    final_markdown = "".join(toc_entries) + "\n---\n\n" + "---\n\n".join(all_content_parts)
    
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(final_markdown)
        print(f"\n成功合并所有文档到: {output_file_path.resolve()}")
    except Exception as e:
        print(f"错误：写入合并后的文件失败: {e}")

if __name__ == "__main__":
    main()
