import io
def write_file(file_name, ndung):
    f = io.open(file_name, 'w',encoding = 'utf-8')
    f.write(ndung)
    f.close
def write_file_from_list(file_name,list_line):
    f = io.open(file_name, 'w',encoding = 'utf-8')
    f.write('\n'.join(list_line))
    f.close()
def write_file_line(file_name,ndung_line):
    f = io.open(file_name, 'a',encoding = 'utf-8')
    f.write('%s\n'%ndung_line)
    f.close()
def read_file_line(file_name):
    f = io.open(file_name, 'r',encoding = 'utf-8')
    ndung=f.read()
    f.close()
    return ndung
def read_file_line(file_name):
    f = io.open(file_name, 'r',encoding = 'utf-8')
    ndung=f.read()
    f.close()
    return ndung.split('\n')
if __name__ == "__main__":
    file_name = "test.txt"
    L = read_file_line(file_name)
    print(L)