import keyboard as k
import json
import os
import random
import sympy.physics.units as u

def clipboard():
    file_path = os.path.join(os.path.dirname(__file__), 'clipboard.json')

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump({"texts": []}, f)

    with open(file_path, 'r') as f:
        data = json.load(f)

    while True:
        print("Clipboard Menu:")
        print("1. Info (recommended to check out first)")
        print("2. Add text to clipboard")
        print("3. View clipboard contents")
        print("4. Clear clipboard")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            userinput = input("Enter the text you want to save: ")
            data["texts"].append(userinput)
            with open(file_path, 'w') as f:
                json.dump(data, f)
            print("Text saved to clipboard.")
            input('Press Enter to continue...')
        
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            if data["texts"]:
                print("Clipboard contents:")
                for i, text in enumerate(data["texts"], 1):
                    print(f"{i}. {text}")
            else:
                print("Clipboard is empty.")
            input("Press Enter to continue...")
        
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            data["texts"] = []
            with open(file_path, 'w') as f:
                json.dump(data, f)
            print("Clipboard cleared.")
            input('Press Enter to continue...')
        
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        
        else:
            print("Please select one of the numbers.")
            input('Press Enter to continue...')

def converter():
    while True:
            print('Welcome to the Quick Converter. First, type out the number that will be converted.')
            try:
                number = float(int(input()))
            except ValueError:
                print('Please type a valid number.')
                continue
            
            unit1 = input('Now enter the unit of the first number: ')

            if unit1 not in u.__dict__:
                print('Please type a valid unit.')
                continue

            unit2 = input('Now enter the unit you would like to convert the first number to. Note: units have to be related to work.')

            if unit2 not in u.__dict__:
                print('Please type a valid unit.')
                continue

            print(number * getattr(u, unit1).convert_to(getattr(u, unit2)))

            question = input('Would you like to make another conversion? (y/n): ')

            if question == 'n':
                break

            os.system('cls' if os.name == 'nt' else 'clear')

def shortkeys():
    file_path = os.path.join(os.path.dirname(__file__), 'shortkeys.json')
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump({"shortcuts": {}}, f)

    with open(file_path, 'r') as f:
        data = json.load(f)

    if not isinstance(data.get("shortcuts"), dict):
        data["shortcuts"] = {}
        with open(file_path, 'w') as f:
            json.dump(data, f)

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        print('Shortkeys Menu:')
        print('1. Info (recommended to check out first)')
        print('2. Assign a Shortkey')
        print('3. Clear Shortkeys')
        print('4. View Shortkeys')
        print('5. Exit')

        choice = input('Select a number: ')

        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == '1':
            print('Welcome to Shortkeys. Shortkeys is a UsefulTools feature that allows you to write a whole sentence with the press of a key.')
            print('To create Shortkeys, select "Assign a Shortkey" and follow the on-screen instructions.')
            print('To view Shortkeys, select "View Shortkeys".')
            print('To clear Shortkeys, select "Clear Shortkeys".')
            print('To leave the menu, select "Exit".')
            input('Press Enter to continue...')

        elif choice == '2':
            key = input('Enter the key for the Shortkey (single character or valid key): ')
            if len(key) != 1 and key not in k.all_modifiers:
                print('Please enter a valid single character or key.')
                input('Press Enter to continue...')
                continue
            if key in data["shortcuts"]:
                print(f'Warning: The key "{key}" is already assigned. It will be overwritten.')
                try:
                    k.remove_hotkey(key)
                except:
                    pass
            text = input('Enter the text for the Shortkey: ')
            data["shortcuts"][key] = text
            with open(file_path, 'w') as f:
                json.dump(data, f)
            try:
                k.add_hotkey(key, lambda text=text: k.write(text), suppress=True)
                print(f'Shortkey "{key}" assigned successfully.')
            except Exception as e:
                print(f'Error assigning Shortkey: {e}')
            input('Press Enter to continue...')

        elif choice == '3':
            confirm = input('Are you sure you want to clear all Shortkeys? (y/n): ')
            if confirm.lower() == 'y':
                for key in data["shortcuts"]:
                    try:
                        k.remove_hotkey(key)
                    except Exception as e:
                        print(f'Error removing Shortkey "{key}": {e}')
                data["shortcuts"] = {}
                with open(file_path, 'w') as f:
                    json.dump(data, f)
                print('All Shortkeys cleared.')
            else:
                print('Operation canceled.')
            input('Press Enter to continue...')

        elif choice == '4':
            if data["shortcuts"]:
                print('Current Shortkeys:')
                for key, text in data["shortcuts"].items():
                    print(f'Key: {key} -> Text: {text}')
            else:
                print('No Shortkeys assigned.')
            input('Press Enter to continue...')

        elif choice == '5':
            break

        else:
            print('Please select a valid option.')
            input('Press Enter to continue...')

while True:
    try:
        print('Welcome to UsefulTools v1.0.3-alpha. Select a tool:')
        print('NEW: 1. Shortkeys')
        print('2. Clipboard')
        print('3. Quick Converter')
        print('4. Random Number Picker')
        print('5. Changelog')
        print('\n')
    
        choice = input('Select a number: ')
        print('\n')

    except json.JSONDecodeError:
        print('placeholder')

    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == '1':
        shortkeys()

    elif choice == '2':
        clipboard()
    
    elif choice == '3':
        converter()
    
    elif choice == '4':
        print('Welcome to the Random Number Picker.')
        try:
            print('Enter the minimum number: ')
            min = int(input())
            print('Enter the maximum number: ')
            max = int(input())
        except ValueError:
            print('Please type a valid number.')
            continue
        
        print(random.randint(min, max))
        input('Press Enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif choice == '5':
        print('Welcome to the Changelog. Here you can see UsefulTools\'... changelog.')
        input('Press Enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')
        print('v1.0.1-alpha')
        print('Welcome to the Changelog!\nVersion v1.0.0-alpha had nothing interesting so I didn\'t bother to add it here.\nVersion v1.0.1-alpha includes the Changelog, and makes it so you don\'t need to change the path directory for the clipboard function (or so I hope).\nNote: Changelog, for optimization purposes, only covers the latest version.')
        input('Press Enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print('Please select one of the numbers.')
        input('Press Enter to continue...')

