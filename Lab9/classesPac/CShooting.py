import random

class Shooting:
    def __init__(self):
        """Constructor for the Shooting class."""
        self.hit_shoots = 0
        self.missed_shoots = 0

    def get_hit_shoots(self):
        """Method to get the count of hit shoots."""
        return self.hit_shoots

    def get_missed_shoots(self):
        """Method to get the count of missed shoots."""
        return self.missed_shoots

    def get_accuracy_of_shots(self):
        """Method to get the accuracy of shots."""
        total_shots = self.hit_shoots + self.missed_shoots
        return f"{round((self.hit_shoots / total_shots) * 100)}%"

    def make_shoot(self, distance, serviceability, bullets):
        """Method to simulate one shoot."""
        if serviceability.get_serv() <= 0:
            print("Your weapon is broken")
            return False
        elif not bullets.reduce():
            return False
        else:
            serviceability.reduce()
            res = distance * random.randint(0, 9)
            if res < 50:
                self.hit_shoots += 1
                return True
            else:
                self.missed_shoots += 1
                return False
