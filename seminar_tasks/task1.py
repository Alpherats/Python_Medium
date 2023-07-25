class GamePerson:
    _max_level = 80

    def __init__(self, name, race = 'human', speed = 100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level
    def deal_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            if self.health < 0:
                print('U are dead!')


p1 = GamePerson("Artas", "Undead")
print(p1.name)

