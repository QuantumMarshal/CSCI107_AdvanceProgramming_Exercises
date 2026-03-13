"""
2.3 Class Methods and Property Decorators

Use vehicle5.py and dealership.py as a model to complete this

Goal: Modify the existing class from the previous exercise to include a class attribute/method and a property decorator

STEP-BY-STEP:
    STEP 1 - Add a property decorator
        Choose one attribute, it could be the one you wrote a getter/setter method for previously or another one.
        Write a property decorator for it that allows you to return its value
            See the @property in vehicle5.py for an example

    STEP 2 - Add a setter decorator
        Use property decorator you wrote in STEP 1 to to create a setter decorator.
        The decorator should accept at least one parameter similar to the setter method you wrote previously.
        The decorator should validate some data or condition then set a new value or reject the request with a message.
        See the  @price.setter decorator in vehicle5.py for an example

    STEP 3 - Demonstrate the use of your decorators.
        Create an instance from your class.
        Use the property decorator to display an attribute.
            For example we used car1.price in vehicle5.py

        Use the setter decorator to:
            1) Set a value that will be accepted and set,
                For example, we used car1.price = 35000 in vehicle5.py
            2) Set another value that will be rejected

    STEP 4 - Create a class attribute
        Create an attribute that will be applied to every instance created from the class. It DOES NOT have to be private or protected.
            For example we used __CAR_COUNT = 0 in vehicle5.py

    STEP 5 - Create a class method
        Create a class method decorator that will apply to every instance from a class in the same way.
        Call the class method from your constructor (__init__) when the object is created
            For example, we created:
                    @classmethod
                    def increase_car_count(cls)
                Then called it using: Car.increase_car_count()

    STEP 6 - Demonstrate that your class attribute works by calling it from your main code
        For example, we used:
            print(Car._Car__CAR_COUNT)
        ...to show that the car count goes up after every car instance is created
"""
import faker
import random

class Entity:
    __ENTITY_COUNT = 0
    @classmethod
    def increase_entity_count(cls):
        cls.__ENTITY_COUNT += 1

    @classmethod
    def get_entity_count(cls):
        return cls.__ENTITY_COUNT

    def __init__(self, name, class_type, position = (0,0), hp=100, level=1, attack=10, defense=5, active=True, inventory=[]):
        self.name = name
        self.class_type = class_type
        self.position = position
        self.hp = hp
        self.level = level
        self.attack = attack
        self.defense = defense
        self.active = active
        self.inventory = inventory

        self.__stamina = 0
        self._strength = 0

        self.increase_entity_count()

    @property
    def type_of_player(self):
        return self.class_type

    @type_of_player.setter
    def type_of_player(self, value):
        self.class_type = value

    @property
    def stamina(self):
        return self.__stamina
    @stamina.setter
    def stamina(self, value):
        if value < 0:
            print("Stamina cannot be negative")
        else:
            self.__stamina = value

    def get_stamina(self):
        return self.__stamina

    def set_stamina(self, stamina):
        if stamina >= 0:
            self.__stamina = stamina
        else:
            print("You can't set negative value")

    def update_pos(self, new_pos):
        prev_pos = self.position
        self.position = new_pos
        return f"You move from {prev_pos} to {new_pos}. New Position: {self.position}"

    def deal_dmg(self, target):
        target.take_dmg(self.attack)
        print(f"{self.name} deal {self.attack} to {target.name}")

    def take_dmg(self, dmg):
        self.hp = self.hp - max(dmg - self.defense, 0)
        print(f"{self.name} has {self.hp} HP left.")
        return self.hp

    def update_inventory(self, item):
        self.inventory.append(item)
        return self.inventory

if __name__ == '__main__':
    faker = faker.Faker("en_US")
    rand = random.Random()
    character = Entity("Player", "Mage")
    # print(character.__dict__)

    num = int(input("Enter the number of entities: "))
    entities = []
    for i in range(num):
        # entity_name = input("Enter the entity name: ")
        # entity_class_type = input("Enter the class type: ")
        entity_name = faker.name()
        entity_class_type = faker.job()
        entity_hp = rand.randint(0, 100)
        entities.append(Entity(entity_name, entity_class_type, hp = entity_hp))

    entities_dict = [i.__dict__ for i in entities]
    # print(entities_dict)

    print("Get class type normally:", entities[0].class_type)
    print("Get class type using decorator:",entities[0].type_of_player)
    # Set the new class type
    entities[0].type_of_player = "Developer"
    print("New class type using decorator:", entities[0].type_of_player)

    print(entities[0].stamina)
    entities[0].stamina = 100
    print(entities[0].stamina)
    entities[0].stamina = -10
    print(entities[0].stamina)

    print(Entity.get_entity_count())
