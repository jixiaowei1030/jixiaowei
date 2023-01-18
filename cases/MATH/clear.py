import os
import shutil


for path,dirs,files in os.walk(os.path.join(os.path.abspath(__file__).split('xmkp-api-test')[0],'xmkp-api-test'),topdown=False):
    for file in files:
        if file and '.pyc' in file:
            print(file)
            os.remove(os.path.join(path,file))
    for d in dirs:
        if d and '__pycache__' in d:
            print(d)
            shutil.rmtree(os.path.join(path,d))