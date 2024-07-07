import csv
import time

import requests
from bs4 import BeautifulSoup
import json
from notifiers import get_notifier

TOKEN = '7323608342:AAE4wNHiFs9tQMFgqutKkaJmhCeM2LzL3mQ'
CHAT_ID = '324015551'

username = "zabutniy20"
password = "XHt7nTwPHW"
PROXY_DNS = "139.171.75.217:50100"
proxy = {"https": "http://{}:{}@{}".format(username, password, PROXY_DNS)}

cookies = {
    'visitor_id': '92d09a18-6a60-4e95-a6fa-4e2ac09e08d0',
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
    '_tt_enable_cookie': '1',
    '_ttp': '_ECYOCRSzf90jHdmx-WxyQ3XU2p',
    'nloc': 'en-sa',
    'review_lang': 'xx',
    '_clck': 'n7patw%7C2%7Cfn7%7C0%7C1646',
    '__gads': 'ID=c5a2fe204a1a2e3a:T=1720105174:RT=1720190134:S=ALNI_MaT5UZGhtveXpxuohdPalFibT1LlQ',
    '__gpi': 'UID=00000a39e306d2fb:T=1720105174:RT=1720190134:S=ALNI_MbZMcqtdKjYVHOPf1MHn82PRrCvUg',
    '__eoi': 'ID=77beaff7f7f3ea38:T=1720105174:RT=1720190134:S=AA-AfjaTeVL0CZ-czxn87eLjZl4H',
    '_clsk': 'x9gb7h%7C1720190686942%7C1%7C0%7Co.clarity.ms%2Fcollect',
    'AKA_A2': 'A',
    'bm_mi': 'F09E910AAD4D22CF38FD82CBDD18BB9A~YAAQrDxRaGiHX3CQAQAAM5JugxgUEAN6nyqXZvAeZ5FoU9PTrOs/ZzdzqDGL584ewY+3yH7ZXGxaGCswuU7qwPzLggkiFbJ4Niibz/Kfmk5sbr3TaaNppZDjf+yh1JJAQUQpPu5gxDoAzi/ADmbhaOqx1D6FRzHylKcCwaKERG/8//7xqSH3OHrAmHwJ9fdhvbCsPNYtWl2Zgzfn4bszVjP9s2x1HlwScYp+dAft6HvXPAMYnwOIBjIwkxe643XFo/cvXkmnkOmXXnijBnh2CIgoRVZxI4ddIh63m1hRRYWjii/7AJUAA7hG3SqQn+V32ylSwGIz5ZCyfs/QqZrjgTk1UkV3D6xV~1',
    'ak_bmsc': '20288C50BA1FCFC1BDC197C4195CE1F9~000000000000000000000000000000~YAAQrDxRaKuHX3CQAQAAk5lugxjLmP0yFp2ybIFd+1kOeXeNyCwF/FZCUBjyLG5y6wDY60xoyqiRpNbmRH6ENFDfAKV9GlpcHI6XSS/Yi0GB78/JNdL/xHzIjMsFSEJ9eL6qSJy+r1AI8jkC9dnzVW3NcuPkU2gLNetsRLqmwYQbkjCor5uvS63+AUhiDakEzg4z6ZU32ICoytVy8w8+oOV1qUwBNHCqaVV/FZLfHzmYOKbq4HHoB+zWGISgwbGGwKpMOw17QZ3d9ZrfMmwb5QjICI3b42wTLJJkwe7rr54lyVNjJGgqzKzAj6sdeCJcDLbUtb4O9JnDo7e+tPpTMAVGJEPBmLF63rYqhHk+18XiCojftBlAo/v9nwjpNDrJFRJmsWC79MLkevgIitTN4nUzjL/fW17wEm+4+eCT8yNj+skZ8FWBwquEOfAWb8U5e0ezKCMWptzGPzpDjTlwzFMdx/kWkqlBTyyxOuYYT1UaqZwRdNdheZyzmXo=',
    'x-whoami-headers': 'eyJ4LWxhdCI6IjI0NzMxMTM4MiIsIngtbG5nIjoiNDY2NzAwODE0IiwieC1hYnkiOiJ7XCJwZHBfYm9zLmVuYWJsZWRcIjoxLFwib3RwX2xvZ2luLmVuYWJsZWRcIjoxLFwicGRwX2ZseW91dC5mbHlvdXRfdmFsdWVcIjowfSIsIngtZWNvbS16b25lY29kZSI6IlNBLVJVSC1TMTciLCJ4LWFiLXRlc3QiOls3MzEsODMwLDg1MV0sIngtcm9ja2V0LXpvbmVjb2RlIjoiVzAwMDgzNDk2QSIsIngtcm9ja2V0LWVuYWJsZWQiOnRydWUsIngtYm9yZGVyLWVuYWJsZWQiOnRydWV9',
    '_etc': 'U2mcSciuxu4fp6HH',
    'nguestv2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiIwNjgxMDM3YzI0NjY0YjNhYmI2YjZiZGNlN2FiM2NlNSIsImlhdCI6MTcyMDE5NDY3MCwiZXhwIjoxNzIwMTk0OTcwfQ.lms5ErMGWGW_NHiqPEkVPkGOQ8xxXgwIeWRarH5EyhM',
    '_gat_UA-84507530-14': '1',
    'bm_sv': 'C9683C1E1850CABEB10E901D58EDBE3A~YAAQciTDF9XCEGKQAQAAQ6WXgxiQnCGV74x5/K7cZTX21h+Oejoe7rL/uAMnKCwV9FN63QLx+j5cyj2xFPXZa9XfZHm+qyh2AJohrm1co+BUaj69p7Gzvzf9ZUsHFoUM/KqZre3ikUqUTaJFO9I4lw3d4hUcFwS9C+lMLetTqkWAGHz8h2IbSpp4D68PB9lzCqEcviVZ2XbjSUj75ZtpuNDnRGDbvbjJRKrQ2nsWOuXg9gtonL+Uu1nA0ULuw5U=~1',
    '_uetsid': '031865b03a1611ef958847ddf30170a1',
    '_uetvid': '031894203a1611efa723cb0481da0994',
    '_scid_r': '015b19a8-19f1-4bd3-a6bc-b28015e53033',
    'RT': '"z=1&dm=noon.com&si=70c2df7c-a902-400a-bedd-aa3f78198390&ss=ly8u0s7y&sl=6&tt=0&obo=6&rl=1&ld=1h5qu&r=0b80765a52c30c14d62497fb51695d99&ul=1h5qv"',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk-UA;q=0.7,uk;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'visitor_id=92d09a18-6a60-4e95-a6fa-4e2ac09e08d0; _gcl_au=1.1.884992829.1720105130; _ga=GA1.2.1820979055.1720105168; _gid=GA1.2.1305513592.1720105168; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22ESOHCAM3IgNst0UQFbC3%22%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%7D; _ym_uid=1720105170311697895; _ym_d=1720105170; _scid=015b19a8-19f1-4bd3-a6bc-b28015e53033; _ScCbts=%5B%5D; _fbp=fb.1.1720105173069.46575517599655031; _sctr=1%7C1720040400000; _tt_enable_cookie=1; _ttp=_ECYOCRSzf90jHdmx-WxyQ3XU2p; nloc=en-sa; review_lang=xx; _clck=n7patw%7C2%7Cfn7%7C0%7C1646; __gads=ID=c5a2fe204a1a2e3a:T=1720105174:RT=1720190134:S=ALNI_MaT5UZGhtveXpxuohdPalFibT1LlQ; __gpi=UID=00000a39e306d2fb:T=1720105174:RT=1720190134:S=ALNI_MbZMcqtdKjYVHOPf1MHn82PRrCvUg; __eoi=ID=77beaff7f7f3ea38:T=1720105174:RT=1720190134:S=AA-AfjaTeVL0CZ-czxn87eLjZl4H; _clsk=x9gb7h%7C1720190686942%7C1%7C0%7Co.clarity.ms%2Fcollect; AKA_A2=A; bm_mi=F09E910AAD4D22CF38FD82CBDD18BB9A~YAAQrDxRaGiHX3CQAQAAM5JugxgUEAN6nyqXZvAeZ5FoU9PTrOs/ZzdzqDGL584ewY+3yH7ZXGxaGCswuU7qwPzLggkiFbJ4Niibz/Kfmk5sbr3TaaNppZDjf+yh1JJAQUQpPu5gxDoAzi/ADmbhaOqx1D6FRzHylKcCwaKERG/8//7xqSH3OHrAmHwJ9fdhvbCsPNYtWl2Zgzfn4bszVjP9s2x1HlwScYp+dAft6HvXPAMYnwOIBjIwkxe643XFo/cvXkmnkOmXXnijBnh2CIgoRVZxI4ddIh63m1hRRYWjii/7AJUAA7hG3SqQn+V32ylSwGIz5ZCyfs/QqZrjgTk1UkV3D6xV~1; ak_bmsc=20288C50BA1FCFC1BDC197C4195CE1F9~000000000000000000000000000000~YAAQrDxRaKuHX3CQAQAAk5lugxjLmP0yFp2ybIFd+1kOeXeNyCwF/FZCUBjyLG5y6wDY60xoyqiRpNbmRH6ENFDfAKV9GlpcHI6XSS/Yi0GB78/JNdL/xHzIjMsFSEJ9eL6qSJy+r1AI8jkC9dnzVW3NcuPkU2gLNetsRLqmwYQbkjCor5uvS63+AUhiDakEzg4z6ZU32ICoytVy8w8+oOV1qUwBNHCqaVV/FZLfHzmYOKbq4HHoB+zWGISgwbGGwKpMOw17QZ3d9ZrfMmwb5QjICI3b42wTLJJkwe7rr54lyVNjJGgqzKzAj6sdeCJcDLbUtb4O9JnDo7e+tPpTMAVGJEPBmLF63rYqhHk+18XiCojftBlAo/v9nwjpNDrJFRJmsWC79MLkevgIitTN4nUzjL/fW17wEm+4+eCT8yNj+skZ8FWBwquEOfAWb8U5e0ezKCMWptzGPzpDjTlwzFMdx/kWkqlBTyyxOuYYT1UaqZwRdNdheZyzmXo=; x-whoami-headers=eyJ4LWxhdCI6IjI0NzMxMTM4MiIsIngtbG5nIjoiNDY2NzAwODE0IiwieC1hYnkiOiJ7XCJwZHBfYm9zLmVuYWJsZWRcIjoxLFwib3RwX2xvZ2luLmVuYWJsZWRcIjoxLFwicGRwX2ZseW91dC5mbHlvdXRfdmFsdWVcIjowfSIsIngtZWNvbS16b25lY29kZSI6IlNBLVJVSC1TMTciLCJ4LWFiLXRlc3QiOls3MzEsODMwLDg1MV0sIngtcm9ja2V0LXpvbmVjb2RlIjoiVzAwMDgzNDk2QSIsIngtcm9ja2V0LWVuYWJsZWQiOnRydWUsIngtYm9yZGVyLWVuYWJsZWQiOnRydWV9; _etc=U2mcSciuxu4fp6HH; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiIwNjgxMDM3YzI0NjY0YjNhYmI2YjZiZGNlN2FiM2NlNSIsImlhdCI6MTcyMDE5NDY3MCwiZXhwIjoxNzIwMTk0OTcwfQ.lms5ErMGWGW_NHiqPEkVPkGOQ8xxXgwIeWRarH5EyhM; _gat_UA-84507530-14=1; bm_sv=C9683C1E1850CABEB10E901D58EDBE3A~YAAQciTDF9XCEGKQAQAAQ6WXgxiQnCGV74x5/K7cZTX21h+Oejoe7rL/uAMnKCwV9FN63QLx+j5cyj2xFPXZa9XfZHm+qyh2AJohrm1co+BUaj69p7Gzvzf9ZUsHFoUM/KqZre3ikUqUTaJFO9I4lw3d4hUcFwS9C+lMLetTqkWAGHz8h2IbSpp4D68PB9lzCqEcviVZ2XbjSUj75ZtpuNDnRGDbvbjJRKrQ2nsWOuXg9gtonL+Uu1nA0ULuw5U=~1; _uetsid=031865b03a1611ef958847ddf30170a1; _uetvid=031894203a1611efa723cb0481da0994; _scid_r=015b19a8-19f1-4bd3-a6bc-b28015e53033; RT="z=1&dm=noon.com&si=70c2df7c-a902-400a-bedd-aa3f78198390&ss=ly8u0s7y&sl=6&tt=0&obo=6&rl=1&ld=1h5qu&r=0b80765a52c30c14d62497fb51695d99&ul=1h5qv"',
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

counter = 13607

with open('noon_v5.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    for row in data[13608:]:
        counter += 1
        print(counter)
        print('******')
        print(f'Start work with {row[0]}')
        time.sleep(2)
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
                try:
                    first_name = soup.find('div', class_='sc-d4d577d5-15 jfOgKH').text + ' '
                except:
                    time.sleep(5)
                    try:
                        first_name = soup.find('div', class_='sc-35f61ce6-4 xhoDA').text + ' '
                    except:
                        time.sleep(5)
                        try:
                            first_name = soup.find('div', class_='sc-35f61ce6-4 xhoDA').text + ' '
                        except:
                            telegram = get_notifier('telegram')
                            telegram.notify(token=TOKEN, chat_id=CHAT_ID, message='Something happened')
                            raise Exception('Something happened')
                name = first_name + soup.find('h1', class_='sc-d4d577d5-16 geJsxE').text
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
        else:
            print(row[1])
            print(f'Failed {result.status_code}')
            telegram = get_notifier('telegram')
            telegram.notify(token=TOKEN, chat_id=CHAT_ID, message='Something happened')
            raise Exception

