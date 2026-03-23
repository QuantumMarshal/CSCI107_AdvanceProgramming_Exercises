class GameObject:
    def __init__(self, name, class_type, position = (0,0), hp=100, level=1, attack=10, defense=5, active=True):
        self.name = name
        self._class_type = class_type
        self.__position = position
        self.__hp = hp
        self.__stamina = 0
        self.__level = level
        self.__attack = attack
        self.__defense = defense
        self.__active = active

    def get_stamina(self):
        return self.__stamina

    def set_stamina(self, stamina):
        if stamina >= 0:
            self.__stamina = stamina
        else:
            print("You can't set negative value")

    def get_position(self):
        return self.__position

    def update_pos(self, new_pos):
        prev_pos = self.__position
        self.__position = new_pos
        return f"You move from {prev_pos} to {new_pos}. New Position: {self.__position}"

    def deal_dmg(self, target):
        target.take_dmg(self.__attack)
        print(f"{self.name} deal {self.__attack} to {target.name}")

    def take_dmg(self, dmg):
        self.hp = self.__hp - max(dmg - self.__defense, 0)
        print(f"{self.name} has {self.__hp} HP left.")
        return self.hp


