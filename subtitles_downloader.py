import requests
from bs4 import BeautifulSoup
import urllib.request


a=input("Enter movie name: ").replace(" ","+")

base="https://opensubtitles.org/en/search2/sublanguageid-eng/moviename-{}"

r=requests.get(base.format(a))
soup=BeautifulSoup(r.text,"lxml")
data=soup.find_all("a",class_="bnone")
if len(data)>0:

        for i in range(len(data)):
            print(i+1,")",data[i]["title"],data[i]["href"])

        inp=int(input(">>"))
        filename=data[inp-1]["title"]
        r=requests.get("https://opensubtitles.org/"+data[inp-1]["href"])
        soup=BeautifulSoup(r.text,"lxml")
        try:

                data=soup.find_all("a",class_="bnone")[0]["href"].split("/")


                movie_id=[int(i) for i in data if i.isdigit()]
                urllib.request.urlretrieve("https://opensubtitles.org/en/subtitleserve/sub/{}".format(movie_id[0]),"{}.zip".format(filename[12:].replace(" ","_")))

                print("subtitle downloaded")
        except:
            data=soup.find_all("a",class_="bt-dwl external adds_trigger",href=True)

            dfile=requests.get("https://opensubtitles.org/",data[0]["href"],allow_redirects=True)


            urllib.request.urlretrieve("https://opensubtitles.org"+data[0]["href"],"{}.zip".format(filename[12:].replace(" ","_")))
            print("subtitle downloaded")
else:
    print("No results found")
