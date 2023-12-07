
from select import select


class Sports:
    def __init__(self, name):
        self.name = name

    @property
    def sports_name(self):
        return self.name

    @sports_name.setter
    def sports_name(self, value):
        self._name = value

class LandSport(Sports):
    def __init__(self, name, field):
        super().__init__(name)
        self._field = field

    @property
    def landsports_field(self):
        return self._field

class WaterSports(Sports):
    def __init__(self, name, activity):
        super().__init__(name)
        self._activitiy = activity

    @property
    def watersports_field(self):
        return self._activitiy

if __name__ == "__main__":
    baseball = LandSport("baseball","baseball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)

    water_skiing = WaterSports("Water sliing","Strap on your skiing and fly across the water")
    print(water_skiing.sports_name)
    print(water_skiing.watersports_field)