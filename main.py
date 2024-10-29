from entity import Entity
from hero import Hero
from map1 import Map
from enemy import Enemy
import check_input

def main():
    name = input("What is your name, traveler? ")
    h = Hero(name)
    m = Map()
    
    choice = 0
    while choice != 5:
        e = Enemy()
        print(h)
        print(m.show_map(h.loc))
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        choice = check_input.get_int_range("Enter choice: ", 1,5)
        m.reveal(h.loc)
        if choice == 1:
            map_char = h.go_north()
            if map_char == 'o':
                print("You cannot go that way...")
            elif map_char == 'n':
                print("There is nothing here...")
            elif map_char == 'm':
                print(f"You encounter {e.names}")
                print(e)
                while e.hp != 0 or h.hp != 0:
                    print(f"1. Attack {e.name}")
                    print("2. Runaway")
                    attack_choice = check_input.get_int_range("Enter Choice: ", 1,2)
                    if attack_choice == 1:
                        print(h.attack(e))
                        print(e.attack(h))
                        
                        if e.hp == 0:
                            print(f"You have slain a {e.name}")
                            break
                        elif h.hp == 0:
                            print("You have been defeated")
                            break
                    else:
                        h.loc[0] += 1
                        break
            elif map_char == 'i':
                h.heal()
                print("You found a Health Potion! You drink it to restore your health.")
                m.remove_at_loc(h.loc)
            elif map_char == 'f':
                print("Congratulations! You found the exit.")
                print("game over")
                break
            else:
                print("this will never happen")
        elif choice == 2:
            map_char = h.go_south()
            if map_char == 'o':
                print("You cannot go that way...")
            elif map_char == 'n':
                print("There is nothing here...")
            elif map_char == 'm':
                print(f"You encounter {e.name}")
                print(e)
                while e.hp != 0 or h.hp != 0:
                    print(f"1. Attack {e.name}")
                    print("2. Runaway")
                    attack_choice = check_input.get_int_range("Enter Choice:", 1,2)
                    if attack_choice == 1:
                        print(h.attack(e))
                        print(e.attack(h))
                        if e.hp == 0:
                            print(f"You have slain a {e.name}")
                            break
                        elif h.hp == 0:
                            print("You have been defeated")
                            break
                    else:
                        h.loc[0] -= 1
                        break
            elif map_char == 'i':
                h.heal()
                print("You found a Health Potion! You drink it to restore your health.")
                m.remove_at_loc(h.loc)
            elif map_char == 'f':
                print("Congratulations! You found the exit.")
                print("game over")
                break
            else:
                print("this will never happen")
        elif choice == 3:
            map_char = h.go_east()
            if map_char == 'o':
                print("You cannot go that way...")
            elif map_char == 'n':
                print("There is nothing here...")
            elif map_char == 'm':
                print(f"You encounter {e.name}")
                print(e)
                while e.hp != 0 or h.hp != 0:
                    print(f"1. Attack {e.name}")
                    print("2. Runaway")
                    attack_choice = check_input.get_int_range("Enter Choice:", 1,2)
                    if attack_choice == 1:
                        print(h.attack(e))
                        print(e.attack(h))
                        if e.hp == 0:
                            print(f"You have slain a {e.name}")
                            break
                        elif h.hp == 0:
                            print("You have been defeated")
                            break
                    else:
                        h.loc[1] -= 1
                        break
            elif map_char == 'i':
                h.heal()
                print("You found a Health Potion! You drink it to restore your health.")
                m.remove_at_loc(h.loc)
            elif map_char == 'f':
                print("Congratulations! You found the exit.")
                print("game over")
                break
            else:
                print("this will never happen")
        elif choice == 4:
            map_char = h.go_west()
            if map_char == 'o':
                print("You cannot go that way...")
            elif map_char == 'n':
                print("There is nothing here...")
            elif map_char == 'm':
                print(f"You encounter {e.name}")
                print(e)
                while e.hp != 0 or h.hp != 0:
                    print(f"1. Attack {e.name}")
                    print("2. Runaway")
                    attack_choice = check_input.get_int_range("Enter Choice:", 1,2)
                    if attack_choice == 1:
                        print(h.attack(e))
                        print(e.attack(h))
                        if e.hp == 0:
                            print(f"You have slain a {e.name}")
                            break
                        elif h.hp == 0:
                            print("You have been defeated")
                            print("game over")
                            break
                    else:
                        h.loc[1] += 1
                        break
            elif map_char == 'i':
                h.heal()
                print("You found a Health Potion! You drink it to restore your health.")
                m.remove_at_loc(h.loc)
            elif map_char == 'f':
                print("Congratulations! You found the exit.")
                print("game over")
                break
            else:
                print("this will never happen")
        if h.hp == 0:
            break 
            
main()