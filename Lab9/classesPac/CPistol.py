from .CBullet import Bullet
from .CShooting import Shooting
from .CServiceability import Serviceability

class Pistol:
    count_without_param = 0
    count_with_param = 0

    def __init__(self, bullet_count=None, model=None):
        """Constructor for the Pistol class."""
        if bullet_count is None and model is None:
            self.bullets = Bullet()
            self.serviceability = Serviceability()
            self.shoot = Shooting()
            Pistol.count_without_param += 1
        else:
            self.bullets = Bullet(bullet_count)
            self.serviceability = Serviceability(model)
            self.shoot = Shooting()
            Pistol.count_with_param += 1

    def make_some_shoots(self, how_many, distance):
        """Method to simulate shooting multiple times."""
        print("-----You started shooting-----")
        while how_many != 0:
            if self.shoot.make_shoot(distance, self.serviceability, self.bullets):
                print("You hit the target")
            else:
                print("You missed the target")
            how_many -= 1

    def get_hit_shoots(self):
        """Method to get the count of hit shoots."""
        return self.shoot.get_hit_shoots()

    def get_missed_shoots(self):
        """Method to get the count of missed shoots."""
        return self.shoot.get_missed_shoots()

    def get_accuracy(self):
        """Method to get the accuracy of shots."""
        return self.shoot.get_accuracy_of_shots()

    def repair_gun(self, money):
        """Method to repair the gun."""
        if self.serviceability.repair(money):
            print("-----You have repaired your gun-----")
        else:
            print("-----You failed to repair your gun-----")

    def get_guns_serviceability(self):
        """Method to get the serviceability of the pistol."""
        return self.serviceability.get_serv()

    def get_guns_model(self):
        """Method to get the model of the pistol."""
        return self.serviceability.get_model()

    def dispose(self):
        """Method to release used resources."""
        pass

    def get_guns_bullet_count(self):
        """Method to get the current bullet count."""
        return self.bullets.get_bullets()

    def reload_gun(self):
        """Method to reload the gun."""
        self.bullets.reload()
        print("-----You have reloaded your gun-----")
