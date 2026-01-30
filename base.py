# 基础代码，包含干草，灌木，树，胡萝卜，南瓜，向日葵,仙人掌的种植
def Total_harvest():
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            if can_harvest():
                harvest()
            move(North)
        move(East)


def Glass_plant():
    clear()
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                move(North)
            move(East)


def Wood_plant():
    clear()
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                plant(Entities.Bush)
                move(North)
            move(East)
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                    move(North)
            move(East)


def Tree_plant():
    clear()
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if x % 2 == 0 and y % 2 != 0 or x % 2 == 1 and y % 2 != 1:
                    plant(Entities.Tree)
                move(North)
            move(East)
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                    move(North)
            move(East)


def Carrot_plant():
    clear()
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Soil:
                    till()
                if get_water() <= 0.3:
                    use_item(Items.Water)
                plant(Entities.Carrot)
                move(North)
            move(East)
        Total_harvest()


def Pumpkin_plant():
    clear()
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if get_ground_type() != Grounds.Soil:
                    till()
                if get_water() <= 0.3:
                    use_item(Items.Water)
                plant(Entities.Pumpkin)
                move(North)
            move(East)
        while True:
            dead = 0
            for i in range(get_world_size()):
                for j in range(get_world_size()):
                    if get_entity_type() == Entities.Dead_Pumpkin:
                        harvest()
                        plant(Entities.Pumpkin)
                        dead += 1
                    move(North)
                move(East)
            if dead == 0:
                harvest()
                break


def Sunflowers_plant():
    clear()
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if get_ground_type() != Grounds.Soil:
                    till()
                if get_water() <= 0.3:
                    use_item(Items.Water)
                plant(Entities.Sunflower)
                move(North)
            move(East)
        for n in range(15, 6, -1):
            for x in range(get_world_size()):
                for y in range(get_world_size()):
                    if measure() == n:
                        harvest()
                    move(North)
                move(East)


def cactus_plant():
    clear()
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):
                if get_ground_type() == Grounds.Grassland:
                    till()
                plant(Entities.Cactus)
                move(East)
            move(North)
        n = 0
        while True:
            i = 0
            Size = get_world_size()
            for x in range(Size):
                L = measure()
                move(East)
                R = measure()
                if L > R and x != get_world_size() - 1:
                    swap(West)
                    i += 1
            if i == 0:
                move(North)
                n += 1
            if n == get_world_size():
                break
        n = 0
        while True:
            i = 0
            Size = get_world_size()
            for x in range(Size):
                L = measure()
                move(North)
                R = measure()
                if L > R and x != get_world_size() - 1:
                    swap(South)
                    i += 1
            if i == 0:
                move(East)
                n += 1
            if n == get_world_size():
                harvest()
                break
