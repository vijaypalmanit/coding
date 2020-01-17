import os
list=os.listdir('D:\Personal\Personal\Investment Proofs Submission FY 2019-20\Broadband Bills')
print(list)

for filename in list:
    if filename in ['Backup','rename.py']:
        continue
    else:
         name       = filename.split('.')[0]
         extension = filename.split('.')[1]
         os.rename(filename,name+' '+'2019'+'.'+extension)