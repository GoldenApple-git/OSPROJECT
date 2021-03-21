import os
import zipfile
import shutil

class Compile:
    def __init__(self,folder=""):
        self.path1 = f'..\\UserS'
        self.path = f'..\\UserS\\{folder}'
        print(self.path)
        print(self.path1)

    def compilefile(self,file):
        self.zipf = zipfile.ZipFile(f"../LocalData/Account/{file}.db", 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(self.path):
            for file in files:
                self.zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(self.path, '..')))
        self.zipf.close()
        shutil.rmtree(self.path)

    def decompilfile(self,file):
        self.zipf = zipfile.ZipFile(f'../LocalData/Account/{file}.db', 'r')
        self.zipf.extractall(self.path1)
