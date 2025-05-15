import os
import time
import re
import shutil
import markdownify
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse
import uuid
from bs4 import BeautifulSoup, NavigableString # NavigableString 用于判断文本节点

# --- 默认配置参数 (用户可以在脚本内部修改这些默认值) ---
# -----------------------------------------------------------------------------
DEFAULT_TARGET_WIKI_BASE_URL = ""
DEFAULT_TARGET_PAGE_TITLE_SUFFIX = ""
DEFAULT_MAIN_CONTENT_CSS_SELECTOR = "article, main, .main-content, #main, #content, .content, div.article-content, div.content-body, .prose"
DEFAULT_HTML_CLEANUP_SELECTORS = [
    "nav", "footer", "aside", ".sidebar", ".toc", "div#toc", "nav#TableOfContents",
    ".page-meta", "div.td-toc", "div.community-links", "script", "style",
    "header", ".header", ".site-header", ".top-nav", ".bottom-nav",
    ".breadcrumb", ".breadcrumbs", ".related-posts", ".comments", "#comments",
    ".cookie-banner", ".ads", "[class*='ad-']", "[id*='ad-']",
    ".edit-this-page", "a[href*='edit']", "button.copy", "div.edit-link",
    "div.prev-next-links", "div.last-updated" # 常见文档页脚导航和更新时间
]
DEFAULT_PAGE_TITLE_EXCLUSION_KEYWORDS = ["更新日志", "release notes", "changelog", "版本历史", "历史版本"]
DEFAULT_URL_PATH_EXCLUSIONS_FOR_CRAWL = ["/dev/", "/archive/", "/files/", "/static/", "/assets/", "/images/"]
DEFAULT_MARKDOWN_CLEANUP_PATTERNS = [
    (r'!\[.*?\]\(.*?\)\s*', '', 0),
    (r'`CTRL K`\s*\n`CTRL K`\s*\n', '', re.IGNORECASE),
    (r'^`CTRL K`\s*$', '', re.MULTILINE | re.IGNORECASE),
    (r'中文\s*\n\s*System\s*\n', '', 0),
    (r'^中文\s*$', '', re.MULTILINE),
    (r'^System\s*$', '', re.MULTILINE),
    (r'^#+\s*$', '', re.MULTILINE), 
    (r'\n{3,}', '\n\n', 0), 
    (r'Last updated on .*?\s*', '', 0),
    (r'Edit this page on GitHub', '', 0),
    (r'Improve this page', '', 0),
    (r'Found an issue\? Let us know!', '', 0),
    (r'Table of Contents', '', re.IGNORECASE), 
    (r'On this page', '', re.IGNORECASE),     
    (r'\u00a9 \d{4}.*?Ltd\.', '', 0),         
    (r'\u00a9 \d{4}.*?\.', '', 0),
    (r'Contribute to this page', '', re.IGNORECASE), 
    (r'View page source', '', re.IGNORECASE),
    (r'Permanent link', '', re.IGNORECASE), 
    (r'\[¶\]\(#.*?\s*".*?"\)', '', 0), 
]
DEFAULT_OUTPUT_DIR_BASE = "wiki_output_interactive"
DEFAULT_MAX_PAGES_TO_CRAWL = 50
DEFAULT_POLITENESS_DELAY = 0.25
DEFAULT_HEADLESS_BROWSER = True
# -----------------------------------------------------------------------------

# --- 全局变量 ---
TARGET_WIKI_START_URL = ""
TARGET_WIKI_BASE_URL = ""
TARGET_PAGE_TITLE_SUFFIX = ""
MAIN_CONTENT_CSS_SELECTOR = ""
HTML_CLEANUP_SELECTORS = []
PAGE_TITLE_EXCLUSION_KEYWORDS = []
URL_PATH_EXCLUSIONS_FOR_CRAWL = [] 
MARKDOWN_CLEANUP_PATTERNS = []
OUTPUT_DIR_BASE = ""
MAX_PAGES_TO_CRAWL = 0
POLITENESS_DELAY = 0.0
HEADLESS_BROWSER = True
_TARGET_WIKI_BASE_URL_EFFECTIVE = ""
temp_individual_files_dir = "" 


def setup_global_config_from_input():
    """通过用户输入或默认值来设置全局配置变量。"""
    global TARGET_WIKI_START_URL, TARGET_WIKI_BASE_URL, TARGET_PAGE_TITLE_SUFFIX, \
           MAIN_CONTENT_CSS_SELECTOR, HTML_CLEANUP_SELECTORS, PAGE_TITLE_EXCLUSION_KEYWORDS, \
           URL_PATH_EXCLUSIONS_FOR_CRAWL, MARKDOWN_CLEANUP_PATTERNS, OUTPUT_DIR_BASE, \
           MAX_PAGES_TO_CRAWL, POLITENESS_DELAY, HEADLESS_BROWSER, temp_individual_files_dir

    print("--- Wiki 爬虫配置 ---")
    while not TARGET_WIKI_START_URL:
        TARGET_WIKI_START_URL = input("请输入目标 Wiki 的起始 URL (例如: https://wiki.example.com/docs/): ").strip()
        if not (TARGET_WIKI_START_URL.startswith("http://") or TARGET_WIKI_START_URL.startswith("https://")):
            print("URL 格式无效，请输入以 http:// 或 https:// 开头的完整 URL。")
            TARGET_WIKI_START_URL = ""

    TARGET_WIKI_BASE_URL = input(f"请输入目标 Wiki 的基础 URL (用于判断内部链接，默认会自动从起始URL推断): ").strip() or DEFAULT_TARGET_WIKI_BASE_URL
    TARGET_PAGE_TITLE_SUFFIX = input(f"请输入页面标题中需要移除的固定后缀 (可选，默认为空): ").strip() or DEFAULT_TARGET_PAGE_TITLE_SUFFIX
    
    print(f"\n提示: 主要内容 CSS 选择器是适配不同 Wiki 的关键。默认尝试: '{DEFAULT_MAIN_CONTENT_CSS_SELECTOR}'")
    MAIN_CONTENT_CSS_SELECTOR = input(f"请输入核心内容区的 CSS 选择器 (可选，默认为尝试通用选择器): ").strip() or DEFAULT_MAIN_CONTENT_CSS_SELECTOR

    print(f"\n以下配置将使用默认值，您可以在脚本顶部修改这些默认列表以进行高级定制：")
    HTML_CLEANUP_SELECTORS = DEFAULT_HTML_CLEANUP_SELECTORS
    print(f" - HTML 清理选择器数量: {len(HTML_CLEANUP_SELECTORS)}")
    PAGE_TITLE_EXCLUSION_KEYWORDS = DEFAULT_PAGE_TITLE_EXCLUSION_KEYWORDS
    print(f" - 页面标题排除关键词: {PAGE_TITLE_EXCLUSION_KEYWORDS}")
    
    URL_PATH_EXCLUSIONS_FOR_CRAWL = list(DEFAULT_URL_PATH_EXCLUSIONS_FOR_CRAWL) # 从默认值开始
    print(f" - 当前默认的URL路径排除规则为: {URL_PATH_EXCLUSIONS_FOR_CRAWL}")
    
    while True:
        add_exclusions_prompt = input("   您想额外添加要排除的URL路径吗 (例如 /en/, /ru/)? (yes/no, 默认 no): ").strip().lower()
        if add_exclusions_prompt == 'yes':
            while True:
                additional_path = input("     请输入一个要额外排除的URL路径片段 (例如: /en/，路径需以 / 开头)，或直接按 Enter 结束添加: ").strip()
                if not additional_path: # 用户直接按回车，结束添加
                    break
                if additional_path.startswith('/'):
                    if additional_path not in URL_PATH_EXCLUSIONS_FOR_CRAWL:
                        URL_PATH_EXCLUSIONS_FOR_CRAWL.append(additional_path)
                        print(f"       已添加: '{additional_path}'. 当前排除列表: {URL_PATH_EXCLUSIONS_FOR_CRAWL}")
                    else:
                        print(f"       路径 '{additional_path}' 已在排除列表中。")
                else:
                    print("       无效路径，必须以 / 开头。请重新输入。")
            break # 结束外层 "yes/no" 循环
        elif add_exclusions_prompt == 'no' or not add_exclusions_prompt: # 用户输入 no 或直接回车
            break
        else:
            print("   无效输入，请输入 'yes' 或 'no'。")

    print(f"   最终URL路径排除规则为: {URL_PATH_EXCLUSIONS_FOR_CRAWL}")
    confirm_exclusions = input("   确认以上排除列表吗? (yes/no, 默认 yes): ").strip().lower()
    if confirm_exclusions == 'no':
        print("   用户未确认排除列表。请注意，脚本将使用当前列表。如需修改，请重新运行脚本进行配置。")
        # 为了简单，这里不实现返回重新输入逻辑，用户需重启脚本


    MARKDOWN_CLEANUP_PATTERNS = DEFAULT_MARKDOWN_CLEANUP_PATTERNS
    print(f" - Markdown 清理模式数量: {len(MARKDOWN_CLEANUP_PATTERNS)}")
    OUTPUT_DIR_BASE = input(f"请输入输出文件夹的基础名称 (默认: {DEFAULT_OUTPUT_DIR_BASE}): ").strip() or DEFAULT_OUTPUT_DIR_BASE
    
    try:
        MAX_PAGES_TO_CRAWL = int(input(f"请输入最大爬取页面数 (默认: {DEFAULT_MAX_PAGES_TO_CRAWL}): ").strip() or str(DEFAULT_MAX_PAGES_TO_CRAWL))
    except ValueError: MAX_PAGES_TO_CRAWL = DEFAULT_MAX_PAGES_TO_CRAWL
    try:
        POLITENESS_DELAY = float(input(f"请输入每个请求间的延迟 (秒, 默认: {DEFAULT_POLITENESS_DELAY}): ").strip() or str(DEFAULT_POLITENESS_DELAY))
    except ValueError: POLITENESS_DELAY = DEFAULT_POLITENESS_DELAY
    
    headless_input = input(f"是否以无头模式运行浏览器 (True/False, 默认: {DEFAULT_HEADLESS_BROWSER}): ").strip().lower()
    HEADLESS_BROWSER = False if headless_input == 'false' else DEFAULT_HEADLESS_BROWSER
    
    print("--- 配置完成 ---\n")
    os.makedirs(OUTPUT_DIR_BASE, exist_ok=True)
    temp_individual_files_dir = os.path.join(OUTPUT_DIR_BASE, "individual_pages_temp")
    if os.path.exists(temp_individual_files_dir): shutil.rmtree(temp_individual_files_dir)
    os.makedirs(temp_individual_files_dir, exist_ok=True)


def sanitize_filename(name: str) -> str:
    if not name: return f"untitled_{int(time.time())}"
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = name.replace(" ", "_")
    name = name[:150]
    if not name.strip() or name.strip() == ".": name = f"untitled_{int(time.time())}"
    return name

def extract_code_from_element(code_element):
    """
    从 BeautifulSoup 元素 (通常是 <code> 或 <pre>) 中提取纯文本代码,
    尝试保留换行和主要缩进。
    """
    text_parts = []
    # 遍历所有子孙节点以正确处理换行和文本片段
    for elem in code_element.descendants:
        if isinstance(elem, NavigableString):
            text_parts.append(str(elem))
        elif elem.name == 'br': # HTML <br> 标签
            text_parts.append('\n')
        elif elem.name in ['div', 'p'] and elem.find_previous_sibling() and elem.find_previous_sibling().name in ['div', 'p']:
            # 对于某些代码块结构，div或p可能代表新行，但要避免在行内元素间加过多换行
            # 这是一个启发式规则，可能需要调整
             if not text_parts or not text_parts[-1].endswith('\n'):
                 text_parts.append('\n')


    plain_code_text = "".join(text_parts)
    
    # 清理：移除行尾空格，尝试移除完全由空格组成的行，但保留行首的真实缩进
    cleaned_lines = []
    for line in plain_code_text.splitlines():
        stripped_line = line.rstrip()
        if stripped_line or line.strip() == "": # 保留空行（只包含换行符的行）或非空白行
            cleaned_lines.append(stripped_line) 
            
    final_code = "\n".join(cleaned_lines)
    return final_code.strip('\n') # 移除开头和结尾可能的多余换行


def clean_html_before_markdownify(html_content: str, page_title: str) -> tuple[str, dict]:
    """
    在将 HTML 转换为 Markdown 之前，使用 BeautifulSoup 清理 HTML 内容。
    特殊处理代码块，将其替换为占位符，并存储代码内容。
    """
    if not html_content: return "", {}
    soup = BeautifulSoup(html_content, 'html.parser')
    code_blocks_data = {} # 用于存储提取的代码块: {placeholder: {"lang": lang, "code": code_text}}
    code_block_counter = 0

    # 1. 特殊处理代码块 (例如 MetaCube X Wiki 的 div.language-xxx > pre > code)
    # 也处理通用的 <pre><code> 或 <pre> 结构
    # 优先处理更具体的结构，然后处理通用的 <pre>
    code_selectors_priority = [
        'div[class*="language-"] pre', # 针对 Shiki/Prism 等高亮库的常见结构
        'pre > code',                  # 标准的 pre 包裹 code
        'pre'                          # 单独的 pre 标签
    ]

    processed_code_elements = set() # 避免重复处理嵌套的 pre/code

    for selector in code_selectors_priority:
        for element in soup.select(selector):
            if element in processed_code_elements or element.find_parent(lambda tag: tag in processed_code_elements):
                continue # 如果元素或其父元素已被处理，则跳过

            lang = ""
            # 尝试从 class 获取语言
            # 对于 'div[class*="language-"] pre'，语言在父 div 上
            parent_div = element.find_parent('div', class_=lambda x: x and x.startswith('language-'))
            if parent_div:
                classes = parent_div.get('class', [])
                for cls in classes:
                    if cls.startswith('language-'):
                        lang = cls.split('language-', 1)[1].split(' ')[0] # 取 language- 后面的部分，并处理可能的多class情况
                        break
            
            # 如果是从 'pre > code' 或 'pre' 选中的，尝试从 code 或 pre 的 class 获取
            if not lang and element.name == 'code' and element.has_attr('class'):
                classes = element.get('class', [])
                for cls in classes:
                    if cls.startswith('language-'):
                        lang = cls.split('language-', 1)[1]
                        break
            if not lang and element.name == 'pre' and element.has_attr('class'): # 如果是直接处理 <pre>
                classes = element.get('class', [])
                for cls in classes:
                    if cls.startswith('language-'):
                        lang = cls.split('language-', 1)[1]
                        break
            
            # MetaCube X 特有的语言标识 <span class="lang">yaml</span>
            lang_span = element.find_previous_sibling('span', class_='lang') if element.name == 'pre' else None
            if not lang and lang_span and lang_span.string:
                lang = lang_span.string.strip().lower()
                lang_span.decompose() # 移除语言标识 span

            # 移除代码块内的复制按钮等非代码元素
            for btn in element.select('button.copy, div.copy-button'): btn.decompose()
            
            plain_code_text = extract_code_from_element(element)

            if plain_code_text:
                placeholder = f"%%CODE_BLOCK_PLACEHOLDER_{code_block_counter}%%"
                code_blocks_data[placeholder] = {"lang": lang, "code": plain_code_text}
                
                # 用占位符替换整个代码块结构 (是 element 还是 parent_div?)
                # 如果是 div > pre > code, 应该替换最外层的 div
                replacement_target = parent_div if parent_div and selector == 'div[class*="language-"] pre' else element
                
                # 创建一个包含占位符的 <p> 标签来替换，markdownify 会处理 <p>
                placeholder_tag = soup.new_tag('p') 
                placeholder_tag.string = placeholder
                replacement_target.replace_with(placeholder_tag)
                
                processed_code_elements.add(replacement_target) # 标记已处理
                code_block_counter += 1
            elif element.get_text(strip=True): # 如果有文本但提取逻辑失败，保留原样让markdownify尝试
                print(f"警告：在 '{page_title}' 中为代码块 (选择器: {selector}) 提取纯文本失败，但元素内有文本，将由markdownify尝试处理。")
                processed_code_elements.add(element)
            else: # 如果代码块为空，直接移除
                element.decompose()


    # 2. 执行用户配置的常规 HTML 元素清理
    for selector in HTML_CLEANUP_SELECTORS:
        try:
            elements = soup.select(selector)
            for element in elements:
                if element not in processed_code_elements and not element.find_parent(lambda tag: tag in processed_code_elements):
                    element.decompose()
        except Exception as e:
            print(f"警告：在 '{page_title}' 中移除元素时出错 (选择器: {selector}): {e}")

    # 3. 移除图片、figure、script、style (再次确保)
    for img_tag in soup.find_all('img'): img_tag.decompose()
    for figure_tag in soup.find_all('figure'): figure_tag.decompose()
    for s in soup(['script', 'style']): s.decompose()
    
    return str(soup), code_blocks_data


def crawl_page_content(page, url: str, existing_titles: set) -> tuple[str | None, str | None]:
    # print(f"正在尝试爬取页面内容: {url}") 
    for exclusion_path in URL_PATH_EXCLUSIONS_FOR_CRAWL:
        if exclusion_path in url:
            print(f"信息：URL '{url}' 匹配排除路径 '{exclusion_path}'，将被完全跳过。")
            return None, None
    try:
        page.goto(url, timeout=60000)
        page.wait_for_load_state('networkidle', timeout=30000)
    except Exception as e_goto:
        print(f"错误：导航到或加载 {url} 失败: {e_goto}")
        return None, None

    raw_title = page.title()
    if "404" in raw_title or "not found" in raw_title.lower() or "page not found" in raw_title.lower() or "could not be found" in raw_title.lower():
        print(f"信息：检测到404页面，跳过: {url} (标题: {raw_title})")
        return None, None

    title = raw_title.strip()
    if TARGET_PAGE_TITLE_SUFFIX and title.endswith(TARGET_PAGE_TITLE_SUFFIX):
        title = title[:-len(TARGET_PAGE_TITLE_SUFFIX)].strip()
    
    unique_title = title
    url_path_for_title = url.strip('/').split('/')[-1] if '/' in url.strip('/') else url.strip('/').replace('.', '_')
    parsed_base_url_hostname = urlparse(_TARGET_WIKI_BASE_URL_EFFECTIVE).hostname
    generic_titles_to_avoid = ["home", "首页", "index", parsed_base_url_hostname if parsed_base_url_hostname else ""]
    if not unique_title or unique_title.lower() in generic_titles_to_avoid or unique_title in existing_titles :
        if url_path_for_title and url_path_for_title.lower() not in generic_titles_to_avoid and url_path_for_title != (urlparse(TARGET_WIKI_START_URL).hostname if urlparse(TARGET_WIKI_START_URL).hostname else "") :
            generated_title_part = url_path_for_title.replace('-', ' ').replace('_', ' ').replace(".html", "").replace(".htm","").title()
            potential_title = f"{title} - {generated_title_part}" if (title and title.lower() not in generic_titles_to_avoid) else generated_title_part
            if potential_title not in existing_titles: unique_title = potential_title
            else: unique_title = f"{potential_title}_{int(time.time())}"
        else: unique_title = f"{unique_title}_{int(time.time())}" if (unique_title and unique_title.lower() not in generic_titles_to_avoid) else f"PageFrom_{url_path_for_title.replace('/', '_')}_{int(time.time())}"
    if not unique_title: unique_title = f"untitled_from_{sanitize_filename(url)}_{int(time.time())}"
    existing_titles.add(unique_title)

    is_content_excluded_page = False
    for keyword in PAGE_TITLE_EXCLUSION_KEYWORDS:
        if keyword.lower() in unique_title.lower():
            is_content_excluded_page = True
            break
    
    content_html_raw = ""
    try:
        if MAIN_CONTENT_CSS_SELECTOR:
            main_content_element = page.locator(MAIN_CONTENT_CSS_SELECTOR)
            if main_content_element.count() > 0:
                try: content_html_raw = main_content_element.first.inner_html(timeout=10000) 
                except Exception: 
                    print(f"警告：使用选择器 '{MAIN_CONTENT_CSS_SELECTOR}' 获取 inner_html 时出错 for '{unique_title}'。尝试 page.content()。")
                    content_html_raw = page.content() 
            if not content_html_raw: # 如果使用主要选择器后内容仍为空 (例如选择器不匹配任何元素)
                 print(f"警告：主要选择器 '{MAIN_CONTENT_CSS_SELECTOR}' 未提取到任何 HTML 内容 for '{unique_title}'。尝试 page.content()。")
                 content_html_raw = page.content() 
        else: # 如果用户没有配置主要选择器
            print(f"警告：未配置 MAIN_CONTENT_CSS_SELECTOR。将尝试提取整个页面 HTML for '{unique_title}'。")
            content_html_raw = page.content() # 获取整个页面的HTML
    except Exception as e_selector:
        print(f"警告：提取HTML内容时出错 for '{unique_title}': {e_selector}。尝试 page.content()。")
        try: content_html_raw = page.content()
        except Exception as e_body_fallback:
            print(f"错误：提取 {url} 的 page content 也失败: {e_body_fallback}")
            return unique_title, None

    if not content_html_raw:
        print(f"警告：未能为 {url} 提取到任何 HTML 内容")
        return unique_title, None

    if is_content_excluded_page:
        print(f"信息：页面 '{unique_title}' (来自URL: {url}) 内容被排除（基于标题关键词），仅保留标题和提示。")
        return unique_title, f"\n\n(此部分内容 '{unique_title}' 因类型（如更新日志等）被精简，详情请参考原始文档)\n\n"

    # 在转换为 Markdown 之前，清理 HTML 并提取代码块
    cleaned_html, extracted_code_blocks = clean_html_before_markdownify(content_html_raw, unique_title)
    
    if not cleaned_html.strip():
        print(f"警告：HTML内容在清理后为空 for '{unique_title}'。")
        return unique_title, ""

    try:
        md_options = {'heading_style': 'atx', 'strip': ['img', 'figure', 'script', 'style', 'iframe', 'button', 'input', 'select', 'textarea']}
        if not HTML_CLEANUP_SELECTORS or len(HTML_CLEANUP_SELECTORS) <= 10 : 
            md_options['strip'].extend(['nav', 'footer', 'aside', 'header']) # 如果用户没怎么配置清理，让markdownify更激进
        
        markdown_content = markdownify.markdownify(cleaned_html, **md_options)
        
        # 将占位符替换回格式化后的代码块
        for placeholder, code_data in extracted_code_blocks.items():
            lang_hint = code_data['lang'] if code_data['lang'] else ''
            # 确保代码块前后有空行，除非占位符本身就在行首/行尾
            formatted_code_block = f"\n```{lang_hint}\n{code_data['code']}\n```\n"
            markdown_content = markdown_content.replace(placeholder, formatted_code_block)

        # 应用用户配置的 Markdown 文本清理规则
        for item in MARKDOWN_CLEANUP_PATTERNS:
            pattern, replacement, flags = item[0], item[1], item[2] if len(item) > 2 else 0
            try: markdown_content = re.sub(pattern, replacement, markdown_content, flags=flags | re.UNICODE)
            except Exception as e_re: print(f"警告：应用Markdown清理模式 '{pattern}' 时出错: {e_re}")
        
        markdown_content = markdown_content.strip() # 最后再清理一次首尾空白

        if not markdown_content:
            print(f"警告：Markdown 内容在清理后为空 for '{unique_title}'。")
            return unique_title, ""
        return unique_title, markdown_content
    except Exception as e_md:
        print(f"错误：为 {url} 将 HTML 转换为 Markdown 或后处理失败: {e_md}")
        return unique_title, f"# {unique_title}\n\n错误：Markdown转换或后处理失败: {e_md}"

def generate_toc_entry(title: str, depth: int = 1) -> str:
    anchor = title.lower(); anchor = re.sub(r'\s+', '-', anchor) 
    anchor = re.sub(r'[^\w\s\u4e00-\u9fff-]+', '', anchor, flags=re.UNICODE) 
    anchor = re.sub(r'-+', '-', anchor); anchor = anchor.strip('-')
    if not anchor : anchor = f"section-{uuid.uuid4().hex[:8]}"
    return f"- [{title}](#{anchor})"

def merge_markdown_files(page_details_list: list, base_output_dir: str, individual_files_subdir_path: str, output_filename_base: str = "Wiki_All_In_One"):
    parsed_start_url = urlparse(TARGET_WIKI_START_URL)
    site_name_part = parsed_start_url.hostname.replace('www.', '').replace('.', '_') if parsed_start_url.hostname else "untitledwiki"
    final_output_filename = f"{site_name_part}_{output_filename_base}.md"
    output_filepath = os.path.join(base_output_dir, final_output_filename)
    
    print(f"\n开始合并 {len(page_details_list)} 个 Markdown 文件到: {output_filepath}...")
    toc_entries = [f"# {site_name_part.replace('_', ' ').title()} 文档目录 (AI 精简版)\n"]
    valid_pages_for_toc_and_merge = []

    for detail in page_details_list:
        page_title, filepath = detail.get("title"), detail.get("filepath")
        if not page_title: continue
        if filepath and os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as infile_check:
                content_sample = infile_check.read(500) 
                if content_sample.strip() and "错误：" not in content_sample:
                    toc_entries.append(generate_toc_entry(page_title))
                    valid_pages_for_toc_and_merge.append(detail)
                elif "(此部分内容" in content_sample and "被精简" in content_sample: 
                    toc_entries.append(generate_toc_entry(page_title))
                    valid_pages_for_toc_and_merge.append(detail) 
        elif page_title and not filepath: 
            is_intentionally_skipped = any(keyword.lower() in page_title.lower() for keyword in PAGE_TITLE_EXCLUSION_KEYWORDS)
            if is_intentionally_skipped:
                toc_entries.append(generate_toc_entry(page_title))
                valid_pages_for_toc_and_merge.append({"title": page_title, "filepath": None, "content_override": f"\n\n(此部分内容 '{page_title}' 因类型被精简)\n\n"})
    
    if not valid_pages_for_toc_and_merge:
        print("没有有效的页面可供合并。"); cleanup_temp_dir(individual_files_subdir_path); return

    toc_markdown = "\n".join(toc_entries) + "\n\n---\n\n"
    with open(output_filepath, "w", encoding="utf-8") as outfile:
        outfile.write(toc_markdown)
        for detail in valid_pages_for_toc_and_merge:
            filepath, page_title = detail.get("filepath"), detail.get("title", "未知章节")
            outfile.write(f"\n# {page_title}\n\n") 
            if filepath and os.path.exists(filepath):
                try:
                    with open(filepath, "r", encoding="utf-8") as infile:
                        file_content = infile.read().strip()
                        if file_content: outfile.write(file_content)
                        elif "(此部分内容" in file_content and "被精简" in file_content: outfile.write(file_content)
                        else: outfile.write(f"(页面 '{page_title}' 内容为空)\n")
                except Exception as e: outfile.write(f"(读取文件 {os.path.basename(filepath)} 出错: {e})\n")
            elif detail.get("content_override"): outfile.write(detail.get("content_override"))
            outfile.write("\n\n---\n\n")
    print(f"成功合并到: {output_filepath}")
    cleanup_temp_dir(individual_files_subdir_path)

def cleanup_temp_dir(dir_path):
    if os.path.exists(dir_path):
        try:
            shutil.rmtree(dir_path)
            print(f"已删除临时目录: {dir_path}")
        except OSError as e:
            print(f"错误：删除临时目录 {dir_path} 失败: {e}")

def main():
    global _TARGET_WIKI_BASE_URL_EFFECTIVE, temp_individual_files_dir 
    setup_global_config_from_input() 
    if not TARGET_WIKI_START_URL: print("错误：未提供有效的起始 URL。"); return

    if not TARGET_WIKI_BASE_URL: 
        parsed_url = urlparse(TARGET_WIKI_START_URL)
        _TARGET_WIKI_BASE_URL_EFFECTIVE = f"{parsed_url.scheme}://{parsed_url.netloc}"
    else: _TARGET_WIKI_BASE_URL_EFFECTIVE = TARGET_WIKI_BASE_URL.strip('/')
    
    print(f"配置信息:\n  起始 URL: {TARGET_WIKI_START_URL}\n  基础 URL: {_TARGET_WIKI_BASE_URL_EFFECTIVE}")
    print(f"  主要内容选择器: {MAIN_CONTENT_CSS_SELECTOR if MAIN_CONTENT_CSS_SELECTOR else '未指定 (将尝试提取body)'}")

    crawled_page_details = [] 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS_BROWSER)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 WikiCrawler/2.2",
            java_script_enabled=True )
        context.set_default_navigation_timeout(60000); context.set_default_timeout(30000) 
        page = context.new_page()
        url_queue, crawled_urls_set, existing_titles, pages_crawled_count = [TARGET_WIKI_START_URL.strip('/')], set(), set(), 0
        print(f"单个 Markdown 文件将临时保存在: {os.path.abspath(temp_individual_files_dir)}")

        while url_queue and pages_crawled_count < MAX_PAGES_TO_CRAWL:
            current_url_to_crawl = url_queue.pop(0) 
            if current_url_to_crawl in crawled_urls_set: continue
            
            skip_url = any(ex_path in current_url_to_crawl for ex_path in URL_PATH_EXCLUSIONS_FOR_CRAWL if ex_path) 
            if skip_url: crawled_urls_set.add(current_url_to_crawl); continue

            print(f"\n正在处理 ({pages_crawled_count + 1}/{MAX_PAGES_TO_CRAWL}): {current_url_to_crawl}")
            title_for_file, md_content = crawl_page_content(page, current_url_to_crawl, existing_titles)
            crawled_urls_set.add(current_url_to_crawl); pages_crawled_count += 1
            
            saved_filepath = None
            if title_for_file:
                if md_content is not None:
                    filename = os.path.join(temp_individual_files_dir, f"{sanitize_filename(title_for_file)}.md")
                    try:
                        with open(filename, "w", encoding="utf-8") as f: f.write(md_content) 
                        saved_filepath = filename
                    except OSError as e: print(f"错误：保存临时文件 {filename} 失败: {e}")
                crawled_page_details.append({"title": title_for_file, "filepath": saved_filepath, "original_url": current_url_to_crawl})

            try: current_page_url_for_join = page.url if page.url.startswith("http") else current_url_to_crawl
            except Exception: current_page_url_for_join = current_url_to_crawl

            if current_page_url_for_join.startswith(current_url_to_crawl.split('?')[0].split('#')[0]):
                try:
                    for link_element in page.locator("a[href]").all():
                        href = link_element.get_attribute("href")
                        if not href: continue
                        abs_url = urljoin(current_page_url_for_join, href)
                        cleaned_url = abs_url.split('?')[0].split('#')[0].strip('/')
                        if any(ex_path in cleaned_url for ex_path in URL_PATH_EXCLUSIONS_FOR_CRAWL if ex_path): continue
                        if cleaned_url.startswith(_TARGET_WIKI_BASE_URL_EFFECTIVE) and \
                           len(cleaned_url) > len(_TARGET_WIKI_BASE_URL_EFFECTIVE.rstrip('/')) and \
                           cleaned_url not in crawled_urls_set and cleaned_url not in url_queue and \
                           not any(cleaned_url.endswith(ext) for ext in [".zip", ".jpg", ".pdf", ".png", ".svg", ".json", ".xml"]) and \
                           "mailto:" not in cleaned_url.lower() and "tel:" not in cleaned_url.lower():
                            if len(url_queue) < MAX_PAGES_TO_CRAWL * 2: url_queue.append(cleaned_url)
                except Exception as e: print(f"错误：在 {current_url_to_crawl} 上发现链接时发生错误: {e}")
            time.sleep(POLITENESS_DELAY) 

        print(f"\n爬取完成。总共处理页面数: {pages_crawled_count}")
        browser.close() 
        if crawled_page_details: merge_markdown_files(crawled_page_details, OUTPUT_DIR_BASE, temp_individual_files_dir)
        else: print("没有有效页面可供合并。"); cleanup_temp_dir(temp_individual_files_dir)
        
        hostname = urlparse(TARGET_WIKI_START_URL).hostname or "untitledwiki"
        final_doc_name = f"{hostname.replace('www.', '').replace('.', '_')}_Wiki_All_In_One.md"
        final_doc_path = os.path.join(OUTPUT_DIR_BASE, final_doc_name)
        if os.path.exists(final_doc_path): print(f"所有操作完成。最终合并的 Markdown 文件位于: {os.path.abspath(final_doc_path)}")
        else: print(f"所有操作完成，但最终合并文件 '{final_doc_path}' 未生成。请检查日志。")

if __name__ == "__main__":
    main()
