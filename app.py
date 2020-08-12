# -*- encoding: utf-8 -*-
from flask import Flask
# from config import DevConfig
from datetime import datetime
import random
import time
from core.crawler import Crawler
from openpyxl import Workbook
from core.browsers import SLEEP_SECOND


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
                "labels": ["Revenue (2020), mln USD", "yoy", "ARPC, $", "CAGR"],
                'fields': ["revenue", "revenue_yoy", "arpc", "cagr"]
            },
            {
                "title": "Digital Market Links",
                "r_type": "251",
                "i_type": "consumer-electronics",
                "labels": ["Revenue (2020), mln USD", "yoy", "Users, mln", "Users yoy", "CAGR", "Users Penetration %",
                           "ARPU"],
                'fields': ["revenue", "revenue_yoy", "users", "users_yoy", "cagr", "user_penetration", "arpu"]
            },
            {
                "title": "Mobile",
                "r_type": "15020100",
                "i_type": "mobile-phones",
                "labels": ["Revenue", "%", "ARPC, $", "CAGR"],
                'fields': ["revenue", "revenue_yoy", "arpc", "cagr"]
            },
            {
                "title": "Laptop & Tablets",
                "r_type": "15030100",
                "i_type": "laptops-tablets",
                "labels": ["Revenue", "%", "ARPC, $", "CAGR"],
                'fields': ["revenue", "revenue_yoy", "arpc", "cagr"]
            }
        ],
        "Vitamin & Personal Care": [
            {
                "title": "Vitamin & Minerals",
                "r_type": "18050000",
                "i_type": "vitamins-minerals",
                "labels": ["Revenue (2020), mln USD", "Revenue yoy", "ARPC", "CAGR"],
                'fields': ["revenue", "revenue_yoy", "arpc", "cagr"]
            },
            {
                "title": "Personal Care",
                "r_type": "254",
                "i_type": "personal-care",
                "labels": ["Revenue (2020), mln USD", "Revenue yoy", "Users, mln", "Users yoy", "CAGR",
                           "Users Penetration %", "ARPU"],
                'fields': ["revenue", "revenue_yoy", "users", "users_yoy", "cagr", "user_penetration", "arpu"]
            }
        ]
    }

    sheet_index = -1
    wb = Workbook()
    for tab_title in tab.keys():
        print(tab_title)
        # create sheet
        sheet_index += 1
        ws = wb.create_sheet(tab_title, sheet_index)
        # ws.cell(row=4, column=2, value=10)
        # ws.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
        cols_index = 1
        for data_group_id in range(len(tab[tab_title])):
            data_group = tab[tab_title][data_group_id]
            row_id = 1

            # print('\t{}\t{}\t{}\t{}'.format(data_group['title'], data_group['r_type'], data_group['i_type'],
            #                                 data_group['fields']))

            if data_group_id == 0:
                cols = ["Area", "Subregion", "Country"] + [data_group['title']] + data_group['labels']
                col_start = 1
            else:
                cols = [data_group['title']] + data_group['labels']

            for c in range(len(cols)):
                _ = ws.cell(row=row_id, column=col_start+c, value="{}".format(cols[c]))

            for area in areas:
                row_id += 1
                url = "https://www.statista.com/outlook/{}/{}/{}/{}".format(data_group['r_type'],
                                                                            area[3],
                                                                            data_group['i_type'],
                                                                            area[4])

                # _ = ws.cell(row=row_id, column=cols_count, value="{}".format(cols[c]))
                # print("\t\t{}".format(url))
                crawler = Crawler(url)
                d = crawler.data()
                if data_group_id == 0:
                    row_data = [area[0], area[1], area[2], url]
                else:
                    row_data = [url]

                for f in data_group['fields']:
                    row_data.append(d[f])
                    # c = "{}\t{}-{}".format(c, f, d[f])

                for c in range(len(row_data)):
                    _ = ws.cell(row=row_id, column=col_start+c, value="{}".format(row_data[c]))

                print(row_data)

                sl = random.choice(SLEEP_SECOND)
                print("*************** sleep {} second ***************".format(sl))
                # if row_id >= 5:
                #     break

                time.sleep(sl)
            col_start += len(cols)

    wb.save(filename="/tmp/statista.xlsx")


if __name__ == "__main__":
    # app.run(threaded=True)
    run_crawler()
