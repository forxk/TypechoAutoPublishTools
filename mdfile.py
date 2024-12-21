import os

def get_all_files(directory):
    """返回指定目录及其子目录中所有文件的完整路径"""
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 拼接完整路径
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files


if __name__ == '__main__':
    res = get_all_files('source')
    for path in res:
        with open(path, 'r') as f:
            filename = path.split('/')[-1]
            with open(f'markdowns/{filename.split('.')[0]}.md', 'w') as f2:
                f2.write(f'# {filename.split('.')[0]}\n')
                for line in f.readlines():
                  line = line.strip()
                  f2.write(f'![{line}]({line})\n')
            print(path.split('/')[-1])
            # print(f.read())
    print(res)