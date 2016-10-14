import sys
sys.path.append('./')
from world import *

def main():
    v_draw_distance = 16
    h_draw_distance = int(v_draw_distance * 2.5)

    if h_draw_distance % 2 != 0:
        h_draw_distance -= 1

    window_width = 80
    window_height = 24

    v_padding = int((window_height - v_draw_distance) / 2) 
    h_padding = 4

    world_size = 'large'

    world_one = make_world(world_size)

    room_count = []
    room_count.append([])
    room_count.append([])
    room_count.append([])
    room_count.append([])
    room_count.append([])

    sprite_count = []
    sprite_count.append([])

    corpses = []
    sprites = {}
    hero_name = input("What is your name? ")
    sprites[hero_name] = Hero(hero_name, int(180/2), int(180/2))
    hero_alive = True
    while hero_alive == True:
        print_window(world_one, window_height, window_width, hero_name, sprites, v_padding, h_padding, v_draw_distance, h_draw_distance)
        move = get_move()
        clear_scrn()
        if move == 'q':
            break
        move_hero(world_one, move, room_count, world_size, sprite_count, sprites, hero_name)
        update_sprites(world_one, sprites, hero_name, move)
        meat_wagon(world_one, sprites, hero_name, corpses)
        funeral_pyre(world_one, sprites, corpses)
        hero_alive = is_hero_alive(sprites, hero_name)
    if move == 'q':
        print('Come Back Soon!')
    else:
        print('You Died!')

main()
