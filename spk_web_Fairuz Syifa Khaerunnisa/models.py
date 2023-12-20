import numpy as np
import pandas as pd
from spk_model import WeightedProduct

class Handphone():

    def __init__(self) -> None:
        self.handphone = pd.read_csv('database/SPK_Fairuz Syifa Khaerunnisa.csv')

    #     self.handphone_array = np.array(self.handphone)

    # @property
    # def handphone_data(self):
    #     data = []
    #     for handphone in self.handphone_array:
    #         data.append({'id': handphone[0], 'nama': handphone[1]})
    #     return data

    # @property
    # def handphone_data_dict(self):
    #     data = {}
    #     for handphone in self.handphone_array:
    #         data[handphone[0]] = handphone[1] 
    #     return data

    def get_recs(self, kriteria):
        wp = WeightedProduct(self.handphone.to_dict(orient="records"), kriteria)
        return wp.calculate

