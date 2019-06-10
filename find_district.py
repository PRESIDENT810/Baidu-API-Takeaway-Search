import requests
import time
import os
import pandas as pd

def find_district(place):
    print("place: ",place)
    address = grim(place)
    print("address: ",address)
    url = "http://api.map.baidu.com/place/v2/search?query={}&region=杭州&output=xml&ak=Foh9cBPtgXT0s33nzjOoqTIxhHTKrA6C".format(address)
    print("url: ",url)
    try:
        response = requests.get(url)
        html = response.text
        print("html",html)
        address = html.split("<address>")[1].split("</address>")[0]
        print("address: ",address,'\n')
        district_idx = address.find("区")
        if district_idx != len(address):
            district = address[district_idx-2:district_idx+1]
        else:
            district = address[district_idx - 2:]
        if district == '':
            district = "no result"
        return district
    except:
        return "no result"

def grim(place):
    end = place.find("(")
    if end != -1:
        place = place[:end + 1]

    end = place.find("（")
    if end != -1:
        place = place[:end+1]
    return place


def write_district(result):
    fhand = open('district list_3.txt','a')
    fhand.write(result+'\n')
    fhand.close()

def main():
    df = pd.read_excel("Book3.xlsx",iterator=True)
    row = 0
    for word in list(df.iloc[:, 2]):
        district = find_district(word)
        write_district(district)
        time.sleep(0.0205)
        # df.iloc[row:, 3] = district
        # row += 1
    df.to_excel("district_results_3.xlsx", index=False)

if __name__=='__main__':
    main()