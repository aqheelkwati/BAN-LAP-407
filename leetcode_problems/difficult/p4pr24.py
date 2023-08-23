import os

files=[file for file in os.listdir() if file.endswith('.jpg') or file.endswith('.txt')]
print(files)
for file in files:
    if file.endswith('jpg'):
        newpath=f'24/{file}'
        os.rename(file,newpath)