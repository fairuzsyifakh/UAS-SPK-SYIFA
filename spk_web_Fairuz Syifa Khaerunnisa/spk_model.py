from settings import BRAND, REPUTASI

class BaseMethod():

    def __init__(self, data_dict, **atur_bobot):
        self.data_csv = data_dict

        # 1-6
        self.raw_weight = {
            'Brand': 4,
            'Reputasi': 5,
            'Antutu Score': 6,
            'Batery': 2,
            'Harga': 3,
            'Ukuran Layar': 1
        }

        if atur_bobot:
            for bobot in atur_bobot.items():
                backup1 = atur_bobot[bobot[0]]
                backup2 = {v: k for k, v in atur_bobot.items()}[bobot[1]]
                atur_bobot[bobot[0]] = bobot[1]
                atur_bobot[backup2] = backup1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'Nama Brand': handphone['Brand'],
            'Brand': BRAND["".join([brand for brand in BRAND if brand.lower() in handphone['Brand'].lower()])],
            'Reputasi': REPUTASI[handphone['Reputasi']],
            'Antutu Score': handphone['Antutu Score'],
            'Batery': handphone['Batery'],
            'Harga': handphone['Harga'],
            'Ukuran Layar': handphone['Ukuran Layar']
        } for handphone in self.data_csv]

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
            'Nama Brand': data['Nama Brand'],
            'Brand': data['Brand']/max_brand,
            'Reputasi': data['Reputasi']/max_reputasi,
            'Antutu Score': data['Antutu Score']/max_antutu_score,
            'Batery': data['Batery']/max_batery,
            'Harga': min_harga/data['Harga'],
            'Ukuran Layar': data['Ukuran Layar']/max_ukuran_layar
        } for data in self.data]
 
class WeightedProduct(BaseMethod):
    def __init__(self, data_csv, atur_bobot:dict):
        super().__init__(data_dict=data_csv, **atur_bobot)

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
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))
