import shutil

import requests
from bs4 import BeautifulSoup


burp0_url = "https://almowafir.com:443/"
burp0_cookies = {"utm_source": "organic", "utm_medium": "organic", "utm_campaign": "www.google.com", "utm_term": "", "utm_content": "https://www.google.com/", "gclid": "", "refer_id": "", "google-analytics_v4_01d0__ga4": "5782816e-3489-4406-802c-0e291dfba1e6", "_fbp": "fb.1.1693841463771.842799036", "_gid": "GA1.2.699560117.1694130769", "alm_rum": "1", "wp_acf_slideup_banners_WhatsApp%20respond%20bubble_clickCnt": "2", "wp_acf_preheader_banners_App%20Android_cnt": "1", "wp_acf_slideup_banners_WhatsApp%20respond%20bubble_cnt": "11", "google-analytics_v4_01d0__ga4sid": "1189885675", "google-analytics_v4_01d0__session_counter": "13", "usedCodes": "%5B%22ALM1%22%2C%22ALMOWAFIR10%22%2C%22ALM10%22%2C%22ADF11%22%5D", "alm_returning": "{%22status%22:%22Returning%22%2C%22ts%22:1694204247722%2C%22vd%22:1}", "_ga": "GA1.2.434020244.1693841454", "_ga_3DP0VNV7LR": "GS1.1.1694201494.15.1.1694204253.0.0.0", "_ga_34B604LFFQ": "GS1.1.1694201494.15.1.1694204253.60.0.0", "site24x7rumID": "259837602196333.1694204247156.1694202186932", "google-analytics_v4_01d0__counter": "697", "google-analytics_v4_01d0__let": "1694204348065", "google-analytics_v4_01d0__engagementPaused": "1694204348065", "google-analytics_v4_01d0__engagementStart": "1694204333942"}
burp0_headers = {"Pragma": "no-cache", "Cache-Control": "no-cache", "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://almowafir.com/beauty-%d8%a7%d9%84%d8%ac%d9%85%d8%a7%d9%84-%d9%88%d8%a7%d9%84%d8%b9%d9%86%d8%a7%d9%8a%d8%a9/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,ar;q=0.8", "Connection": "close"}

r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
soap=BeautifulSoup(r.text)

stores=soap.select('div[class="store"] img')

print(stores)
for store in stores:
    burp0_cookies = {"utm_source": "organic", "utm_medium": "organic", "utm_campaign": "www.google.com", "utm_term": "",
                     "utm_content": "https://www.google.com/", "gclid": "", "refer_id": "",
                     "google-analytics_v4_01d0__ga4": "5782816e-3489-4406-802c-0e291dfba1e6",
                     "_fbp": "fb.1.1693841463771.842799036", "_gid": "GA1.2.699560117.1694130769", "alm_rum": "1",
                     "wp_acf_slideup_banners_WhatsApp%20respond%20bubble_clickCnt": "2",
                     "wp_acf_preheader_banners_App%20Android_cnt": "1",
                     "wp_acf_slideup_banners_WhatsApp%20respond%20bubble_cnt": "11",
                     "google-analytics_v4_01d0__ga4sid": "1189885675",
                     "google-analytics_v4_01d0__session_counter": "13",
                     "usedCodes": "%5B%22ALM1%22%2C%22ALMOWAFIR10%22%2C%22ALM10%22%2C%22ADF11%22%5D",
                     "alm_returning": "{%22status%22:%22Returning%22%2C%22ts%22:1694204247722%2C%22vd%22:1}",
                     "_ga": "GA1.2.434020244.1693841454", "_ga_3DP0VNV7LR": "GS1.1.1694201494.15.1.1694204253.0.0.0",
                     "_ga_34B604LFFQ": "GS1.1.1694201494.15.1.1694204253.60.0.0",
                     "site24x7rumID": "259837602196333.1694204247156.1694202186932",
                     "google-analytics_v4_01d0__counter": "697", "google-analytics_v4_01d0__let": "1694204348065",
                     "google-analytics_v4_01d0__engagementPaused": "1694204348065",
                     "google-analytics_v4_01d0__engagementStart": "1694204333942"}
    burp0_headers = {"Pragma": "no-cache", "Cache-Control": "no-cache",
                     "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
                     "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                     "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1",
                     "Sec-Fetch-Dest": "document",
                     "Referer": "https://almowafir.com/beauty-%d8%a7%d9%84%d8%ac%d9%85%d8%a7%d9%84-%d9%88%d8%a7%d9%84%d8%b9%d9%86%d8%a7%d9%8a%d8%a9/",
                     "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
                     "Connection": "close"}

    url=store.get('src')
    r=requests.get(url,headers=burp0_headers,cookies=burp0_cookies)
    print(url)
    name=url.split('/')[-1]
    print(r.text)
    if r.status_code == 200:
        with open(f'stores_images/{name}', 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
