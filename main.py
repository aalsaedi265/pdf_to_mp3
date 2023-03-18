import os

file_path=r'c:\Users\16075\Downloads\event.ics'


#check if path esists 
if os.path.exists(file_path):
    print('yeeeeeeeeeeeeeeeeeeeee')
else:
    print('noooooooooooooooooooo')

#checks if thefiel is really there
with os.open(file_path,os.O_RDONLY) as f:
    print(f)
    




if os.path.isfile(file_path):
    os.remove(file_path)
    print('bite the dust')
else:
    print('king crimson')
    