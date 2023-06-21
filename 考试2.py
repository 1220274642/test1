import csv

def read_csv_to_list(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_list.append(row)
    return data_list

def split_list(lst, batch_size):
    for i in range(0, len(lst), batch_size):
        yield lst[i:i + batch_size]

csv_file_path = r'C:\Users\Administrator\Desktop\fyx_chinamoney.csv'  # 替换为你的 CSV 文件路径
batch_size = 80

my_list = read_csv_to_list(csv_file_path)

for batch in split_list(my_list, batch_size):
    print(batch)