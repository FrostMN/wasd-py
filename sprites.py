import math

class Sprite(object):
    def __init__(self, name, x, y):
        self._name = name
        self._x = x
        self._y = y

    def __str__(self):
        return 'Name: %s\nX: %s Y: %s\nAttack: %s\nArmor: %s\nHP: %s\nLevel: %s'\
               % (self._name, self._x, self._y, int(self.getAttackStr()), int(self.getArmorStr()), int(self._currentHP), int(self.getLevel()))

    def getName(self):
        return self._name
    
    def getAttackStr(self):
        return self._attack_strength

    def getArmorStr(self):
        return self._armor_strength

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def getCurrentHP(self):
        return self._currentHP

    def setCurrentHP(self, currentHP):
        self._currentHP = currentHP

    def getLevel(self):
        return self._level


class Hero(Sprite):
    _maxHP = 10
    _currentHP = 10
    _level = 1
    _currentXP = 0
    _next_levelXP = 5
    _attack_strength = 1
    _armor_strength = 1
    _kills = 0
    _potions = 3
    
    def __init__(self, name, x, y):
        Sprite.__init__(self, name, x, y)

    def rest(self):
        if self._currentHP < self._maxHP:
            self._currentHP += 1

    def defendAtt(self, sprites, monster_key):
        attack_dmg = sprites[monster_key].getAttackStr()
        self.setCurrentHP(self.getCurrentHP() - (attack_dmg - self._armor_strength))

    def getMaxHP(self):
        return self._maxHP
    
    def getCurrentXP(self):
        return self._currentXP

    def setCurrentXP(self, currentXP):
        self._currentXP = currentXP

    def getNextLevelXP(self):
        return self._next_levelXP

    def setNextLevelXP(self, next_level):
        self._next_levelXP = next_level

    def levelUP(self):
        self._maxHP += 5
        self._currentHP = self._maxHP
        self._level += 1
        self._next_levelXP += 5
        self._attack_strength += 1

    def getKills(slef):
        return slef._kills

    def killIncrement(slef):
        slef._kills += 1

    def getPotions(self):
        return self._potions

    def usePotion(self):
        if self._potions > 0:
            self._currentHP = self._maxHP
            self._potions -= 1

    

    
class Goblin(Sprite):
    _currentHP = 3
    _attack_strength = 2
    _armor_strength = 0
    
    def __init__(self, name, x, y, hero_level = 0):
        Sprite.__init__(self, name, x, y)
        self._level = math.ceil(hero_level * (2/3))

    def defendAtt(self, sprites, hero_name):
        attack_dmg = sprites[hero_name].getAttackStr()
        currentHP = self._currentHP - (attack_dmg - self._armor_strength)
        self.setCurrentHP(currentHP)

    def levelUP(self):
        self._currentHP = self._level + 2
        self._armor_strength = self._level - 1
        self._attack_strength = self._level + 1


    def moveGoblin(self, world, hero_move, sprites, hero_name):
        hero_x = sprites[hero_name].get_x()
        hero_y = sprites[hero_name].get_y()
        if self._y > hero_y:
            test = world[self._y - 1][self._x]
            if test != 1 and test != 2 and test != 3 and test != 7 and test != 8:
                if world[self._y - 1][self._x] != 3:
                    world[self._y][self._x] = 0
                    world[self._y - 1][self._x] = self._name
                    self.set_y(self._y - 1)
                    return 0
            if test == 3:
                sprites[hero_name].defendAtt(sprites, str(self._name))                    
                return 0
        if self._x > hero_x:
            test = world[self._y][self._x - 1]
            if test != 1 and test != 2 and test != 3 and test != 7 and test != 8:
                if world[self._y][self._x - 1] != 3:
                    world[self._y][self._x] = 0
                    world[self._y][self._x - 1] = self._name
                    self.set_x(self._x - 1)
                    return 0
            if test == 3:
                sprites[hero_name].defendAtt(sprites, self._name)
                return 0
        if self._y < hero_y:
            test = world[self._y + 1][self._x]
            if test != 1 and test != 2 and test != 3 and test != 7 and test != 8:
                if world[self._y + 1][self._x] != 3:
                    world[self._y][self._x] = 0
                    world[self._y + 1][self._x] = self._name
                    self.set_y(self._y + 1)
                    return 0
            if test == 3:
                sprites[hero_name].defendAtt(sprites, self._name)
                return 0
        if self._x < hero_x:
            test = world[self._y][self._x + 1]
            if test != 1 and test != 2 and test != 3 and test != 7 and test != 8:
                if world[self._y][self._x + 1] != 3:
                    world[self._y][self._x] = 0
                    world[self._y][self._x + 1] = self._name
                    self.set_x(self._x + 1)
                    return 0
            elif test == 3:
                sprites[hero_name].defendAtt(sprites, self._name)
                return 0

