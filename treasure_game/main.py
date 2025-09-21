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

            match new_or_load_game:
                case '1':
                    player_name = input("Enter your name: ").strip().title()
                    player_health = player_data["health"]
                    player_inventory = []
                    system('cls')
                    break
                case '2':
                    player_name = player_data["name"]
                    player_health = player_data["health"]
                    player_inventory = player_data["inventory"]
                    system('cls')
                    break
                case _:
                    system('cls')

    with open('map.json', 'r') as file:
        map = load(file)
        locations = []

        for areas in map.keys():
            locations.append(areas.title())

    animate(f"Welcome, {player_name}. Prepare yourself for the journey ahead.")
    enter_to_continue = input("Press enter to continue...")
    sleep(1.5)
    system('cls')

    while True:
        events = ["found_treasure", "encountered_danger", "nothing"]
        print("<1> Explore the areas\n<2> View stats\n<3> Save progress\n<4> Exit the game")
        user_choice = input("Enter your choice: ").strip()
        system('cls')

        match user_choice:
            case '1':
                show_areas(locations)
                where_to_explore = input("Where do u want to explore?\n -> ").strip().title()
                system('cls')
                if where_to_explore in locations:
                    event = choice(events)
                    match event:
                        case "found_treasure":
                            player_inventory.append(map[where_to_explore.lower()]["treasure"])
                            animate(f"{player_name} stumbled upon {map[where_to_explore.lower()]["treasure"]}.")
                            press_enter()
                        case "encountered_danger":
                            lost_health = randint(5, 13)
                            player_health -= lost_health
                            if player_health > 0:
                                animate(f"A sudden {map[where_to_explore.lower()]["danger"]} struck unexpectedly, causing {player_name} to lose {lost_health} health!")
                                press_enter()
                            else:
                                animate(f"{player_name}'s final heartbeat echoes through the void.")
                                sleep(2)
                                break
                        case "nothing":
                            animate(f"{player_name} searched every corner but came up empty-handed.")
                            press_enter()
                else:
                    pass
            case '2':
                show_stats(player_name, player_health, player_inventory)
                press_enter()
            case '3':
                animate("⚠️  Warning: This action may overwrite your current progress.")
                yes_or_no = input("Proceed anyway? (y/n): ").strip().lower()

                match yes_or_no:
                    case 'y':
                        player_data["name"] = player_name
                        player_data["health"] = player_health
                        player_data["inventory"] = player_inventory
                        
                        with open('player.json', 'w') as file:
                            dump(player_data, file, indent=4)

                        animate("Your progress has been saved!")
                        press_enter()
                    case 'n':
                        animate("The chapter remains unrecorded.")
                        press_enter()
                    case _:
                        system('cls')
            case '4':
                animate("The echoes of adventure begin to fade.")
                yes_or_no = input("Proceed anyway? (y/n): ").strip().lower()

                match yes_or_no:
                    case 'y':
                        animate(f"May your next journey be even greater {player_name}.")
                        sleep(1)
                        break
                    case 'n':
                        animate(f"You chose to stay. Let the adventure continue {player_name}.")
                        press_enter()
                    case _:
                        system('cls')
            case _:
                pass


def show_areas(array):
    print("===== AVAILABLE AREAS =====")
    for areas in array:
        print(f"❖ {areas}")


def press_enter():
    enter_to_continue = input("Press enter to continue...")
    system('cls')


def show_stats(name, health, inv):
    counts = {}
    print(f"─────────────────────────\n      PLAYER STATS\n─────────────────────────\nName      : {name}\nHealth    : {health}\n\nInventory :")
    
    for items in inv:
        counts[items] = counts.get(items, 0) + 1

    for key, value in counts.items():
        print(f"  • {key:<14}  x {value:>1}")

    print("─────────────────────────")


def animate(string):
    for char in string:
        print(char, end="", flush=True)
        sleep(0.05)
    print()


if __name__ == "__main__":
    main()