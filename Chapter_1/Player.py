"""
2.4 Inheritance

Goal: Extend your previous class by creating another class that is a child class of the current one

STEP-BY_STEP:
    STEP 1: Think of an IS-A relationship that could apply to your current class to form a child class.
        For example: If you have a class called 'warrior' maybe a child class could be 'Samurai'

    STEP 2: Write a new class that inherits from your old class
        Add AT LEAST one attribute in your child class that your parent class does not have
        Remember to properly initialize the child class and include super() to initialize the attributes in the parent class
            See the vehicle6.py example of how we did this

    STEP 3: Write a new method in your child class
        The new method SHOULD be named the same as in your parent class but do something different

            For example, if you have a method called attack in your parent class it should also be in your child class.
                However, the two methods should NOT be identical

    STEP 4: Demonstrate your implementation by creating an instance from the child class and calling the method
"""

from Exercises.Chapter_1.GameObject import GameObject


class Player(GameObject):
    def __init__(self, name, class_type, inventory, position = (0,0), hp=100, level=1, attack=10, defense=5, active=True, ):
        super().__init__(name, class_type, position, hp, level, attack, defense, active)
        self.__inventory = inventory

    def get_inventory(self):
        return list(self.__inventory)

    def __str__(self):
        return f"{self.name}: {self._class_type} at Position {self.get_position()}"

if __name__ == "__main__":
    player1 = Player("Harry", "Mage", dict())
    print(player1)
    print(player1.get_inventory())
