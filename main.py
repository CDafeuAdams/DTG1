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


def your_day_trip(tl_list, tr_list, trans_list, te_list):
    rando_tex_loc = random.choice(tl_list)
    rando_tex_res = random.choice(tr_list)
    rando_trans = random.choice(trans_list)
    rando_tex_ent = random.choice(te_list)
    return [rando_tex_loc, rando_tex_res, rando_trans, rando_tex_ent]

def user_confirmation (list_of_random_items, day_trip_lists):
    user_satisfied = False
    while user_satisfied == False:
        print(f"""Your destination is {list_of_random_items[0]} and you'll be eating at {list_of_random_items[1]}. 
        You'll then take a {list_of_random_items[2]} to go {list_of_random_items[3]}.""")
        user_input = input("Are you satisfied with the selections? Y or N")
        if user_input == "Y":
            user_satisfied = True
        elif user_input == "N":
            list_of_random_items = your_day_trip(day_trip_lists[0],day_trip_lists[1],day_trip_lists[2],day_trip_lists[3])
        else: 
            print(f"Have a great trip!")
    return list_of_random_items

# I changed rando_list to list_of_random_items for both the elif and the return so that the code doesn't break
# I also moved the print to the next line, which was originally on the same line as else
# I also removed the 2nd equal sign from the user_satified == True to user_satified = True, because it kept comparing the true and false and broke there. It wouldn't move forward. 
# I changed the user_input as I was asking for additional input and didn't neet to i.e. if user_input == input("Y") <-- this asking twice, which was unnecessary
# I then added day_trip_lists to rando_list
# I removed the code rando_list = lists_of_random_items, because it wasn't needed after I added my day_trip_lists to the user_confirmation
# I had issues in this areas of my list with the list I created in the function user_confirmation. I watched Amy fix the issues I was having.

#I was following along with Pascal's DTG and as I started to change things around it printed my entire list, instead of randomly selecting one each of the different sections.

def day_trip_lists_run():
    day_trip_lists = list_generator()
    randomized_day_trip_lists = your_day_trip(day_trip_lists[0],day_trip_lists[1],day_trip_lists[2],day_trip_lists[3],)
    randomized_day_trip_lists = user_confirmation(randomized_day_trip_lists, day_trip_lists)
    print(f"Your destination is {randomized_day_trip_lists[0]} and you'll be eating at {randomized_day_trip_lists[1]}. You'll then take a {randomized_day_trip_lists[2]} to go {randomized_day_trip_lists[3]}.")

# I added the list of the day_trip_lists and added I day_trip_list to the 2nd randomized_day_trip_lists and also to the user_confirmation list


greet_user()
day_trip_lists_run()