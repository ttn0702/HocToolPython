from openpyxl import load_workbook
import io
import re
import bs4
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

class String_Interact():
    def __init__(self):
        pass
    def regex_one_value(self,pattern,input_str):
        regex = re.compile(pattern)
        kq = regex.search(input_str)
        if kq:
            return kq.group(1)
        else:
            return ''
    def regex_many_value(self,pattern,input_str):
        regex = re.compile(pattern)
        kq = regex.findall(input_str)
        return kq
    
    def get_element_by_css_selector(self, data, css_selector):
        soup = bs4.BeautifulSoup(data, 'html.parser')
        eles=soup.select(css_selector)
        return eles #get_text() and get('href')

    def extractListTextByCSSSelector(self,data,listCSSSelector,listeAttr):
        list_L_result = []
        for index, _ in enumerate(listCSSSelector):
            CSSSelector = listCSSSelector[index]
            Attr = listeAttr[index]
            L_result = self.get_element_by_css_selector(data,CSSSelector)
            if Attr == "innerText":
                L_result = [img_src.get_text().replace("\n","").replace("\t","").replace("\r","").strip() for img_src in L_result]
            elif Attr == "innerHTML":
                L_result = ["%s"%img_src for img_src in L_result]
            elif Attr == "origin":
                L_result = L_result
            else:    
                L_result = [img_src.get(Attr) for img_src in L_result]
            list_L_result.append(L_result)
        return list_L_result