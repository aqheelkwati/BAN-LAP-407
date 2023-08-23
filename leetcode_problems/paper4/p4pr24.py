import os

files = [f for f in os.listdir() if '.txt' in f.lower() or   '.csv' in f.lower()]

for file in files:
    if file.endswith('.csv'):
        new_path1 = 'csv_d/' + file
        os.rename(file, new_path1)
    else:
        new_path = 'txt_d/' + file
    os.rename(file, new_path)

