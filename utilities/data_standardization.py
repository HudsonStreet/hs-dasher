from os import path
import sys
import csv
from datetime import datetime
sys.path.append(path.abspath('../../hs-vix-calculator'))

from utilities.tradeDateValidator import is_holiday, is_tradeday

cleaned_data_form = {}

def data_clean():
    with open('../vix_w_datetime.csv', 'r') as vix_data:
        data_cleaner = csv.reader(vix_data)

        for item in data_cleaner:
            current_date_time = datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S')
            current_date = current_date_time.strftime('%Y-%m-%d')
            current_time = current_date_time.strftime('%H:%M:%S')
            
            if(is_tradeday(current_date) and item[1] != '[nan]'):
                cleaned_data_form[item[0]] = item[1]
                #print('Date: {date} value: {value}'.format(date = item[0], value = item[1]))


def write_back_to_file():
    with open('../cleaned_vix_w_datetime.csv', 'w') as cleaned_vix_data:
        for key in cleaned_data_form.keys():
            cleaned_vix_data.write("%s,%s\n"%(key, cleaned_data_form[key]))


if __name__ == '__main__':
    data_clean()
    write_back_to_file()