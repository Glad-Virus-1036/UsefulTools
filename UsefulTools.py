import pyautogui as p
import json
import os
import random
import sympy.physics.units as u

def clipboard():

    data = {}

    if not os.path.exists('path'):
        with open('path', 'w') as f:
            json.dump(data, f)
    
    else:
        with open('path', 'r') as f:
            data = json.load(f)

    userinput = input('Enter the text you want to save: ')
    
    data['text'] = userinput

    with open('path', 'w') as f:
        json.dump(data, f)

    user_choice = input('Would you like to see what is currently in the clipboard? (y/n): ')  
    
    if user_choice.lower() == 'y':
        
        with open('path', 'r') as f:
            data = json.load(f)
        
        print(data.get('text', 'No text found in clipboard.'))
        input('Press Enter to continue...')
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

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


while True:
    try:
        print('Welcome to UsefulTools v1.0.0-alpha. Select a tool:')
        print('1. Center Mouse')
        print('2. Clipboard')
        print('3. Quick Converter')
        print('4. Random Number Picker')
        print('\n')
    
        choice = input('Select a number: ')
        print('\n')

        if choice != ['1', '2', '3', '4']:
            raise ValueError
    
    except ValueError:
        print('Please select one of the numbers.')

    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == '1':
        p.moveTo(p.size().width / 2, p.size().height / 2, duration=0.5)
        print('Mouse centered.')
        input('Press Enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')
    
    if choice == '2':
        clipboard()
        os.system('cls' if os.name == 'nt' else 'clear')
    
    if choice == '3':
        converter()
    
    if choice == '4':
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