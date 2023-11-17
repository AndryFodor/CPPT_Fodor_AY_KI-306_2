
class Bullet:
    def __init__(self, count=20):
        """Constructor for the Bullet class."""
        if count <= 20:
            self.bullet = count
        else:
            self.bullet = 0
            print("Pistol can consist of a maximum of 20 bullets")

    def reduce(self):
        """Method to simulate using a bullet."""
        if self.bullet == 0:
            print("Your gun is unloaded")
            return False
        elif self.bullet == 1:
            print("It was your last bullet")
            self.bullet -= 1
            return True
        else:
            self.bullet -= 1
            return True

    def reload(self):
        """Method to reload bullets to the maximum."""
        self.bullet = 20

    def get_bullets(self):
        """Method to get the current bullet count."""
        return self.bullet

