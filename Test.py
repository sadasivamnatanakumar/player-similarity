import pandas as pd
import xlsxwriter

df = pd.read_excel("C:/Users/bornf/Desktop/astro quiz.xlsx")
df.fillna(0)

participants = []

for rowIndex, row in df.iterrows(): 
    for columnIndex, value in row.items():
        if not value in participants:
            participants.append(value)
            
participants_tally = []

for obj in participants:
    count = 0
    for rowIndex, row in df.iterrows(): 
        for columnIndex, value in row.items():
            if obj == value:
                count+=1
    participants_tally.append([obj,count])
    

participants_tally.sort(key=lambda x:x[1],reverse=True)

participants_tally.pop()
print(participants_tally)
with xlsxwriter.Workbook('C:/Users/bornf/Desktop/Results.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(participants_tally):
        worksheet.write_row(row_num, 0, data)
        
        