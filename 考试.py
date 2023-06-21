import requests
import json
from bs4 import BeautifulSoup
import csv

def save_array_to_csv(arr, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(arr)
def get_image_links(url):
    newlist = []
    data = {
        "pageNo": "1",
        "pageSize": "15",
        "isin": "",
        "bondCode": "",
        "issueEnty": "",
        "bondType": "100001",
        "couponType": "",
        "issueYear": "2023",
        "rtngShrt": "",
        "bondSpclPrjctVrty": ""
    }

    response = requests.post(url,data = data)
    # print(response)
    if response.status_code != 200:
        print(f'Error fetching data from {base_url}: {response.status_code}')
        return
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    info_dict = json.loads(str(soup))
    print(info_dict["data"])
    for i in info_dict["data"]['resultList']:
        print(i)
        newlist.append([i['isin'],i['bondCode'],i['issueStartDate'],i['bondTypeCode'],i['entyDefinedCode']])
    print(newlist)
    return newlist
if __name__ == '__main__':
    url = 'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN'
    image_links = get_image_links(url)
    save_array_to_csv(image_links, r'C:\Users\Administrator\Desktop\新疆石油改\考试file.csv')