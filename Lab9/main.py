import classesPac

def main():
    wp = classesPac.WaterPistol()
    if wp.make_settings():
        wp.make_some_shoots(4, 10)
        print("--- Weapon info ---\nModel = " + wp.get_guns_model() +
              ";\nServiceability = " + str(wp.get_guns_serviceability()) +
              ";\nBullets = " + str(wp.get_guns_bullet_count()))
        print("Pressure =", wp.calculate_wp())
    else:
        print("Something went wrong")
    wp.dispose()

if __name__ == "__main__":
    main()