import sys, subprocess, re

class UnsupportedOsError(Exception): 
    def __init__(self):
        super().__init__('this method does not support current OS')

def get_fileinfo(file_path):
    if not sys.platform.startswith('win'):
        output = subprocess.Popen(['file', file_path], stdout=subprocess.PIPE).communicate()[0]
        return output.decode().strip()
    else: raise UnsupportedOsError

def find_flag(flag, file_path):
    file = open(file_path, 'r')
    data = file.read()
    p = re.compile(flag + '\{.{0,}\}')
    return p.findall(data)
