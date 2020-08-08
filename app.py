# -*- encoding: utf-8 -*-
from flask import Flask
# from config import DevConfig
from datetime import datetime
import random
import time

from core.crawler import Crawler

app = Flask(__name__)
# app.config.from_object(DevConfig)


@app.route("/")
def home():
    return "Hello Flask {}".format(random.randint(1000, 999999))


@app.route("/test/")
def test():
    return "test 789 - {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def run_crawler():
    areas = [
        ["Africa", "Africa", "Nigeria", "160", "nigeria"],
        ["Africa", "Africa", "South Africa 南非", "112", "south-africa"],
        ["Africa", "Africa", "Morocco", "159", "morocco"],
        ["Africa", "Africa", "Kenya", "247", "kenya"],
        ["Asia", "East Asia", "China 中國", "117", "china"],
        ["Asia", "East Asia", "Japan 日本", "121", "japan"],
        ["Asia", "East Asia", "South Korea", "125", "south-korea"],
        ["Asia", "East Asia", "Hong Kong 香港", "118", "hong-kong"],
        ["Asia", "SEA", "Indonesia 印尼", "120", "indonesia"],
        ["Asia", "SEA", "Thailand 泰國", "126", "thailand"],
        ["Asia", "SEA", "Vietnam 越南", "127", "vietnam"],
        ["Asia", "South Asia", "India 印度", "119", "india"],
        ["Asia", "South Asia", "Pakistan 巴基斯坦", "294", "pakistan"],
        ["Asia", "West Asia", "Saudi Arabia 沙烏地阿拉伯", "110", "saudi-arabia"],
        ["Australia & Oceania", "Australia & Oceania", "Australia 澳洲", "107", "australia"],
        ["Australia & Oceania", "Australia & Oceania", "New Zealand", "161", "new-zealand"],
        ["Europe", "Central & West Europe", "Germany 德國", "137", "germany"],
        ["Europe", "Central & West Europe", "UK 英國", "156", "united-kingdom"],
        ["Europe", "Central & West Europe", "France 法國", "136", "france"],
        ["Europe", "Central & West Europe", "Poland 波蘭", "146", "poland"],
        ["Europe", "Central & West Europe", "Netherlands 荷蘭", "144", "netherlands"],
        ["Europe", "Central & West Europe", "Switzerland 瑞士", "155", "switzerland"],
        ["Europe", "Central & West Europe", "Belgium 比利時", "129", "belgium"],
        ["Europe", "Central & West Europe", "Austria 奧地利", "128", "austria"],
        ["Europe", "Central & West Europe", "Czechia", "132", "czechia"],
        ["Europe", "Central & West Europe", "Ireland", "140", "ireland"],
        ["Europe", "Eastern Europe", "Russia 俄羅斯", "149", "russia"],
        ["Europe", "Northern Europe", "Sweden 瑞典", "154", "sweden"],
        ["Europe", "Northern Europe", "Norway", "145", "norway"],
        ["Europe", "Northern Europe", "Denmark", "133", "denmark"],
        ["Europe", "Northern Europe", "Finland", "135", "finland"],
        ["Europe", "Southern Europe", "Italy 義大利", "141", "italy"],
        ["Europe", "Southern Europe", "Spain 西班牙", "153", "spain"],
        ["Europe", "Southern Europe", "Turkey 土耳其", "113", "turkey"],
        ["Europe", "Southern Europe", "Portugal", "147", "portugal"],
        ["Europe", "Southern Europe", "Greece 希臘", "138", "greece"],
        ["North America", "North America", "USA 美國", "109", "united-states"],
        ["North America", "North America", "Mexico 墨西哥", "116", "mexico"],
        ["North America", "North America", "Canada 加拿大", "108", "canada"],
        ["South America", "South America", "Brazil 巴西", "115", "brazil"],
        ["South America", "South America", "Argentina 阿根廷", "114", "argentina"],
        ["South America", "South America", "Colombia 哥倫比亞", "158", "colombia"],
        ["South America", "South America", "Chile", "157", "chile"],
        ["Worldwide", "Worldwide", "", "100", "worldwide"]
    ]
    tab = {
        "3C": [
            {
                "title": "Consumer Market Links",
                "r_type": "15000000",
                "i_type": "consumer-electronics",
                'fields': ["revenue", "revenue_yoy", "arpc", "cagr"]
            },
            {
                "title": "Digital Market Links",
                "r_type": "251",
                "i_type": "consumer-electronics",
                'fields': ["revenue", "revenue_yoy", "users", "users_yoy", "cagr", "user_penetration", "arpu"]
            },
            {
                "title": "Mobile",
                "r_type": "15020100",
                "i_type": "mobile-phones",
                'fields': ["revenue", "revenue_yoy", "arpc", "cagr"]
            },
            {
                "title": "Laptop & Tablets",
                "r_type": "15030100",
                "i_type": "laptops-tablets",
                'fields': ["revenue", "revenue_yoy", "arpc", "cagr"]
            }
        ],
        "Vitamin & Personal Care": [
            {
                "title": "Vitamin & Minerals",
                "r_type": "18050000",
                "i_type": "vitamins-minerals",
                'fields': ["revenue", "revenue_yoy", "arpc", "cagr"]
            },
            {
                "title": "Personal Care",
                "r_type": "254",
                "i_type": "personal-care",
                'fields': ["revenue", "revenue_yoy", "users", "users_yoy", "cagr", "user_penetration", "arpu"]
            }
        ]
    }

    for tab_title in tab.keys():
        print(tab_title)
        for data_group in tab[tab_title]:
            print('\t{}\t{}\t{}\t{}'.format(data_group['title'], data_group['r_type'], data_group['i_type'], data_group['fields']))
            i = 0
            for area in areas:
                if i > 2:
                    break
                i += 1
                url = "https://www.statista.com/outlook/{}/{}/{}/{}".format(data_group['r_type'],
                                                                            area[3],
                                                                            data_group['i_type'],
                                                                            area[4])
                print("\t\t{}".format(url))

                crawler = Crawler(url)
                d = crawler.data()
                c = ""
                for f in data_group['fields']:
                    c = "{}\t{}-{}".format(c, f, d[f])

                print("\t\t\t{}".format(c))
                print("*************** sleep 0.3 second ***************")
                time.sleep(0.3)


if __name__ == "__main__":
    # app.run(threaded=True)

    run_crawler()