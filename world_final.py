import sys
sys.path.append('./')
from movement_final import *

def make_world(size):
    sizes = { 'small' : 60,
              'medium' : 120,
              'large' : 180
              }
    world = [[i for i in range(sizes[size])] for j in range(sizes[size])]
    def_world(world)
    return world


def number_to_tile(key):
    if isinstance(key, str) == True:
        return 'G'
    tiles = { 0 : '.', # .
              1 : '#', # #
              2 : '∩', # ∩
              3 : 'H', # H
              4 : 'T', # T
              5 : 'G', # G
              7 : '∩', # ∩
              8 : '∩', # ∩
              9 : ' '
              } #
    return tiles[key]

def clear_scrn():
    clear = ''
    for i in range(40):
        clear += '\n'
    print (clear)


def get_slice_index(world, window_row, sprites, hero_name):
#    hero = find_hero(world)
    hero_y = sprites[hero_name].get_y()
    if window_row == 5:
        return hero_y - 7
    if window_row == 6:
        return hero_y - 6
    if window_row == 7:
        return hero_y - 5
    if window_row == 8:
        return hero_y - 4
    if window_row == 9:
        return hero_y - 3
    if window_row == 10:
        return hero_y - 2
    if window_row == 11:
        return hero_y - 1
    if window_row == 12:
        return hero_y - 0
    if window_row == 13:
        return hero_y + 1
    if window_row == 14:
        return hero_y + 2
    if window_row == 15:
        return hero_y + 3
    if window_row == 16:
        return hero_y + 4
    if window_row == 17:
        return hero_y + 5
    if window_row == 18:
        return hero_y + 6
    if window_row == 19:
        return hero_y + 7    

def get_view_slice(world, index, sprites, hero_name):
    hero_x = sprites[hero_name].get_x()
    view_slice = ''
    for x in range(len(world)):
        if x >= hero_x - 18 and x <= hero_x + 18:
            view_slice += number_to_tile(world[index][x])
    return view_slice

def get_stat_slice(index, sprites, hero_name):
    stat_width = 24
    stat_slice = ''
    
    if index == 5:
        for col in range(stat_width):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 6:
        stat_slice += '   Name: '
        if len(hero_name) > 12:
            for ind in range(len(hero_name)):
                if ind < 12:
                    stat_slice += hero_name[ind]
            stat_slice += '   '
        else:
            stat_slice += hero_name
            for ch in range(stat_width -len(stat_slice)):
                stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 7:
        stat_slice += '   HP: '
        stat_slice += str(sprites[hero_name].getCurrentHP())
        stat_slice += ' / '
        stat_slice += str(sprites[hero_name].getMaxHP())
        for ch in range(stat_width -len(stat_slice)):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 8:
        stat_slice += '   Armour Str: '
        stat_slice += str(sprites[hero_name].getArmorStr())
        for ch in range(stat_width -len(stat_slice)):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 9:
        stat_slice += '   Attack Str: '
        stat_slice += str(sprites[hero_name].getAttackStr())
        for ch in range(stat_width -len(stat_slice)):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 10:
        stat_slice += '   Potions: '
        stat_slice += str(sprites[hero_name].getPotions())
        for ch in range(stat_width -len(stat_slice)):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 11:
        for col in range(stat_width):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 12:
        stat_slice += '   Level: '
        stat_slice += str(sprites[hero_name].getLevel())
        for ch in range(stat_width -len(stat_slice)):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 13:
        stat_slice += '   XP: '
        stat_slice += str(sprites[hero_name].getCurrentXP())
        stat_slice += ' / '
        stat_slice += str(sprites[hero_name].getNextLevelXP())
        for ch in range(stat_width -len(stat_slice)):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 14:
        stat_slice += '   Kills: '
        stat_slice += str(sprites[hero_name].getKills())
        for ch in range(stat_width -len(stat_slice)):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    if index == 15:
        stat_slice = '   Movement: w a s d    *....'
        return stat_slice
    if index == 16:
        stat_slice = '   Potions: p           *....'
        return stat_slice
    if index == 17:
        stat_slice = '   Rest: r   Quit: q    *....'
        return stat_slice
    if index == 18:
        for col in range(stat_width):
            stat_slice += ' '
        stat_slice += '*....'
        return stat_slice
    

def print_window(world, height, width, hero_name, sprites, v_padding, h_padding, v_draw_distance, h_draw_distance):
    hero_x = sprites[hero_name].get_x()
    hero_y = sprites[hero_name].get_x()

    window = ''
    for row in range(height):
        view_slice = ''
        for col in range(width):
            """ start top border """
            if row == 0 and col == 0:
                window += '+'
            if row == 0 and col > 0 and col < len(range(width - 1)):
                window += '-'
            if row == 0 and col == len(range(width - 1)):
                window += '+'
            """ stop top border """

            """ start top padding """
            if row > 0 and row < v_padding and col > 0 and col < len(range(width - 1)):
                window += '.'
            """ start top padding """

            """ start botom padding """
            if row > len(range(height - 1)) - v_padding and row < len(range(height - 1)) and col > 0 and col < len(range(width - 1)):
                window += '.'
            """ stop botom padding """

            """ start left border """
            if col == 0 and (row != 0 and row != len(range(height - 1))):
                window += '|'
            """ stop left border """

            """ start left padding """
            if col > 0 and col < h_padding and (row >= v_padding and row <= len(range(height - 1)) - v_padding):
                window += '.'
            """ stop left padding """            

            """ start view + border"""
            if row == v_padding and col > h_padding and col < h_padding + h_draw_distance:
                window += '*'

            if row == v_padding and col == h_padding + h_draw_distance:
                window += '......**************************....'

            """ view """
            if col == h_padding + 1 and (row > v_padding and row < len(range(height - 1)) - v_padding):
                window += '*'
                window += get_view_slice(world, get_slice_index(world, row, sprites, hero_name), sprites, hero_name)
                window += '*......*'
                window += str(get_stat_slice(row, sprites, hero_name))
            """stop view"""
            

            if row == len(range(height - 1)) - v_padding and col > h_padding and col < h_padding + h_draw_distance:
                window += '*'

            if row == len(range(height - 1)) - v_padding and col == h_padding + h_draw_distance:
                window += '......**************************....'

            """ stop view border """            

            """ start right border """
            if col == len(range(width - 1)) and (row != 0 and row != len(range(height - 1))):
                window += '|'
            """ stop right border """

            """ start bottom border """
            if row == len(range(height - 1)) and col == 0:
                window += '+'
            if row == len(range(height - 1)) and col > 0 and col < len(range(width - 1)):
                window += '-'
            if row == len(range(height - 1)) and col == len(range(width - 1)):
                window += '+'
            """ stop bottom border """
        window += '\n'
    print(window)
        
    
    

def def_world(board):
    '''zeros arrays'''
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 9
    '''adds ones for walls'''
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0:              # Make Top Border Walls 
                board[i][j] = 1
            if j == 0:              # Make Left Border Walls
                board[i][j] = 1
            if i == len(board) - 1: # Male Bottom Border Walls
                board[i][j] = 1
            if j == len(board) - 1: # Make Right Border Walls
                board[i][j] = 1
            if j == int((len(board)/2) - 3) and i >= int((len(board)/2) - 3) and i <= int((len(board)/2) + 3):
                board[i][j] = 1
                if i == int((len(board)/2)):
                    board[i][j] = 8
            if j == int((len(board)/2) + 3) and i >= int((len(board)/2) - 3) and i <= int((len(board)/2) + 3):
                board[i][j] = 1
                if i == int((len(board)/2)):
                    board[i][j] = 8
            if i == int((len(board)/2) - 3) and j >= int((len(board)/2) - 3) and j <= int((len(board)/2) + 3):
                board[i][j] = 1
                if j == int((len(board)/2)) and i == int((len(board)/2) - 3):
                    board[i][j] = 8
            if j > int((len(board)/2) - 3) and j < int((len(board)/2) + 3) and i > int((len(board)/2) - 3) and i < int((len(board)/2) + 3):
                board[i][j] = 0
            if i == int((len(board)/2) + 3) and j >= int((len(board)/2) - 3) and j <= int((len(board)/2) + 3):
                board[i][j] = 1
                if j == int((len(board)/2)) and  i == int((len(board)/2) + 3):
                    board[i][j] = 8
            if i == int(len(board)/2) and j == int(len(board)/2):
                board[i][j] = board[i][j] = 3
    return board
