from Objects import Animal
from Inheritance import Dog

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

cat = Animal('Masik', 22, 10, 'Meow')
dog = Dog('Pusik', 39, 27, 'Bark', 'Jenny')

test_animals.get_type(cat)
test_animals.get_type(dog)