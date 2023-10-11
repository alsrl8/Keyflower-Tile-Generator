import os
import time
from collections import defaultdict
import json

seasons = [
    '',
    'Spring',
    'Summer',
    'Autumn',
    'Winter',
]
items = [
    '',
    'Any Resource',
    'Gold',
    'Iron',
    'Stone',
    'Wood',
    'Any Skill',
    'Random Skill',
    'Anvil',
    'Pick axe',
    'Saw',
    'Any Meeple',
    'Random Meeple',
    'Yellow Meeple',
    'Blue Meeple',
    'Red Meeple',
    'Green Meeple',
    'Transport',
    'Upgrade'
]


def clear_console():
    os.system('cls')


def get_default_file_name():
    default_file_name = 'tileinfo.json'
    return default_file_name


def handle_create_new_tile():
    def input_name():
        clear_console()
        print('Input name', end=' >> ')
        name = input().rstrip()
        if not name:
            print('Invalid name')
            time.sleep(1)
            return input_name()
        else:
            return name

    def input_season():
        clear_console()
        print('Chose season')
        for i in range(1, len(seasons)):
            print(f'{i}. {seasons[i]}')
        season = int(input())
        if not 1 <= season <= 4:
            print('Invalid season')
            time.sleep(1)
            return input_season()
        else:
            return seasons[season]

    def input_item(msg: str, prev=None):
        if prev:
            cost_dict = prev
        else:
            cost_dict = defaultdict(int)

        def add_item(item: str):
            cost_dict[item] += 1

        clear_console()
        print(msg)
        print(f'current: {cost_dict}')
        print(f'{0}. Done')
        for i in range(1, len(items)):
            print(f'{i}. Add {items[i]}')
        option = int(input())
        if not 0 <= option < len(items):
            print('Invalid item')
            time.sleep(1)
            return input_item(msg, cost_dict)
        elif option == 0:
            return cost_dict
        else:
            add_item(items[option])
            return input_item(msg, cost_dict)

    def input_basic_tile_info():

        def input_basic_tile_point():
            clear_console()
            print('Input basic tile point')
            point = int(input())
            return point

        def input_basic_cost():
            clear_console()
            return input_item('Input basic cost')

        def input_basic_reward():
            clear_console()
            return input_item('Input basic reward')

        point = input_basic_tile_point()
        cost = input_basic_cost()
        reward = input_basic_reward()
        return {
            'point': point,
            'cost': cost,
            'reward': reward,
        }

    def input_upgraded_tile_info():

        def input_upgraded_tile_point():
            clear_console()
            print('Input upgraded tile point')
            point = int(input())
            return point

        def input_upgraded_cost():
            clear_console()
            return input_item('Input upgraded cost')

        def input_upgraded_reward():
            clear_console()
            return input_item('Input upgraded reward')

        point = input_upgraded_tile_point()
        cost = input_upgraded_cost()
        reward = input_upgraded_reward()
        return {
            'point': point,
            'cost': cost,
            'reward': reward,
        }

    name = input_name()
    season = input_season()
    cost_to_upgrade = input_item('Input cost to upgrade information')
    basic_tile_info = input_basic_tile_info()
    upgraded_tile_info = input_upgraded_tile_info()

    clear_console()
    info = {
        'name': name,
        'season': season,
        'costToUpgrade': cost_to_upgrade,
        'basicTileInfo': basic_tile_info,
        'upgradedTileInfo': upgraded_tile_info,
    }

    with open(f'./data/{name}.json', 'w') as file:
        file.write(json.dumps(info, indent=4))
        file.write('\n')

    print('This program will be closed in 5 seconds')
    time.sleep(5)
    exit(0)


def handle_merge():
    merged_data = []
    data_dir = './data/'
    files = os.listdir(data_dir)
    json_files = [file for file in files if os.path.isfile(os.path.join(data_dir, file)) and file.endswith('.json')]
    print(f'json file num: {len(json_files)}')

    for json_file in json_files:
        with open(f'{data_dir}{json_file}', 'r') as file:
            data = json.load(file)
            merged_data.append(data)

    with open(f'tileinfo.json', 'w') as file:
        json.dump(merged_data, file, indent=4)

    print('This program will be closed in 5 seconds')
    time.sleep(5)
    exit(0)


def main():
    clear_console()
    print('This is keyflower tile maker')
    print(f'Default file name: {get_default_file_name()}')
    print('-' * 50)
    clear_console()
    print('Chose option')
    print('1. Create new tile')
    print('2. Merge data')
    print('9. Exit')
    user_input = int(input())
    if user_input == 1:
        handle_create_new_tile()
    elif user_input == 2:
        handle_merge()
    elif user_input == 9:
        print('Program exit')
        time.sleep(3)
        exit(0)
    else:
        print('Wrong input')
        input()
        exit(0)


if __name__ == '__main__':
    main()
