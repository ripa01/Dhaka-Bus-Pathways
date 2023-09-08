from bs4 import BeautifulSoup as bs
import requests

page = requests.get("https://rongdhonustudio.com/DhakaBus.html")

soup = bs(page.content)

bus_list = soup.find_all('a',class_ = 'btn btn-primary')
for bus in bus_list:
    print(bus.get_text())
    route_list = soup.find('div',class_ = 'card card-body')
    print(route_list.get_text())

