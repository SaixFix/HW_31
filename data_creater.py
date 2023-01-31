import csv
import json


class Data:
    @staticmethod
    def ads_csv_to_json() -> json:
        with open('./datasets/ads.csv', newline='') as file:
            reader = csv.DictReader(file)

            data_dict = []

            for row in reader:
                data_dict.append(row)

            return json.dumps(data_dict, ensure_ascii=False)
