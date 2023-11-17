import random

class Serviceability:
    def __init__(self, model=None):
        """Constructor for the Serviceability class."""
        self.available_models = ["FN Five-seven", "Glock 17", "HK45 Tactical", "Sig Sauer M11-A1 9mm", "Beretta M9"]
        self.model = model if model else random.choice(self.available_models)
        self.serv = 100

    def get_model(self):
        """Method to get the model of the pistol."""
        return self.model

    def get_serv(self):
        """Method to get the current pistol serviceability."""
        return self.serv

    def reduce(self):
        """Method to simulate reducing serviceability with usage."""
        self.serv -= random.randint(0, 2)
        if self.serv < 10:
            print("WARNING: Serviceability less than 10%")

    def repair(self, money):
        """Method to repair the weapon for a specified cost."""
        if money >= 500:
            res = random.randint(0, 9)
            if res >= 4:
                print("Your weapon is repaired successfully")
                self.serv = 100
                return True
            else:
                print("Sorry, your weapon could not be repaired")
                return False
        else:
            print("Repairs cost 500 units")
            return False
