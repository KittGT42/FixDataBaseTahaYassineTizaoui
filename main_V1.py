import csv
import time

import requests
from bs4 import BeautifulSoup
import json
from notifiers import get_notifier


TOKEN = '7323608342:AAE4wNHiFs9tQMFgqutKkaJmhCeM2LzL3mQ'
CHAT_ID = '324015551'

username = "u85352297558c05c3-zone-custom-region-us"
password = "u85352297558c05c3"
PROXY_DNS = "43.159.28.126:2334"
proxy = {"https":"http://{}:{}@{}".format(username, password, PROXY_DNS)}

cookies = {
    'AKA_A2': 'A',
    'bm_mi': 'F6FA854FD4160EFFB60038DD5BDA8036~YAAQayTDFwonzVqQAQAAtENBfhhSxlgOFlZ7mbvJMm3Xuq3c2TCbxzbPRJIReSMM770pABvHUbaCNRehilPFYItTr/nNCgBc5CGXW6YTIpmwIO3CsC0AZjAWBqAa2/aMPEyTQ/lEJfSn1R/NrGaW6OzOO0puWT0tLW+DRimbl6q0a2Q+GgUuWrtKdnjkdW6UW/m6+5OBk38uT8nUwZiRX/JKxquLwQhB0E82AGxJ8E+tB7zTBCaxhPY8jEEhQN4itYGDa4UDilew9HLrLLg1R8TRdR7lMCmYMV1IqfQn6xiZQXj7aAKhXcQvMGF3yWqHQIfB~1',
    'visitor_id': '92d09a18-6a60-4e95-a6fa-4e2ac09e08d0',
    'ak_bmsc': 'C791E5EFB62FA54616085A05B04C43EC~000000000000000000000000000000~YAAQayTDF6IpzVqQAQAAK1hBfhgtuyvEa86b9PEfMneRsbnaygO0VinfVPYSLNM3wuOd2oBCrNeNcimBlvTMDp1FHURwqdIiP7E8XmNUeguUaPPUcm5Wnl+PJHRkXEFql/6zgmfGWJHiiarVyP36ujG7qx8LVT6XawX24WN7LkBQKFRnJ6Fr8VeKUEFbCkThzTm2z60NZsBdIW+j36/jXYTSnHc629yVly461KzPzLKE3mK3Ri64RTRaBEPYRpCU86ojF2lSdFMt0J/X8z+hdMkqM1yDsNkwHeN2TPqklECQVh7wjpuzAbGiEKkiJsEQZ2fgtrCiTDYc6nsTXZqsnkA/kTgWNQxGoMTPQLed6ONjEY7U8kMF49zKWXGKsDOF0lcCnFXgtPvSv3Jlv2pIbxTudT4cVXY6MaNRQOwY7pllfoWg/aqFURDR/6J92HIR0YhwNxkV2o8Bysg1qa66O61VU18NBEdy7qBO+oSD1cn8zMfb',
    '_gcl_au': '1.1.884992829.1720105130',
    '_ga': 'GA1.2.1820979055.1720105168',
    '_gid': 'GA1.2.1305513592.1720105168',
    '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22ESOHCAM3IgNst0UQFbC3%22%7D',
    '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%7D',
    '_ym_uid': '1720105170311697895',
    '_ym_d': '1720105170',
    '_scid': '015b19a8-19f1-4bd3-a6bc-b28015e53033',
    '_ScCbts': '%5B%5D',
    '_fbp': 'fb.1.1720105173069.46575517599655031',
    '_sctr': '1%7C1720040400000',
    '__gads': 'ID=c5a2fe204a1a2e3a:T=1720105174:RT=1720105174:S=ALNI_MaT5UZGhtveXpxuohdPalFibT1LlQ',
    '__gpi': 'UID=00000a39e306d2fb:T=1720105174:RT=1720105174:S=ALNI_MbZMcqtdKjYVHOPf1MHn82PRrCvUg',
    '__eoi': 'ID=77beaff7f7f3ea38:T=1720105174:RT=1720105174:S=AA-AfjaTeVL0CZ-czxn87eLjZl4H',
    '_tt_enable_cookie': '1',
    '_ttp': '_ECYOCRSzf90jHdmx-WxyQ3XU2p',
    '_clck': 'n7patw%7C2%7Cfn6%7C0%7C1646',
    'nloc': 'en-sa',
    'review_lang': 'xx',
    '_etc': 'SlLpVTJygfa9mwax',
    'nguestv2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiJiNDdiNGZhNzY2NGU0MDFkYWMwZDdmMTAyYmMwNzA4MyIsImlhdCI6MTcyMDEwNzkyOCwiZXhwIjoxNzIwMTA4MjI4fQ.QIPldi2c85I0zzL_aTf_e4m2baMl_7xeb69O6DxVbys',
    '_uetsid': '031865b03a1611ef958847ddf30170a1',
    '_uetvid': '031894203a1611efa723cb0481da0994',
    '_scid_r': '015b19a8-19f1-4bd3-a6bc-b28015e53033',
    'bm_sv': 'BD045467B560347DE55520131FB75D84~YAAQayTDF2fp1FqQAQAAHxJsfhh4dBbWkaPNQa1fGB6+Hzf/bT8biIbRlF1oG3BPuStAGd0HXi20yPevWT9Q2usE/fWhInY0B8XPvBWhDuxNS8GWLLqgg5HMtmjt/F6aC16TpR2CrVUOMIXIb8BH4pcApvWkJ6nBFiwXu6oyg4Za3J3Rod69VzMpws90iqdUnJuqiHPp/uPFp8FMbF94Tyt5uslUIMuyscXyHazNDIvoRcarTIaSGu0FqQIhIuQ=~1',
    '_clsk': 'yqho8h%7C1720108418493%7C3%7C1%7Cm.clarity.ms%2Fcollect',
    'RT': '"z=1&dm=noon.com&si=70c2df7c-a902-400a-bedd-aa3f78198390&ss=ly7fdtbu&sl=2&tt=9u2&rl=1&bcn=%2F%2F173bf10f.akstat.io%2F&obo=1&ld=r7ta&r=0b80765a52c30c14d62497fb51695d99&ul=r8l1&hd=r90s"',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk-UA;q=0.7,uk;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'AKA_A2=A; bm_mi=F6FA854FD4160EFFB60038DD5BDA8036~YAAQayTDFwonzVqQAQAAtENBfhhSxlgOFlZ7mbvJMm3Xuq3c2TCbxzbPRJIReSMM770pABvHUbaCNRehilPFYItTr/nNCgBc5CGXW6YTIpmwIO3CsC0AZjAWBqAa2/aMPEyTQ/lEJfSn1R/NrGaW6OzOO0puWT0tLW+DRimbl6q0a2Q+GgUuWrtKdnjkdW6UW/m6+5OBk38uT8nUwZiRX/JKxquLwQhB0E82AGxJ8E+tB7zTBCaxhPY8jEEhQN4itYGDa4UDilew9HLrLLg1R8TRdR7lMCmYMV1IqfQn6xiZQXj7aAKhXcQvMGF3yWqHQIfB~1; visitor_id=92d09a18-6a60-4e95-a6fa-4e2ac09e08d0; ak_bmsc=C791E5EFB62FA54616085A05B04C43EC~000000000000000000000000000000~YAAQayTDF6IpzVqQAQAAK1hBfhgtuyvEa86b9PEfMneRsbnaygO0VinfVPYSLNM3wuOd2oBCrNeNcimBlvTMDp1FHURwqdIiP7E8XmNUeguUaPPUcm5Wnl+PJHRkXEFql/6zgmfGWJHiiarVyP36ujG7qx8LVT6XawX24WN7LkBQKFRnJ6Fr8VeKUEFbCkThzTm2z60NZsBdIW+j36/jXYTSnHc629yVly461KzPzLKE3mK3Ri64RTRaBEPYRpCU86ojF2lSdFMt0J/X8z+hdMkqM1yDsNkwHeN2TPqklECQVh7wjpuzAbGiEKkiJsEQZ2fgtrCiTDYc6nsTXZqsnkA/kTgWNQxGoMTPQLed6ONjEY7U8kMF49zKWXGKsDOF0lcCnFXgtPvSv3Jlv2pIbxTudT4cVXY6MaNRQOwY7pllfoWg/aqFURDR/6J92HIR0YhwNxkV2o8Bysg1qa66O61VU18NBEdy7qBO+oSD1cn8zMfb; _gcl_au=1.1.884992829.1720105130; _ga=GA1.2.1820979055.1720105168; _gid=GA1.2.1305513592.1720105168; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22ESOHCAM3IgNst0UQFbC3%22%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%7D; _ym_uid=1720105170311697895; _ym_d=1720105170; _scid=015b19a8-19f1-4bd3-a6bc-b28015e53033; _ScCbts=%5B%5D; _fbp=fb.1.1720105173069.46575517599655031; _sctr=1%7C1720040400000; __gads=ID=c5a2fe204a1a2e3a:T=1720105174:RT=1720105174:S=ALNI_MaT5UZGhtveXpxuohdPalFibT1LlQ; __gpi=UID=00000a39e306d2fb:T=1720105174:RT=1720105174:S=ALNI_MbZMcqtdKjYVHOPf1MHn82PRrCvUg; __eoi=ID=77beaff7f7f3ea38:T=1720105174:RT=1720105174:S=AA-AfjaTeVL0CZ-czxn87eLjZl4H; _tt_enable_cookie=1; _ttp=_ECYOCRSzf90jHdmx-WxyQ3XU2p; _clck=n7patw%7C2%7Cfn6%7C0%7C1646; nloc=en-sa; review_lang=xx; _etc=SlLpVTJygfa9mwax; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiJiNDdiNGZhNzY2NGU0MDFkYWMwZDdmMTAyYmMwNzA4MyIsImlhdCI6MTcyMDEwNzkyOCwiZXhwIjoxNzIwMTA4MjI4fQ.QIPldi2c85I0zzL_aTf_e4m2baMl_7xeb69O6DxVbys; _uetsid=031865b03a1611ef958847ddf30170a1; _uetvid=031894203a1611efa723cb0481da0994; _scid_r=015b19a8-19f1-4bd3-a6bc-b28015e53033; bm_sv=BD045467B560347DE55520131FB75D84~YAAQayTDF2fp1FqQAQAAHxJsfhh4dBbWkaPNQa1fGB6+Hzf/bT8biIbRlF1oG3BPuStAGd0HXi20yPevWT9Q2usE/fWhInY0B8XPvBWhDuxNS8GWLLqgg5HMtmjt/F6aC16TpR2CrVUOMIXIb8BH4pcApvWkJ6nBFiwXu6oyg4Za3J3Rod69VzMpws90iqdUnJuqiHPp/uPFp8FMbF94Tyt5uslUIMuyscXyHazNDIvoRcarTIaSGu0FqQIhIuQ=~1; _clsk=yqho8h%7C1720108418493%7C3%7C1%7Cm.clarity.ms%2Fcollect; RT="z=1&dm=noon.com&si=70c2df7c-a902-400a-bedd-aa3f78198390&ss=ly7fdtbu&sl=2&tt=9u2&rl=1&bcn=%2F%2F173bf10f.akstat.io%2F&obo=1&ld=r7ta&r=0b80765a52c30c14d62497fb51695d99&ul=r8l1&hd=r90s"',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

# headers_csv = ['Title', 'Title_link', 'Thumbnail', 'price', 'oldPrice', 'discount', 'product_flag', 'product_flag1',
# 'rating', 'number of reviews', 'description', 'specifiations', 'model number', 'category', 'Brand',
# 'affected_area_category', 'affected_area_subcategory', 'product_category', 'possible_skin_conditions', 'score']
# with open('result.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(headers_csv)

counter = 3692


with open('noon_v5.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    for row in data[3693:]:
        counter += 1
        print(counter)
        print('******')
        print(row[0])
        try:
            result = requests.get(row[1], proxies=proxy, cookies=cookies, headers=headers, timeout=10)
        except:
            time.sleep(10)
            try:
                result = requests.get(row[1], proxies=proxy, cookies=cookies, headers=headers, timeout=10)
            except:
                time.sleep(10)
                try:
                    result = requests.get(row[1], proxies=proxy, cookies=cookies, headers=headers, timeout=10)
                except:
                    time.sleep(10)
                    try:
                        result = requests.get(row[1], proxies=proxy, cookies=cookies, headers=headers, timeout=10)
                    except:
                        telegram = get_notifier('telegram')
                        telegram.notify(token=TOKEN, chat_id=CHAT_ID, message='Something happened')
                        raise Exception('Something happened')
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'lxml')
            try:
                scripts = soup.find_all('script', type='application/ld+json')
                for script in scripts:
                    if 'image' in script.text:
                        result_script = script
                data = json.loads(result_script.string)
                try:
                    image = data['image'][0]
                except:
                    image = None
                    print(f'Images not found {row[1]}')
                name = soup.find('h1', class_='sc-d4d577d5-16 geJsxE').text
                row[0] = name
                row[2] = image
                with open('result.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow(row)
                print(f'Writed {name}')
            except Exception as e:
                print(row[1])
                print(e)
                telegram = get_notifier('telegram')
                telegram.notify(token=TOKEN, chat_id=CHAT_ID, message='Something happened')
                raise Exception('Something happened')
