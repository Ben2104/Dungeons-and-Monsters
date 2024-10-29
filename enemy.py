from entity import Entity
import random
class Enemy(Entity):
    def __init__(self):
        super().__init__(name = random.choice(['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie', 'Werewolf', 'Wraith', 'Troll', 'Orc', 'Demon']), max_hp=random.randint(1,4))
    def attack(self, entity):
        damage = random.randint(1,4)
        entity.take_damge(damage)
        
        return f"{self._name} attacks {entity.name} for {damage} damage"
    