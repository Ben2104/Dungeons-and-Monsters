from entity import Entity
from map1 import Map
import random
class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, max_hp = 25)
        self._loc = [0,0]
    @property
    def loc(self):
        '''getter for location'''
        return self._loc
    
    def attack(self, entity):
        '''attack method'''
        damge = random.randint(2,5)
        entity.take_damge(damge)
        
        return f"{self._name} attacks a {entity.name} for {damge} damage"
    def go_north(self)-> chr:
        '''go_north method'''
        m = Map()
        self._loc[0] -= 1
        if self._loc[0] < 0:
            self._loc[0] += 1
            return 'o'
        m.reveal(self._loc)
        return m[self._loc[0]][self._loc[1]]

        
    def go_south(self)-> chr:
        '''go_south method'''
        m = Map()
        self._loc[0] += 1
        if self._loc[0] > len(m)-1:
            self._loc[0] -= 1
            return 'o'
        m.reveal(self._loc)
        return m[self._loc[0]][self._loc[1]]
        
    def go_west(self)-> chr:
        '''go_west method'''
        m = Map()
        self._loc[1] -= 1
        if self._loc[1] < 0:
            self._loc[1] += 1
            return 'o'
        m.reveal(self._loc)
        return m[self._loc[0]][self._loc[1]]
    def go_east(self) -> chr:
        '''go east method'''
        m = Map()
        self._loc[1] += 1
        if self._loc[1] > len(m):
            self._loc[1] -= 1
            return 'o'
        m.reveal(self._loc)
        return m[self._loc[0]][self._loc[1]]
    