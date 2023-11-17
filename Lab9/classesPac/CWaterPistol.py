from .CPistol import Pistol



# Клас, який розширює інтерфейс Waterable та описує можливість обчислення тиску води в зброї
class waterPressure():
    k = 2
    waterAble = True
    def calculate_wp(self):
        self.pressure = self.k * 50 / self.hole_area
        return self.pressure

    def realize_waterAble(self):
        self.water = self.waterAble
        return self.get_guns_model()

class WaterPistol(Pistol, waterPressure):
    def __init__(self, bullet_count=5, model="", hole_area=5):
        super().__init__(bullet_count, model)
        self.hole_area = hole_area

    def make_some_shoots(self, how_many, distance):
        if self.water and self.pressure != 0:
            super().make_some_shoots(how_many, int(distance * (20 / self.pressure)))
            print("Water shooting is successful")
        else:
            print("Water shooting cannot be started because you don't realize waterAble or don't calculate pressure")

    def get_guns_model(self):
        return super().get_guns_model() + " water version"

    def make_settings(self):
        self.calculate_wp()
        self.realize_waterAble()
        return True

    def dispose(self):
        pass

