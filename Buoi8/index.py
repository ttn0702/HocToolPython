from File_Class import *
import requests 

List_total = []
String_Interact1 = String_Interact()

for page_number in range(1,5):
    url = f'https://etherscan.io/accounts/{page_number}'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    res = requests.get(url,headers=header).text
    
    listCSSSelector = [
        '.table tr',
        
    ]
    listeAttr = [
        'innerHTML'
    ]
    L0, = String_Interact1.extractListTextByCSSSelector(res,listCSSSelector=listCSSSelector,listeAttr=listeAttr)

    for index,value in enumerate(L0):
        if index == 0:
            continue
        else:
            listCSSSelector = [
                'td'
            ]
            listeAttr = [
                'innerText'
            ]
            L1, = String_Interact1.extractListTextByCSSSelector(value,listCSSSelector=listCSSSelector,listeAttr=listeAttr)
            List_total.append(L1)

File_Excel1 = File_Excel('data.xlsx')
sheet_name = 'Sheet1'
File_Excel1.update_cell(sheet_name,'A1','Rank')
File_Excel1.update_cell(sheet_name,'B1',"Address")
File_Excel1.update_cell(sheet_name,'C1',"Name Tag")
File_Excel1.update_cell(sheet_name,'D1',"Balance")
File_Excel1.update_cell(sheet_name,'E1',"Percentage")
File_Excel1.update_cell(sheet_name,'F1',"Txn Count")

for index,value in enumerate(List_total):
    rank = value[0]
    address = value[1]
    name_tag = value[2]
    balance = value[3]
    percentage = value[4]
    txn_count = value[5]
    
    cell_name_rank ="A%s"%(index+2)
    cell_name_address ="B%s"%(index+2)
    cell_name_name_tag ="C%s"%(index+2)
    cell_name_balance ="D%s"%(index+2)
    cell_name_percentage ="E%s"%(index+2)
    cell_name_txn_count ="F%s"%(index+2)

    File_Excel1.update_cell(sheet_name,cell_name_rank,rank)
    File_Excel1.update_cell(sheet_name,cell_name_address,address)
    File_Excel1.update_cell(sheet_name,cell_name_name_tag,name_tag)
    File_Excel1.update_cell(sheet_name,cell_name_balance,balance)
    File_Excel1.update_cell(sheet_name,cell_name_percentage,percentage)
    File_Excel1.update_cell(sheet_name,cell_name_txn_count,txn_count)
