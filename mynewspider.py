"""
从新型冠状病毒肺炎疫情分布网站(https://2019ncov.chinacdc.cn/2019-nCoV/)
爬取疫情数据，数据分为国际和国内两种类型，在运行命令时分别以--world和--domestic区分
"""


import requests
import json
import os
import io
import csv
import datetime
import argparse
import sys

from tqdm import tqdm

"""
确保日期格式符合形如20220101的格式
"""
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y%m%d')
    except ValueError:
        return False
    return True

def download_as_bytes_with_progress(url: str, missing: list) -> bytes:

    try:
        resp = requests.get(url, stream=True)
        resp.raise_for_status()
    except Exception as e:
        print(e)
        print(f"{url} is not Downloaded")
        missing.append(url)
        return None
    else:
        total = int(resp.headers.get('content-length', 0))
        bio = io.BytesIO()
        with tqdm(
            desc=url,
            total=total,
            unit='b',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in resp.iter_content(chunk_size=65536):
                bar.update(len(chunk))
                bio.write(chunk)
        return bio.getvalue()

def save_data(dst: str, name: str, header: list, features: list):
    with open(os.path.join(dst, name + '.csv'), encoding='UTF-8', mode='w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        for feature in features:
            properties = feature['properties']
            f_csv.writerow(list(properties.values()))

def download(dst: str, start: int, end: int, world: bool, domestic: bool):
    missing = []
    print("#########"
        " Fetch data from https://2019ncov.chinacdc.cn/2019-nCoV/ "
        "##########")
    if not os.path.exists(dst):
        os.makedirs(dst)
    url = ""
    for day in range(start, end+1):
        if not validate(str(day)):
            continue
        print(f"Downloading date of Date {day}...")
        if world:
            url = 'https://2019ncov.chinacdc.cn/JKZX/gb_yq_'+ str(day) + '.json'
        elif domestic:
            url = 'https://2019ncov.chinacdc.cn/JKZX/yq_'+ str(day) + '.json'
        
        rawContent = download_as_bytes_with_progress(url, missing)
        if not rawContent:
            continue
        jsonContent = json.loads(str(rawContent, encoding='utf-8'))
        features = jsonContent['features']
        header = list(features[0]['properties'].keys())
        save_data(dst, str(day), header, features)

    print("Done.")
    print(f"Data in url list {missing} is missing due to some problems")



if __name__ == "__main__":
    today = int(datetime.datetime.today().strftime("%Y%m%d"))
    default_start_date = 20200101
    p = argparse.ArgumentParser()
    p.add_argument("--dst", type=str, default="", help=".csv 文件存放的文件夹")
    p.add_argument("--start", type=int, default=default_start_date, help="选择开始下载的日期")
    p.add_argument("--end", type=int, default=today, help="选择结束下载的日期")
    p.add_argument("--world", action="store_true", default="", help="下载全球疫情数据")
    p.add_argument("--domestic", action="store_true", default="", help="下载中国的疫情数据")
    args = p.parse_args()
    download(args.dst, args.start, args.end, args.world, args.domestic)
