from openpyxl import load_workbook
import io
def read_file_line(file_name):
    f = io.open(file_name, 'r',encoding = 'utf-8')
    ndung=f.read().split('\n')
    f.close()
    return ndung
def update_cell(file_path,sheet_name,cell_name,new_value):
    wb = load_workbook(filename = file_path)
    wb[sheet_name][cell_name].value = new_value
    wb.close()
    wb.save(file_path)
if __name__ =="__main__":
    file_path = 'file_excel.xlsx'
    sheet_name = 'Sheet1'
    file1 ='file_1.txt'
    file2 ='file_2.txt'
    L1 = read_file_line(file1)
    L2 = read_file_line(file2)
    for i in range(0,len(L1)):
        user = L1[i]
        num = L2[i]
        cell_name_user ="A%s"%(i+1)
        cell_name_num ="B%s"%(i+1)
        update_cell(file_path,sheet_name,cell_name_user,user)
        update_cell(file_path,sheet_name,cell_name_num,num)

