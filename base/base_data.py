import os

import yaml


def base_data(filename,key):
    with open("..%sdata%s%s" % (os.sep,os.sep,filename)) as f:
        case_data = yaml.load(f,Loader=yaml.FullLoader)[key]
        data_list = list()
        for i in case_data.values():
            data_list.append(i)
        return data_list

print(base_data("data.yaml","test_contact"))