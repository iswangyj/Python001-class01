from abc import ABCMeta, abstractmethod

class Zoo(object):
    def __init__(self, name):
        self.animals = []
        self.name = name

    def add_animal(self, instance):
        if type(instance).__name__ in self.animals:
            print(f'{type(instance).__name__} existed')
        else:
            self.animals.append(type(instance).__name__)
            self.__dict__[type(instance).__name__] = instance


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, type, shape, nature):
        self.type = type
        self.shape = shape
        self.nature = nature
        if self.type == '食肉' and self.shape in ('中等', '大型') and self.nature == '凶猛':
            self.is_fierce_animal = True
        else:
            self.is_fierce_animal = False


class Cat(Animal):
    voice = '喵喵喵'
    is_suitable_pet = True

    def __init__(self, name, type, shape, nature):
        super().__init__(type, shape, nature)
        self.name = name


	
if __name__ == '__main__':
	
    # 实例化动物园
	
    z = Zoo('时间动物园')
	
    # 实例化一只猫，属性包括名字、类型、体型、性格
	
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
	
    # 增加一只猫到动物园
	
    z.add_animal(cat1)
	
    # 动物园是否有猫这种动物
	
    have_cat = getattr(z, 'Cat')