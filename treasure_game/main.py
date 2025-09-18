from json import load, dump
from os import system
from time import sleep
from random import choice, randint

def main():
    system('cls')
    with open('player.json', 'r') as file:
        player_data = load(file)
        system('cls')
        
        while True:
            new_or_load_game = input("<1> New game\n<2> Load game\n -> ").strip()

            if new_or_load_game == '1':
                player_name = input("Enter your name: ").strip().title()
                player_health = player_data["health"]
                player_inventory = []
                system('cls')
                break
            elif new_or_load_game == '2':
                player_name = player_data["name"]
                player_health = player_data["health"]
                player_inventory = player_data["inventory"]
                system('cls')
                break
            else:
                pass
                system('cls')

    with open('map.json', 'r') as file:
        map = load(file)
        locations = []

        for areas in map.keys():
            locations.append(areas.title())

    welcome = f"Welcome, {player_name}. Prepare yourself for the journey ahead.\n"
    animate(welcome)
    enter_to_continue = input("Press enter to continue...")
    sleep(1.5)
    system('cls')

    while True:
        pass

        events = ["found_treasure", "encountered_danger", "nothing"]
        display()
        user_choice = input("Enter your choice: ").strip()
        system('cls')

        if user_choice == '1':
            show_areas(locations)
            where_to_explore = input("Where do u want to explore?\n -> ").strip().title()
            system('cls')
            if where_to_explore in locations:
                event = choice(events)
                if event == events[0]:
                    player_inventory.append(map[where_to_explore.lower()]["treasure"])
                    event0 = f"{player_name} stumbled upon {map[where_to_explore.lower()]["treasure"]}.\n"
                    animate(event0)
                    press_enter()
                elif event == events[1]:
                    lost_health = randint(5, 13)
                    player_health -= lost_health
                    if player_health > 0:
                        event1 = f"A sudden {map[where_to_explore.lower()]["danger"]} struck unexpectedly, causing {player_name} to lose {lost_health} health!\n"
                        animate(event1)
                        press_enter()
                    else:
                        message = f"{player_name}'s final heartbeat echoes through the void.\n"
                        animate(message)
                        sleep(2)
                        break
                elif event == events[2]:
                    event2 = f"{player_name} searched every corner but came up empty-handed.\n"
                    animate(event2)
                    press_enter()
            else:
                pass
        elif user_choice == '2':
            show_stats(player_name, player_health, player_inventory)
            press_enter()
        elif user_choice == '3':
            warning_msg = "⚠️  Warning: This action may overwrite your current progress.\n"
            animate(warning_msg)
            yes_or_no = input("Proceed anyway? (y/n): ").strip().lower()

            if yes_or_no == 'y':
                player_data["name"] = player_name
                player_data["health"] = player_health
                player_data["inventory"] = player_inventory
                
                with open('player.json', 'w') as file:
                    dump(player_data, file, indent=4)

                saved = "Your progress has been saved!\n"
                animate(saved)
                press_enter()
            elif yes_or_no == 'n':
                unsaved = f"The chapter remains unrecorded.\n"
                animate(unsaved)
                press_enter()
            else:
                pass
                system('cls')
        elif user_choice == '4':
            warning_msg = "The echoes of adventure begin to fade.\n"
            animate(warning_msg)
            yes_or_no = input("Proceed anyway? (y/n): ").strip().lower()

            if yes_or_no == 'y':
                message = f"May your next journey be even greater {player_name}.\n"
                animate(message)
                sleep(1)
                break
            elif yes_or_no == 'n':
                message = f"You chose to stay. Let the adventure continue {player_name}.\n"
                animate(message)
                press_enter()
            else:
                pass
                system('cls')
        else:
            pass


def display():
    print("<1> Explore the areas\n<2> View stats\n<3> Save progress\n<4> Exit the game")


def show_areas(array):
    print("===== AVAILABLE AREAS =====")
    for areas in array:
        print(f"❖ {areas.title()}")


def press_enter():
    enter_to_continue = input("Press enter to continue...")
    system('cls')


def show_stats(name, health, inv):
    counts = {}
    print(f"─────────────────────────\n      PLAYER STATS\n─────────────────────────\nName      : {name}\nHealth    : {health}\n\nInventory :")
    
    for items in inv:
        counts[items] = counts.get(items, 0) + 1

    for key, value in counts.items():
        print(f"  • {key}  x {value}")

    print("─────────────────────────")


def animate(string):
    for chars in string:
        print(f"{chars}", end="", flush=True)
        sleep(0.05)


if __name__ == "__main__":
    main()