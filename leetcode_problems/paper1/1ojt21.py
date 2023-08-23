# 21. How do you open a file of large size, say around 10GB? So that program should not
# Crash
# with open('large_file.txt', 'rb') as f:
with open('file1.txt','rb') as f:
    chunk_size = 1024 # read 1KB at a time
    while True:
        chunk = f.read(chunk_size)
        print(chunk)
        if not chunk:
            break