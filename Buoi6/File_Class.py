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
    
    def read_file_list(seft):
        f = io.open(seft.file_name, 'r',encoding = 'utf-8')
        ndung=f.read()
        f.close()
        return ndung.split('\n')

class File_Excel():
    def __init__(self,file_name):
        self.file_name =file_name
    def read_file_line(self):
        f = io.open(self.file_name, 'r',encoding = 'utf-8')
        ndung=f.read().split('\n')
        f.close()
        return ndung
    def update_cell(self,sheet_name,cell_name,new_value):
        wb = load_workbook(filename = self.file_name)
        wb[sheet_name][cell_name].value = new_value
        wb.close()
        wb.save(self.file_name)
