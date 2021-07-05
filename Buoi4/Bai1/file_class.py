from openpyxl import load_workbook
import io
class File_Interact():
    def __init__(self,file_name):
        self.file_name =file_name
    def write_file(seft, ndung):
        f = io.open(seft.file_name, 'w',encoding = 'utf-8')
        f.write(ndung)
        f.close
    def write_file_from_list(seft,list_line):
        f = io.open(seft.file_name, 'w',encoding = 'utf-8')
        f.write('\n'.join(list_line))
        f.close()
    def write_file_line(seft,ndung_line):
        f = io.open(seft.file_name, 'a',encoding = 'utf-8')
        f.write('%s\n'%ndung_line)
        f.close()
    def read_file_line(seft):
        f = io.open(seft.file_name, 'r',encoding = 'utf-8')
        ndung=f.read()
        f.close()
        return ndung
    def read_file_line(seft):
        f = io.open(seft.file_name, 'r',encoding = 'utf-8')
        ndung=f.read()
        f.close()
        return ndung.split('\n')

