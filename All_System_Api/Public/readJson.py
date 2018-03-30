#coding:utf-8
import json
import os
import shutil
from BaseRequest.BasePath import conf_path
def write_json(jsonFileName,data):
    with open(os.path.join(conf_path,jsonFileName), 'w') as json_file:
        json_file.write(json.dumps(data))

def read_json(jsonFileName):
    with open(os.path.join(conf_path,jsonFileName),'r') as json_file:
        data = json.load(json_file)
        return data


def removeAll(rootDir):
    fileList=os.listdir(rootDir)
    for f in fileList:
        filepath = os.path.join( rootDir, f )
        if os.path.isfile(filepath):
            os.remove(filepath)
            print (filepath+" removed!")
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)
            print ("dir "+filepath+" removed!")

if __name__=="__main__":
    print read_json('purchase_sales_management.json')
