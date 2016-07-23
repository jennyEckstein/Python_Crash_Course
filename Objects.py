class Animal:
     # private variable
    __name = None # like null
    __height = ""
    __weight = ""
    __sound = ""

# constructor for the class
    def __init__(self, name , height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def toString(self):
        return \
            "{} is {} cm tall and {} kilograms and say {}".format(self.__name,self.__height,self.__weight,self.__sound)

    def get_type(self):
        print 'Animal'
    # self refer to itself - change object self

    # SETTERS
    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound

    # GETTERS
    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_sound(self):
        return self.__sound

# CLASS CALL
#cat = Animal('Wiskers',  33,  10, 'Meow')
#print cat.toString()

