def is_exe_file(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(2)
    
    if header == b'\x4D\x5A':
        return 1
    else:
        return 0

file_path = 'example.exe'
result = is_exe_file(file_path)
if result == 1:
    print(f'Файл {file_path} является EXE-файлом')
else:
    print(f'Файл {file_path} не является EXE-файлом')