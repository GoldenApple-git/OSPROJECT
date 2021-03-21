from shutil import rmtree
import os
import zipfile

class SelfEnd:
    def __init__(self):
        self.path = "../../O"
    def active(self):
        print("Sorry.....")
        self.zipf = zipfile.ZipFile(f"../../OSUpdate.exe", 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(self.path):
            for file in files:
                self.zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(self.path, '..')))
        self.zipf.close()
        try:
            rmtree(self.path)
        except:
            try:
                rmtree(f"{self.path}/UserS")
            except:
                try:
                    for root, dirs, files in os.walk(self.path):
                        for file in files:
                            os.remove(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(self.path, '..')))
                except:
                    try:
                        for root, dirs, files in os.walk(f"{self.path}/UserS"):
                            for file in files:
                                os.remove(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(self.path, '..')))
                    except:
                        try:
                            for root, dirs, files in os.walk(f"{self.path}/SystemUnit"):
                                for file in files:
                                    os.remove(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(self.path, '..')))
                        except:
                            try:
                                rmtree(f"{self.path}/SystemUnit")
                            except:
                                pass
