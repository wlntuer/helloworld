import hashlib


def get_file_md5(file_path):
    """
    获取文件md5值
    :param file_path: 文件路径名
    :return: 文件md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).upper()


md5 = get_file_md5('C://Users/wlntu/Desktop/数据整合问题讨论20191209.md')
print(md5)
