import requests
from bs4 import BeautifulSoup
from exception import exception


def extraction_data():
    try:
        content = requests.get("https://www.boj.or.jp/")
    except exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")

        result = soup.find("span",{"class": "tit market01"})
        name = result.text

        result = soup.find("span",{"class": "value"})
        angka = result.find("span", {"class":"monetary_base2"}).text
        value = angka


        result = dict()
        result["name"] = name
        result["value"] = value

        print(angka)
        return result


def show_data(result):
    if result is None:
        print("Warning Missing Data")
        return
    print("The Bank Market Operation")
    print(f'{result["name"]}')
    print(f'{result["value"]}')
    #print(f'Valvue Monetary base { valvuemonetarybase["valvuemonetarybase"]})

if __name__ == "__main__":
    extraction_data()
