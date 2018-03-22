
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL


url = "https://www.apple.com/itunes/charts/songs/"

html_content = urlopen(url).read().decode("utf8")
soup = BeautifulSoup(html_content, "html.parser")

section = soup.find('section',"section chart-grid")
#vì ul k có tên, khó tìm nên mình chọn là section

li_list = section.find_all("li")


datas=[]
for li in li_list:
    data={}
    data["names"] = li.h3.a.string
    data["artists"]=li.h4.a.string
    datas.append(data)
pyexcel.save_as(records=datas,dest_file_name="iTuneslist.xls")


#part 2
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)

for li in li_list:
    song = li.h3.a.string
    artist = li.h4.a.string
    dl.download([song + ' ' + artist])
