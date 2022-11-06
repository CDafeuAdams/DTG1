import random

def greet_user():
    print("Hello Traveler")
traveler_name = input("What is your name?")
print("Hello " + traveler_name)

def list_generator():
    texas_locations = ["Houston", "Austin", "San Antonio", "El Paso", "Waco", "Arlington", "Corpus Christi", "Dallas", "Fort Worth", "Plano", "Laredo"]
    texas_restaurants = ["Mo Better Brews", "Torchy's", "Cappy's", "Zino's Greek", "Magnolia Table", "Pappadeaux Seafood Kitchen", "Saltwater Grill", "Rodeo Goat", "Enchilada's Ole", "Grace", "Tabernilla"]
    transportations = ["motorcycle", "horse", "car", "train", "monster truck", "SUV", "helicopter", "boat", "hot air balloon"]
    texas_entertainments = ["to the Rodeo", "Fishing", "to the Beach", "to Six Flags", "to the River Walk", "to the Space Center", "to the Natural Bridge Caverns", "to the Museum", "to the Van Gogh Exhibit", "to the Comedy Club", "to the Aquarium", "to the Zoo", "to the National Park"]
    return [texas_locations, texas_restaurants, transportations, texas_entertainments]