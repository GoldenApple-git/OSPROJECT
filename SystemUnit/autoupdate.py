from urllib.request import Request, urlopen
import urllib.request
import re
import os
import json
import sys

class Update:
    def __init__(self):
        self.rawdata = open("./settingsdata.db", "r", newline="").read().split("#")
        for lines in self.rawdata:
            if "version" in tuple(lines.split(","))[0]:
                self.version = tuple(lines.split(","))[1]
                break
        self.version = urlopen(Request("https://raw.githubusercontent.com/GoldenApple-git/OSPROJECT/main/version.txt?token=AJNKA2RSCLOQRGBGV7AIKMDAK53MU")).read().decode()
        self.get = open("./settingsdata.db", "r", newline="").read().split("#")
        p=0
        for lines in self.get:
            if "version" in tuple(lines.split(","))[0]:
                datas = open("./settingsdata.db", "r", newline="").readlines()
                if datas[p][-2:] == "#\n":
                    datas[p] = f"version,{self.version}#\n"
                else:
                    datas[p] = f"version,{self.version}"
            p+=1
            open("./settingsdata.db", "w", newline="").writelines(datas)

    def check(self):
        if self.rawdata == self.version:
            return True
        else:
            return False

    def create_url(self,url):
        repo_only_url = re.compile(r"https:\/\/github\.com\/[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}\/[a-zA-Z0-9]+")
        re_branch = re.compile("/(tree|blob)/(.+?)/")

        branch = re_branch.search(url)
        download_dirs = url[branch.end():]
        api_url = (url[:branch.start()].replace("github.com", "api.github.com/repos", 1) +
                "/contents/" + download_dirs + "?ref=" + branch.group(2))

        return api_url, download_dirs

    def upgrade(self, url,output_dir):
            flatten = False
            api_url, download_dirs = self.create_url(url)

            if not flatten:
                if len(download_dirs.split(".")) == 0:
                    dir_out = os.path.join(output_dir, download_dirs)
                else:
                    dir_out = os.path.join(output_dir, "/".join(download_dirs.split("/")[:-1]))
            else:
                dir_out = output_dir

            try:
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)
                response = urllib.request.urlretrieve(api_url)
            except KeyboardInterrupt:
                # when CTRL+C is pressed during the execution of this script,
                # bring the cursor to the beginning, erase the current line, and dont make a new line
                sys.exit()

            if not flatten:
                # make a directory with the name which is taken from
                # the actual repo
                os.makedirs(dir_out, exist_ok=True)

            # total files count
            total_files = 0

            with open(response[0], "r") as f:
                data = json.load(f)
                # getting the total number of files so that we
                # can use it for the output information later
                total_files += len(data)

                # If the data is a file, download it as one.
                if isinstance(data, dict) and data["type"] == "file":
                    try:
                        # download the file
                        opener = urllib.request.build_opener()
                        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                        urllib.request.install_opener(opener)
                        urllib.request.urlretrieve(data["download_url"], os.path.join(dir_out, data["name"]))
                        # bring the cursor to the beginning, erase the current line, and dont make a new line
                        print("Downloaded: " + "{}".format(data["name"]))

                        return total_files
                    except KeyboardInterrupt:
                        # when CTRL+C is pressed during the execution of this script,
                        # bring the cursor to the beginning, erase the current line, and dont make a new line
                        sys.exit()

                for file in data:
                    file_url = file["download_url"]
                    file_name = file["name"]

                    if flatten:
                        path = os.path.basename(file["path"])
                    else:
                        path = file["path"]
                    dirname = os.path.dirname(path)

                    if dirname != '':
                        os.makedirs(os.path.dirname(path), exist_ok=True)
                    else:
                        pass

                    if file_url is not None:
                        try:
                            opener = urllib.request.build_opener()
                            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                            urllib.request.install_opener(opener)
                            # download the file
                            urllib.request.urlretrieve(file_url, path)

                            # bring the cursor to the beginning, erase the current line, and dont make a new line
                            print("Downloaded: " + "{}".format(file_name))

                        except KeyboardInterrupt:
                            # when CTRL+C is pressed during the execution of this script,
                            # bring the cursor to the beginning, erase the current line, and dont make a new line
                            sys.exit()
                    else:
                        self.upgrade(file["html_url"], dir_out)

            return total_files
