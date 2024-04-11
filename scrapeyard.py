import requests
import json
import Driver
from bs4 import BeautifulSoup

def scrape_drivers_data():
    html_doc = requests.get('https://www.formula1.com/en/drivers.html')
    soup = BeautifulSoup(html_doc.content, 'html.parser')
    data = []
    all_drivers = (soup.find_all("div", class_="col-12 col-md-6 col-lg-4 image-center") + soup.find_all("div", class_="col-12 col-md-6 col-lg-4 col-xl-3"))

    for cur_driver in all_drivers:
        dloop = Driver.DriverObj(cur_driver)
        driver_data = {'position': dloop.position, 'points': dloop.points, 'driver_name': dloop.name, 'driver_surname': dloop.surname, 'team': dloop.team, 'team_color': dloop.team_color,'picture': dloop.picture}
        data.append(driver_data)
        
    return json.dumps(data, ensure_ascii=False)

def get_drivers_data():
    return scrape_drivers_data()