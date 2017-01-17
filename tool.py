def transUTF8toAscii(fs_path):
    if isinstance(fs_path,unicode) :
        fs_path = fs_path.decode('utf8').encode('ascii')
    return fs_path