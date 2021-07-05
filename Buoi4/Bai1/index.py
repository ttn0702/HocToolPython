from file_class import *

file_name = File_Interact('name.txt')
L_name = file_name.read_file_line()

file_age = File_Interact('tuoi.txt')
L_age = file_age.read_file_line()

file_info = File_Interact('info.txt')
for i in range(len(L_name)):
    L = '%s %s'%(L_name[i],L_age[i])
    file_info.write_file_line(L)
