import re
import os

def remove_specific_markdown_links(content):
  """
  更精确地去除 Markdown 文本中连续出现的、作为导航的链接。

  主要针对以下两种情况：
  1. 一行完全由两个或更多 Markdown 链接组成。
  2. 一行以两个或更多 Markdown 链接结尾。

  参数:
    content (str): 包含 Markdown 链接的文本内容。

  返回:
    str: 去除链接后的文本内容。
  """
  lines = content.splitlines()
  processed_lines = []

  # 定义单个 Markdown 链接的基本模式 (非捕获)
  # \[           # 匹配开头的 '['
  # [^\]]+      # 匹配链接文本 (一个或多个非 ']' 字符)
  # \]           # 匹配结尾的 ']'
  # \(           # 匹配开头的 '('
  # [^\)]+      # 匹配链接 URL (一个或多个非 ')' 字符)
  # \s* # 匹配零个或多个空格
  # (?:\"[^\"]+\")? # 匹配可选的用双引号括起来的标题 (非捕获组)
  # \)           # 匹配结尾的 ')'
  single_link_raw_pattern = r"\[[^\]]+\]\([^\)]+\s*(?:\"[^\"]+\")?\)"
  
  # 匹配一个 Markdown 链接，前后允许有空格 (用于构建连续链接模式)
  link_with_optional_spacing_pattern = r"\s*" + single_link_raw_pattern + r"\s*"

  for line in lines:
    original_line = line # 保留原始行用于调试或备用

    # 规则 1: 如果一行（忽略首尾空格）完全由两个或更多 Markdown 链接组成，则清空该行。
    # 例如: "[A](a) [B](b)" -> ""
    # 或者: "[A](a)[B](b)" -> ""
    # 模式: ^ \s* (链接 \s*){2,} \s* $
    full_line_multiple_links_pattern = r"^\s*(?:" + link_with_optional_spacing_pattern + r"){2,}\s*$"
    if re.fullmatch(full_line_multiple_links_pattern, line):
      processed_lines.append("") # 清空这一行
      continue

    # 规则 2: 如果一行以两个或更多 Markdown 链接结尾，移除这些链接，保留之前的内容。
    # 例如: "Text [A](a) [B](b)" -> "Text "
    # 模式: ^ (前缀文本) ( (链接 \s*){2,} ) \s* $
    # (.*?) : 捕获组1 (链接前的内容，非贪婪)
    # ( (?: 链接模式 ){2,} ) : 捕获组2 (两个或多个链接的块)
    # \s*$ : 行尾 (允许空格)
    end_with_multiple_links_pattern = r"^(.*?)((?:" + link_with_optional_spacing_pattern + r"){2,})\s*$"
    match_obj = re.match(end_with_multiple_links_pattern, line)
    if match_obj:
      # 保留链接前的内容 (捕获组1)，并去除可能多余的尾部空格
      prefix_text = match_obj.group(1).rstrip()
      processed_lines.append(prefix_text)
      continue
            
    # 如果没有被以上规则处理，则保留原行
    processed_lines.append(original_line)

  final_content = "\n".join(processed_lines)
  
  # 移除可能产生的连续空行 (3个或更多换行符替换为2个)
  final_content = re.sub(r'\n{3,}', '\n\n', final_content)
  
  return final_content

# 定义输入和输出文件名
input_file_path = "Stash_Wiki_Optimized_v2.md"
file_name, file_extension = os.path.splitext(input_file_path)
output_file_path = f"{file_name}_cleaned{file_extension}"

try:
  # 读取原始 Markdown 文件内容
  with open(input_file_path, 'r', encoding='utf-8') as file:
    markdown_content = file.read()

  # 调用函数去除特定链接
  cleaned_text = remove_specific_markdown_links(markdown_content)

  # 将处理后的文本保存到新文件
  with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(cleaned_text)
  
  print(f"处理完成，已将结果保存到: {output_file_path}")
  # 您可以取消下面的注释来预览清理后文件的前几行
  # print("\n文件内容预览 (前10行):")
  # print('\n'.join(cleaned_text.splitlines()[:10]))

except FileNotFoundError:
  print(f"错误：文件 {input_file_path} 未找到。请确保文件在脚本所在的目录下，或者提供正确的文件路径。")
except Exception as e:
  print(f"处理文件时发生错误：{e}")
