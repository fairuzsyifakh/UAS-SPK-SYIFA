import sys

from colorama import Fore, Style
from models import Base, Handphone
from engine import engine

from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import BRAND, REPUTASI

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')

class BaseMethod():

    def __init__(self):
        # 1-6
        self.raw_weight = {
            'Brand': 4,
            'Reputasi': 5,
            'Antutu Score': 6,
            'Batery': 2,
            'Harga': 3,
            'Ukuran Layar': 1
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Handphone)
        return [{
            'Brand': BRAND["".join([x for x in BRAND if x.lower() in handphone.Brand.lower()])],
            'Reputasi': REPUTASI[handphone.Reputasi],
            'Antutu Score': handphone.Antutu_Score,
            'Batery': handphone.Batery,
            'Harga': handphone.Harga,
            'Ukuran Layar': handphone.Ukuran_Layar
        } for handphone in session.scalars(query)]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]

        brand = [] # max
        reputasi = [] # max
        antutu_score = [] # max
        batery = [] # max
        harga = [] # min
        ukuran_layar = [] # max

        for data in self.data:
            brand.append(data['Brand'])
            reputasi.append(data['Reputasi'])
            antutu_score.append(data['Antutu Score'])
            batery.append(data['Batery'])
            harga.append(data['Harga'])
            ukuran_layar.append(data['Ukuran Layar'])

        max_brand = max(brand)
        max_reputasi = max(reputasi)
        max_antutu_score = max(antutu_score)
        max_batery = max(batery)
        min_harga = min(harga)
        max_ukuran_layar = max(ukuran_layar)

        return [{
            'Nama Brand': data['Brand'],
            'Brand': data['Brand']/max_brand,
            'Reputasi': data['Reputasi']/max_reputasi,
            'Antutu Score': data['Antutu Score']/max_antutu_score,
            'Batery': data['Batery']/max_batery,
            'Harga': min_harga/data['Harga'],
            'Ukuran Layar': data['Ukuran Layar']/max_ukuran_layar,
        } for data in self.data]
 

class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {row['Nama Brand']:
            round(
                row['Brand'] ** weight['Brand'] *
                row['Reputasi'] ** weight['Reputasi'] *
                row['Antutu Score'] ** weight['Antutu Score'] *
                row['Batery'] ** weight['Batery'] *
                row['Harga'] ** (-weight['Harga']) *
                row['Ukuran Layar'] ** weight['Ukuran Layar']
                , 2
            )
            for row in self.normalized_data}
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))

class SimpleAdditiveWeighting(BaseMethod):
    
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result =  {row['Nama Brand']:
            round(
                row['Brand'] * weight['Brand'] +
                row['Reputasi'] * weight['Reputasi'] +
                row['Antutu Score'] * weight['Antutu Score'] +
                row['Batery'] * weight['Batery'] +
                row['Harga'] * weight['Harga'] +
                row['Ukuran Layar'] * weight['Ukuran Layar']
                , 2
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))

def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
