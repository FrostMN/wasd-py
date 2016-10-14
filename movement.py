import sys
sys.path.append('./')
from sprites import *

import random

def get_move():
    move = '  '
    while len(move) > 1:
        move = input("Enter Move: ")
        if move == '':
            move = '  '
    return move[0]
  
def move_hero(world, move, room_count, world_size, sprite_count, sprites, hero_name):
    if move == 'i':
        for i in sprites:
            print (sprites[i])
        input()
    if move == 'p':
        for i in sprites:
            sprites[hero_name].usePotion()
    if move == 'r':
        sprites[hero_name].rest()
    mv_num = ord(move)
    hero_x = sprites[hero_name].get_x()
    hero_y = sprites[hero_name].get_y()
    if mv_num == 119:           # W
        if str(type(world[hero_y - 1][hero_x])) == "<class 'str'>":
            sprites[world[hero_y - 1][hero_x]].defendAtt(sprites, hero_name)
            return 0
        if world[hero_y - 1][hero_x] != 1:
            sprites[hero_name].set_x(hero_x)
            sprites[hero_name].set_y(hero_y - 1)
            if world[hero_y - 1][hero_x] == 8:
                world[hero_y][hero_x] = 0
                world[hero_y - 1][hero_x] = 3
                first_door(world, mv_num, sprites, hero_name)
            elif world[hero_y - 1][hero_x] == 2:
                world[hero_y][hero_x] = 0
                world[hero_y - 1][hero_x] = 3
                if world[hero_y - 2][hero_x] != 0:
                    room(world, mv_num, room_count, world_size, sprite_count, sprites, hero_name)
                    room_count.append([])                    
            elif world[hero_y - 1][hero_x] == 7:
                world[hero_y][hero_x] = 0
                world[hero_y - 1][hero_x] = 3
                if world[hero_y - 2][hero_x] != 0:
                    door(world, mv_num, sprites, hero_name)
                    room_count.append([])
            else:
                world[hero_y][hero_x] = 0
                world[hero_y - 1][hero_x] = 3
    elif mv_num == 97:            # A
        if str(type(world[hero_y][hero_x - 1])) == "<class 'str'>":
            sprites[world[hero_y][hero_x - 1]].defendAtt(sprites, hero_name)
            return 0
        if world[hero_y][hero_x - 1] != 1:
            sprites[hero_name].set_x(hero_x - 1)
            sprites[hero_name].set_y(hero_y)
            if world[hero_y][hero_x - 1] == 8:
                world[hero_y][hero_x] = 0
                world[hero_y][hero_x - 1] = 3
                first_door(world, mv_num, sprites, hero_name)
            elif world[hero_y][hero_x - 1] == 2:
                world[hero_y][hero_x] = 0
                world[hero_y][hero_x - 1] = 3
                if world[hero_y][hero_x - 2] != 0:
                    room(world, mv_num, room_count, world_size, sprite_count, sprites, hero_name)
            elif world[hero_y][hero_x - 1] == 7:
                world[hero_y][hero_x] = 0
                world[hero_y][hero_x - 1] = 3
                if world[hero_y][hero_x - 2] != 0:
                    door(world, mv_num, sprites, hero_name)
            else:
                world[hero_y][hero_x] = 0
                world[hero_y][hero_x - 1] = 3
    elif mv_num == 115:           # S
        if str(type(world[hero_y + 1][hero_x])) == "<class 'str'>":
            sprites[world[hero_y + 1][hero_x]].defendAtt(sprites, hero_name)
            return 0
        if world[hero_y + 1][hero_x] != 1:
            sprites[hero_name].set_x(hero_x)
            sprites[hero_name].set_y(hero_y + 1)
            if world[hero_y + 1][hero_x] == 8:
                world[hero_y][hero_x] = 0
                world[hero_y + 1][hero_x] = 3
                first_door(world, mv_num, sprites, hero_name)
            elif world[hero_y + 1][hero_x] == 2:
                world[hero_y][hero_x] = 0
                world[hero_y + 1][hero_x] = 3
                if world[hero_y + 2][hero_x] != 0:
                    room(world, mv_num, room_count, world_size, sprite_count, sprites, hero_name)
            elif world[hero_y + 1][hero_x] == 7:
                world[hero_y][hero_x] = 0
                world[hero_y + 1][hero_x] = 3
                if world[hero_y + 2][hero_x] != 0:
                    door(world, mv_num, sprites, hero_name)
            else:
                world[hero_y][hero_x] = 0
                world[hero_y + 1][hero_x] = 3
    elif mv_num == 100:           # D
        if str(type(world[hero_y][hero_x + 1])) == "<class 'str'>":
            sprites[world[hero_y][hero_x + 1]].defendAtt(sprites, hero_name)
            return 0
        if world[hero_y][hero_x + 1] != 1:
            sprites[hero_name].set_x(hero_x + 1)
            sprites[hero_name].set_y(hero_y)
            if world[hero_y][hero_x + 1] == 8:
                world[hero_y][hero_x] = 0
                world[hero_y][hero_x + 1] = 3
                first_door(world, mv_num, sprites, hero_name)
            elif world[hero_y][hero_x + 1] == 2:
                world[hero_y][hero_x] = 0
                world[hero_y][hero_x + 1] = 3
                if world[hero_y][hero_x + 2] != 0:
                    room(world, mv_num, room_count, world_size, sprite_count, sprites, hero_name)
            elif world[hero_y][hero_x + 1] == 7:
                world[hero_y][hero_x] = 0
                world[hero_y][hero_x + 1] = 3
                if world[hero_y][hero_x + 2] != 0:
                    door(world, mv_num, sprites, hero_name)
            else:
                world[hero_y][hero_x] = 0
                world[hero_y][hero_x + 1] = 3

def first_door(world, move, sprites, hero_name):
#    hero = find_hero(world)
    hero_x = sprites[hero_name].get_x()
    hero_y = sprites[hero_name].get_y()
    v_hall = 3
    h_hall = 8
    if move == 119:           # W
        for width in range(3):
            for leng in range(v_hall):
                if width == 0 or width == 2:
                    world[hero_y - leng][hero_x - 1 + width] = 1
                if leng == v_hall - 1 and width == 1:
                    world[hero_y - leng][hero_x - 1 + width] = 2                    
                if leng < v_hall - 1 and leng > 0 and width == 1:
                    world[hero_y - leng][hero_x - 1 + width] = 0                    
    elif move == 97:            # A
        for width in range(3):
            for leng in range(h_hall):
                if width == 0 or width == 2:
                    world[hero_y - 1 + width][hero_x - leng] = 1
                if leng == h_hall - 1 and width == 1:
                    world[hero_y - 1 + width][hero_x - leng] = 2                    
                if leng < h_hall - 1 and leng > 0 and width == 1:
                    world[hero_y - 1 + width][hero_x - leng] = 0                    
    elif move == 115:           # S
        for width in range(3):
            for leng in range(v_hall):
                if width == 0 or width == 2:
                    world[hero_y + leng][hero_x - 1 + width] = 1               
                if leng == v_hall - 1 and width == 1:
                    world[hero_y + leng][hero_x - 1 + width] = 2                    
                if leng < v_hall - 1 and leng > 0 and width == 1:
                    world[hero_y + leng][hero_x - 1 + width] = 0                    
    elif move == 100:           # D
        for width in range(3):
            for leng in range(h_hall):
                if width == 0 or width == 2:
                    world[hero_y - 1 + width][hero_x + leng] = 1
                if leng == h_hall - 1 and width == 1:
                    world[hero_y - 1 + width][hero_x + leng] = 2                    
                if leng < h_hall - 1 and leng > 0 and width == 1:
                    world[hero_y - 1 + width][hero_x + leng] = 0                    

def room(world, move, room_count, world_size, sprite_count, sprites, hero_name):
    hero_x = sprites[hero_name].get_x()
    hero_y = sprites[hero_name].get_y()
    room_h = 7
    room_w = 15
    rand_x = random.randint(1, room_w - 2)
    rand_y = random.randint(1, room_h - 3)
    if move == 119:             # W
        room_count.append([])
        for width in range(room_w):
            for leng in range(room_h):
                if width == 0 or width == room_w - 1:
                    world[hero_y - leng][hero_x - int(room_w / 2) + width] = 1
                if leng == room_h - 1 and width > 0 and width < room_w - 1:
                    world[hero_y - leng][hero_x - int(room_w / 2) + width] = 1
                if hero_x - int(room_w / 2) + width != hero_x and leng == 0:
                    world[hero_y - leng][hero_x - int(room_w / 2) + width] = 1
                if width > 0 and width < room_w - 1 and leng > 0 and leng < room_h - 1:
                    world[hero_y - leng][hero_x - int(room_w / 2) + width] = 0
                world[(hero_y - room_h + 2) + rand_y][hero_x - int(room_w / 2) + rand_x] = 'Gob_' + str(len(sprite_count)) 
        rand_door(world, move, room_count, world_size, sprites, hero_name)
        if world[hero_y - 3][hero_x + 14] == 8:
            world[hero_y - 3][hero_x + 7] = 7
        if world[hero_y - 3][hero_x - 14] == 8:
            world[hero_y - 3][hero_x - 7] = 7
        sprites['Gob_' + str(len(sprite_count))] = Goblin('Gob_' + str(len(sprite_count)), hero_x - int(room_w / 2) + rand_x,(hero_y - room_h + 2) + rand_y, sprites[hero_name].getLevel())
        sprites['Gob_' + str(len(sprite_count))].levelUP()
        sprite_count.append([])
    elif move == 97:            # A
        room_count.append([])
        for width in range(room_w):
            for leng in range(room_h):
                if leng == 0 or leng == room_h - 1:
                    world[hero_y - int(room_h / 2) + leng][hero_x - width] = 1
                if width == room_w - 1 and leng > 0 and leng < room_h - 1:
                   world[hero_y - int(room_h / 2) + leng][hero_x - width] = 1
                if hero_y - int(room_h / 2) + leng != hero_y and width == 0:
                    world[hero_y - int(room_h / 2) + leng][hero_x - width] = 1
                if leng > 0 and leng < room_h - 1 and width > 0 and width < room_w - 1:
                    world[hero_y - int(room_h / 2) + leng][hero_x - width] = 0
                world[(hero_y - int(room_h / 2)) + rand_y][hero_x - room_w + 1 + rand_x] = 'Gob_' + str(len(sprite_count))
        rand_door(world, move, room_count, world_size, sprites, hero_name)
        if world[hero_y + 5][hero_x - 7] == 8:
            world[hero_y + 3][hero_x - 7] = 7
        if world[hero_y - 5][hero_x - 7] == 8:
            world[hero_y - 3][hero_x - 7] = 7
        sprites['Gob_' + str(len(sprite_count))] = Goblin('Gob_' + str(len(sprite_count)), hero_x - room_w + 1 + rand_x, (hero_y - int(room_h / 2)) + rand_y, sprites[hero_name].getLevel())
        sprites['Gob_' + str(len(sprite_count))].levelUP()
        sprite_count.append([])
    elif move == 115:           # S
        room_count.append([])
        for width in range(room_w):
            for leng in range(room_h):
                if width == 0 or width == room_w - 1:
                    world[hero_y + leng][hero_x - int(room_w / 2) + width] = 1
                if leng == room_h - 1 and width > 0 and width < room_w - 1:
                    world[hero_y + leng][hero_x - int(room_w / 2) + width] = 1
                if hero_x - int(room_w / 2) + width != hero_x and leng == 0:
                    world[hero_y + leng][hero_x - int(room_w / 2) + width] = 1
                if width > 0 and width < room_w - 1 and leng > 0 and leng < room_h - 1:
                    world[hero_y + leng][hero_x - int(room_w / 2) + width] = 0
                world[(hero_y + 1) + rand_y][hero_x - int(room_w / 2) + rand_x] = 'Gob_' + str(len(sprite_count)) 
        rand_door(world, move, room_count, world_size, sprites, hero_name)
        if world[hero_y + 3][hero_x + 14] == 8:
            world[hero_y + 3][hero_x + 7] = 7
        if world[hero_y + 3][hero_x - 14] == 8:
            world[hero_y + 3][hero_x - 7] = 7
        sprites['Gob_' + str(len(sprite_count))] = Goblin('Gob_' + str(len(sprite_count)), hero_x - int(room_w / 2) + rand_x, (hero_y + 1) + rand_y, sprites[hero_name].getLevel())
        sprites['Gob_' + str(len(sprite_count))].levelUP()
        sprite_count.append([])
    elif move == 100:           # D
        room_count.append([])
        for width in range(room_w):
            for leng in range(room_h):
                if leng == 0 or leng == room_h - 1:
                    world[hero_y - int(room_h / 2) + leng][hero_x + width] = 1
                if width == room_w - 1 and leng > 0 and leng < room_h - 1:
                   world[hero_y - int(room_h / 2) + leng][hero_x + width] = 1
                if hero_y - int(room_h / 2) + leng != hero_y and width == 0:
                    world[hero_y - int(room_h / 2) + leng][hero_x + width] = 1
                if leng > 0 and leng < room_h - 1 and width > 0 and width < room_w - 1:
                    world[hero_y - int(room_h / 2) + leng][hero_x + width] = 0
                world[(hero_y - int(room_h / 2)) + rand_y][hero_x + 1 + (rand_x - 1)] = 'Gob_' + str(len(sprite_count))
        rand_door(world, move, room_count, world_size, sprites, hero_name)
        if world[hero_y + 5][hero_x + 7] == 8:
            world[hero_y + 3][hero_x + 7] = 7
        if world[hero_y - 5][hero_x + 7] == 8:
            world[hero_y - 3][hero_x + 7] = 7
        sprites['Gob_' + str(len(sprite_count))] = Goblin('Gob_' + str(len(sprite_count)), hero_x + 1 + (rand_x - 1), (hero_y - int(room_h / 2)) + rand_y, sprites[hero_name].getLevel())
        sprites['Gob_' + str(len(sprite_count))].levelUP()
        sprite_count.append([])

def door(world, move, sprites, hero_name):
    hero_x = sprites[hero_name].get_x()
    hero_y = sprites[hero_name].get_y()
    v_hall = 3
    h_hall = 4
    if move == 119:           # W
        for width in range(3):
            for leng in range(v_hall):
                if width == 0 or width == 2:
                    world[hero_y - leng][hero_x - 1 + width] = 1
                if leng == v_hall - 1 and width == 1:
                    world[hero_y - leng][hero_x - 1 + width] = 2                    
                if leng < v_hall - 1 and leng > 0 and width == 1:
                    world[hero_y - leng][hero_x - 1 + width] = 0                    
    elif move == 97:            # A
        if world[hero_y][hero_x - 7] == 8:
            first_door(world, move)
            return 0
        for width in range(3):
            for leng in range(h_hall):
                if width == 0 or width == 2:
                    world[hero_y - 1 + width][hero_x - leng] = 1
                if leng == h_hall - 1 and width == 1:
                    world[hero_y - 1 + width][hero_x - leng] = 2                    
                if leng < h_hall - 1 and leng > 0 and width == 1:
                    world[hero_y - 1 + width][hero_x - leng] = 0                    
    elif move == 115:           # S
        for width in range(3):
            for leng in range(v_hall):
                if width == 0 or width == 2:
                    world[hero_y + leng][hero_x - 1 + width] = 1               
                if leng == v_hall - 1 and width == 1:
                    world[hero_y + leng][hero_x - 1 + width] = 2                    
                if leng < v_hall - 1 and leng > 0 and width == 1:
                    world[hero_y + leng][hero_x - 1 + width] = 0                    
    elif move == 100:           # D
        if world[hero_y][hero_x + 7] == 8:
            first_door(world, move)
            return 0
        for width in range(3):
            for leng in range(h_hall):
                if width == 0 or width == 2:
                    world[hero_y - 1 + width][hero_x + leng] = 1
                if leng == h_hall - 1 and width == 1:
                    world[hero_y - 1 + width][hero_x + leng] = 2                    
                if leng < h_hall - 1 and leng > 0 and width == 1:
                    world[hero_y - 1 + width][hero_x + leng] = 0                    


def rand_door(world, move, room_count, world_size, sprites, hero_name):
#    hero = find_hero(world)
    hero_x = sprites[hero_name].get_x()
    hero_y = sprites[hero_name].get_y()
    door_chance = random.randint(0, 100)
    doors = 0
    door_it = 0
    wall = {  'small'  : 60,
              'medium' : 120,
              'large'  : 180
              }
    size = { 'small'  : 8,
             'medium' : 13,
             'large'  : 16
             }
    if len(room_count) < size[world_size]:
        if door_chance < 10:
            doors = 1
        elif door_chance < 90:
            doors = 2
        else:
            doors = 3
    elif len(room_count) < size[world_size]:
        if door_chance < 80:
            doors = 1
        elif door_chance < 95:
            doors = 2
        else:
            doors = 3
    elif len(room_count) < size[world_size]:
        if door_chance < 90:
            doors = 1
        elif door_chance < 99:
            doors = 2
        else:
            doors = 3
    else:
        doors = 0
    if move == 119:             # W
        w_door = False
        n_door = False
        e_door = False
        s_door = False
        if hero_x < 30:
            w_door = True
        if hero_y < 25:
            n_door = True
        if hero_x > wall[world_size] - 30:
            e_door = True
        if hero_y > wall[world_size] - 25:
            s_door = True
        if world[hero_y - 3][hero_x - 7] == 7 or world[hero_y - 3][hero_x - 10] == 2 or world[hero_y - 3][hero_x - 10] == 7:
            world[hero_y - 3][hero_x - 7] = 7
            w_door = True
            door_it += 1
        if world[hero_y - 8][hero_x] == 7 or world[hero_y - 8][hero_x] == 2 or world[hero_y - 8][hero_x] == 7:
            world[hero_y - 6][hero_x] = 7
            n_door = True
            door_it += 1
        if world[hero_y - 3][hero_x + 7] == 7 or world[hero_y - 3][hero_x + 10] == 2 or world[hero_y - 3][hero_x + 10] == 7:
            world[hero_y - 3][hero_x + 7] = 7
            e_door = True
            door_it += 1
        if world[hero_y - 3][hero_x - 10] == 1:
            w_door = True
            door_it += 1
        if world[hero_y - 8][hero_x] == 1:
            n_door = True
            door_it += 1
        if world[hero_y - 3][hero_x + 10] == 1:
            e_door = True
            door_it += 1
        while door_it < doors:
            direct = random.randint(0, 3)
            if w_door == False and direct == 0:
                world[hero_y - 3][hero_x - 7] = 7
                w_door = True
                door_it += 1
            if n_door == False and direct == 1:
                world[hero_y - 6][hero_x] = 7
                n_door = True
                door_it += 1
            if e_door == False and direct == 2:
                world[hero_y - 3][hero_x + 7] = 7
                e_door = True
                door_it += 1
    elif move == 97:            # A
        s_door = False
        w_door = False
        n_door = False
        e_door = False
        if hero_x < 30:
            w_door = True
        if hero_y < 25:
            n_door = True
        if hero_x > wall[world_size] - 30:
            e_door = True
        if hero_y > wall[world_size] - 25:
            s_door = True
        if world[hero_y - 3][hero_x - 7] == 7 or world[hero_y - 5][hero_x - 7] == 2 or world[hero_y - 5][hero_x - 7] == 7:
            world[hero_y - 3][hero_x - 7] = 7
            s_door = True
            door_it += 1
        if world[hero_y][hero_x - 14] == 7 or world[hero_y][hero_x - 16] == 2 or world[hero_y][hero_x - 16] == 7:
            world[hero_y3][hero_x - 16] = 7
            w_door = True
            door_it += 1
        if world[hero_y + 3][hero_x - 7] == 7 or world[hero_y + 5][hero_x - 7] == 2 or world[hero_y + 5][hero_x - 7] == 7:
            world[hero_y + 3][hero_x - 7] = 7
            n_door = True
            door_it += 1
        if world[hero_y - 5][hero_x - 7] == 1:
            n_door = True
            door_it += 1
        if world[hero_y][hero_x - 16] == 1:
            w_door = True
            door_it += 1
        if world[hero_y + 5][hero_x - 7] == 1:
            s_door = True
            door_it += 1
        while door_it < doors:
            direct = random.randint(0, 3)
            if s_door == False and direct == 0:
                world[hero_y + 3][hero_x - 7] = 7
                s_door = True
                door_it += 1
            if w_door == False and direct == 1:
                world[hero_y][hero_x - 14] = 7
                w_door = True
                door_it += 1
            if n_door == False and direct == 2:
                world[hero_y - 3][hero_x - 7] = 7
                n_door = True
                door_it += 1
    elif move == 115:           # S
        e_door = False
        s_door = False
        w_door = False
        n_door = False
        if hero_x < 30:
            w_door = True
        if hero_y < 25:
            n_door = True
        if hero_x > wall[world_size] - 30:
            e_door = True
        if hero_y > wall[world_size] - 25:
            s_door = True
        if world[hero_y + 3][hero_x + 7] == 7 or world[hero_y + 3][hero_x + 10] == 2 or world[hero_y + 3][hero_x + 10] == 7:
            world[hero_y + 3][hero_x + 7] = 7
            e_door = True
            door_it += 1
        if world[hero_y + 3][hero_x - 7] == 7 or world[hero_y - 3][hero_x - 10] == 2 or world[hero_y - 3][hero_x - 10] == 7:
            world[hero_y + 3][hero_x + 7] = 7
            s_door = True
            door_it += 1
        if world[hero_y + 6][hero_x] == 7 or world[hero_y + 8][hero_x] == 2 or world[hero_y + 8][hero_x] == 7:
            world[hero_y + 6][hero_x] = 7
            w_door = True
            door_it += 1
        if world[hero_y + 3][hero_x + 10] == 1:
            e_door = True
            door_it += 1
        if world[hero_y + 3][hero_x - 10] == 1:
            w_door = True
            door_it += 1
        if world[hero_y + 6][hero_x] == 1:
            s_door = True
            door_it += 1
        while door_it < doors:
            direct = random.randint(0, 3)
            if e_door == False and direct == 0:
                world[hero_y + 3][hero_x - 7] = 7
                e_door = True
                door_it += 1
            if s_door == False and direct == 1:
                s_door = True
                door_it += 1
                world[hero_y + 6][hero_x] = 7
            if w_door == False and direct == 2:
                w_door = True
                door_it += 1
                world[hero_y + 3][hero_x + 7] = 7
    elif move == 100:           # D
        s_door = False
        e_door = False
        n_door = False
        w_door = False
        if hero_x < 30:
            w_door = True
        if hero_y < 25:
            n_door = True
        if hero_x > wall[world_size] - 30:
            e_door = True
        if hero_y > wall[world_size] - 25:
            s_door = True
        if world[hero_y + 5][hero_x + 7] == 7 or world[hero_y + 3][hero_x + 7] == 2 or world[hero_y + 3][hero_x + 7] == 7:
            world[hero_y + 3][hero_x + 7] = 7
            s_door = True
            door_it += 1
        if world[hero_y - 5][hero_x + 7] == 7 or world[hero_y - 3][hero_x + 7] == 2 or world[hero_y - 3][hero_x + 7] == 7:
            world[hero_y - 3][hero_x + 7] = 7
            n_door = True
            door_it += 1
        if world[hero_y][hero_x + 14] == 7 or world[hero_y][hero_x + 14] == 2 or world[hero_y][hero_x + 16] == 7 or world[hero_y][hero_x + 16] == 2:
            world[hero_y - 3][hero_x + 7] = 7
            e_door = True
            door_it += 1
        if world[hero_y + 5][hero_x + 7] == 1:
            s_door = True
            door_it += 1
        if world[hero_y - 5][hero_x + 7] == 1:
            n_door = True
            door_it += 1
        if [hero_x + 17] == 1:
            e_door = True
            door_it += 1
        while door_it < doors:
            direct = random.randint(0, 3)
            if s_door == False and direct == 0:
                world[hero_y + 3][hero_x + 7] = 7
                s_door = True
                door_it += 1
            if e_door == False and direct == 1:
                e_door = True
                door_it += 1
                world[hero_y][hero_x + 14] = 7
            if n_door == False and direct == 2:
                n_door = True
                door_it += 1
                world[hero_y - 3][hero_x + 7] = 7
        

def update_sprites(world, sprites, hero_name, hero_move):
#    hero = find_hero(world)
    hero_x = sprites[hero_name].get_x()
    hero_y = sprites[hero_name].get_y()
    for key in sprites:
        if key != hero_name:
            sprites[key].moveGoblin(world, hero_move, sprites, hero_name)


def meat_wagon(world, sprites, hero_name, corpses):
    for key in sprites:
        if key != hero_name:
            currentHP = sprites[key].getCurrentHP()
            corpse_x = 0
            corpse_y = 0
            if currentHP < 1:
                corpse_x = sprites[key].get_x()
                corpse_y = sprites[key].get_y()
                world[corpse_y][corpse_x] = 0
                corpses.append(key)
                sprites[hero_name].setCurrentXP(sprites[hero_name].getCurrentXP() + 1)
                sprites[hero_name].killIncrement()
    if sprites[hero_name].getCurrentXP() == sprites[hero_name].getNextLevelXP():
        sprites[hero_name].levelUP()

def funeral_pyre(world, sprites, corpses):
    for body in corpses:
        sprites.pop(body)
    corpses.clear()

def is_hero_alive(sprites, hero_name):
    if sprites[hero_name].getCurrentHP() < 1:
        return False
    else:
        return True
    
"""
def make_room(x, y):
    room = []
    for row in range(y):
        room.append([])

    for row in range(y):
        for col in range(x):
            room[row].append(0)
    room = def_room(room)
    return room


def def_room(room):
    '''zeros arrays'''
    for i in range(len(room)):
        for j in range(len(room[i])):
            room[i][j] = 0
    '''adds ones for walls'''
    for i in range(len(room)):
        for j in range(len(room[i])):
            if i == 0:
                room[i][j] = 1
            if j == 0:
                room[i][j] = 1
            if i == len(room) - 1:
                room[i][j] = 1
            if j == len(room) - 1:
                room[i][j] = 1
    return room
"""
