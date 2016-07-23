from Objects import Animal


# Inherit from Animal class
# located in another file


class Dog(Animal, object):

    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        #Animal.__init__(self)
        #self.all_data = [name, height, weight, sound]
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print ('Dog')

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} and owner is {}".format(self.get_name(),
                        self.get_height(),
                        self.get_weight(),
                        self.get_sound(),
                        self.__owner)

        # attributes are not required to be sent in
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print self.get_sound()
        else:
            print self.get_sound() * how_many


spot = Dog("Spot", 53, 27, "Ruff", "Jenny")
print spot.toString()
