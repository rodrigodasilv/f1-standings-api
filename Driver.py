import team_colors

class DriverObj:
    def __init__(self, driver):
        self.position = int(driver.find("div", class_="rank").text)
        self.points = int(driver.find("div", class_="f1-wide--s").text)
        self.name = driver.find("span", class_="d-block f1--xxs f1-color--carbonBlack").text.upper()
        self.surname = driver.find("span", class_="d-block f1-bold--s f1-color--carbonBlack").text.upper()
        self.team = driver.find("p", class_="listing-item--team f1--xxs f1-color--gray5").text.upper()
        self.team_color = team_colors.team_colors_list.get(self.team)
        self.picture = driver.find("picture",class_="listing-item--photo").find("source")['data-srcset'].split()[0][:-1]