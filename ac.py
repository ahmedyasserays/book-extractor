import shutil

base_path = 'C:/Users/AHMED/AppData/Local/Temp/flipBuilder/flipexe/files/mobile/'
book = 'waves'
pages = 127
for i in range(pages):
    path = base_path + f'{i+1}.jpg'
    new_path = f'{book}-{i+1}.jpg'
    shutil.copyfile(path, new_path)
    print(i)
    
    
    
