import requests
import json
import Driver
from bs4 import BeautifulSoup


def get_drivers_data():
    html_doc = requests.get('https://www.formula1.com/en/drivers.html')
    soup = BeautifulSoup(html_doc.content, 'html.parser')
    all_drivers_array = []
    all_drivers_html = (soup.find_all("div", class_="f1-inner-wrapper flex flex-col gap-xs"))
    for curr_driver_html in all_drivers_html:
        position = int(curr_driver_html.find(name="p",
                                             class_="f1-heading-black font-formulaOne tracking-normal font-black "
                                                    "non-italic text-fs-42px leading-none").text)
        points = int(curr_driver_html.find(name="p",
                                           class_="f1-heading-wide font-formulaOneWide tracking-normal font-normal "
                                                  "non-italic text-fs-18px leading-none normal-case").text)
        name = curr_driver_html.find(name="p",
                                     class_="f1-heading tracking-normal text-fs-12px leading-tight uppercase "
                                            "font-normal non-italic f1-heading__body font-formulaOne").text
        surname = curr_driver_html.find(name="p", class_="f1-heading tracking-normal text-fs-18px leading-tight "
                                                         "uppercase font-bold non-italic f1-heading__body "
                                                         "font-formulaOne").text

        team = curr_driver_html.find(name="p",
                                     class_="f1-heading tracking-normal text-fs-12px leading-tight normal-case "
                                            "font-normal non-italic f1-heading__body font-formulaOne "
                                            "text-greyDark").text
        picture_url = curr_driver_html.find(name="img", class_="f1-c-image ml-0 mr-0 pr-s max-w-3/4").get('src')

        curr_driver = Driver.Driver(position=position,
                                    points=points,
                                    name=name,
                                    surname=surname,
                                    team=team,
                                    picture_url=picture_url)

        all_drivers_array.append(curr_driver.to_dict())

    return json.dumps(all_drivers_array, ensure_ascii=False)
