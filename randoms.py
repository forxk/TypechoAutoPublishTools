import os
import random
import string

def rename_files_with_random_string(folder_path, length=8):
    """
    批量将文件夹下的文件重命名为随机字符串
    
    :param folder_path: 文件夹路径
    :param length: 随机字符串长度，默认为8位
    """
    # 生成随机字符串的函数
    def random_string(length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    # 遍历文件夹内文件并重命名
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(old_path):
            # 生成唯一的新文件名
            new_name = random_string(length) + os.path.splitext(filename)[1]
            new_path = os.path.join(folder_path, new_name)
            
            # 防止文件名重复
            while os.path.exists(new_path):
                new_name = random_string(length) + os.path.splitext(filename)[1]
                new_path = os.path.join(folder_path, new_name)
            
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_name}')

# # 示例调用
# folder = '/path/to/folder'
# rename_files_with_random_string(folder, length=8)
