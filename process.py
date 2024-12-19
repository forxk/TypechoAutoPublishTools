import os

def get_all_files(directory):
    """返回指定目录及其子目录中所有文件的完整路径"""
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files

# print(get_all_files('source'))

def process_file(file):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 获取文件名（不带扩展名）
    filename = os.path.splitext(os.path.basename(file))[0]
    name = filename.split('写真')[0].split('期')[-1]
    
    # 生成 Markdown 文件内容
    markdown_content = f"""---
title: "{filename}"
tags: 
- 秀人
- 写真
- {name}
categories:
- 秀人
- 写真
---

{content}
"""
    # 写入新的 Markdown 文件
    output_file = f"_posts/{filename}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

for file in get_all_files('source'):
    if file == 'source/.DS_Store':
        continue
    process_file(file)