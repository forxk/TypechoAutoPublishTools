import os
import random
import string
from randoms import *

def get_all_files(directory):
    """返回指定目录及其子目录中所有文件的完整路径"""
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 拼接完整路径
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files

def process_file(file):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    # 获取文件名（不带扩展名）
    filename = os.path.splitext(os.path.basename(file))[0]
    name = filename.split('写真')[0].split('期')[-1]
    
    # 生成 Markdown 文件内容
    markdown_content = f"""---
title: "{filename}"
tags: 
- 模特学院
- 写真
- {name}
categories:
- 模特学院
- 写真
---

"""
    # 添加图链语法
    for line in lines:
        line = line.strip()
        if line:
            markdown_content += f"![]({line})\n"
    
    # 写入新的 Markdown 文件
    output_file = f"_posts/{filename}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    # 日志记录
    print(f"Generated Markdown content for {file}:\n{markdown_content}")

if __name__ == '__main__':
    res = get_all_files('source')
    for path in res:
        if path == 'source/.DS_Store':
            continue
        process_file(path)
    print(res)
    folder = '_posts'
    rename_files_with_random_string(folder, length=8)