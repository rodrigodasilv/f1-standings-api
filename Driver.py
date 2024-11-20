import team_colors


class Driver:
    def __init__(self, position, points, name, surname, team, picture_url):
        self.position = position
        self.points = points
        self.name = name.upper()
        self.surname = surname.upper()
        self.team = team.upper()
        self.team_color = team_colors.team_colors_list.get(self.team)
        self.picture_url = picture_url

    def to_dict(self):
        return {
            "position": self.position,
            "points": self.points,
            "name": self.name,
            "surname": self.surname,
            "team": self.team,
            "picture_url": self.picture_url,
        }
