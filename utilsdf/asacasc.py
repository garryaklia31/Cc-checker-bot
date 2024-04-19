import requests

bin = input("enter bin : ")

cookies = {
    '_gid': 'GA1.2.1707906897.1696948597',
    'dom3ic8zudi28v8lr6fgphwffqoz0j6c': '3e94a55f-1389-4d57-adff-ad9ad36e7ffb%3A1%3A1',
    '_ga': 'GA1.1.1175969531.1696948596',
    '_ga_7SVC6KCCG1': 'GS1.1.1696948596.1.1.1696948634.0.0.0',
    'cf_clearance': 'uf4QjLv4G5c1qrOq_yg8Idb3.nFaKWGGHpNrAaFNecg-1696949444-0-1-62815a88.f80f4543.74b5db47-0.2.1696949444',
    'PHPSESSID': '68f7fca46396ede5e541a1b6f47b5be6',
}

headers = {
    'authority': 'bincodes.net',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.1707906897.1696948597; dom3ic8zudi28v8lr6fgphwffqoz0j6c=3e94a55f-1389-4d57-adff-ad9ad36e7ffb%3A1%3A1; _ga=GA1.1.1175969531.1696948596; _ga_7SVC6KCCG1=GS1.1.1696948596.1.1.1696948634.0.0.0; cf_clearance=uf4QjLv4G5c1qrOq_yg8Idb3.nFaKWGGHpNrAaFNecg-1696949444-0-1-62815a88.f80f4543.74b5db47-0.2.1696949444; PHPSESSID=68f7fca46396ede5e541a1b6f47b5be6',
    'origin': 'https://bincodes.net',
    'referer': 'https://bincodes.net/bin-checker',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'bin_number': bin,
    'action': 'bin_ccn_generator',
}

response = requests.post('https://bincodes.net/ajax/bin-checker.php', cookies=cookies, headers=headers, data=data)

Bin = response.json()['bin_id']
Brand = response.json()['brand']
Type = response.json()['type']
Level = response.json()['level']
Country = response.json()['country']
Bank = response.json()['bank_name']
Bank_WebSite = response.json()['bank_website']
Bank_Phone = response.json()['bank_phone']

print(f'''bin : {Bin}''')
print(f'''Brand : {Brand}''')
print(f"Type : {Type}")
print(f"Level : {Level}")
print(f"Country : {Country}")
print(f"Bank : {Bank}")
print(f"Bank webSite : {Bank_WebSite}")
print(f"Bank Phone : {Bank_Phone}")