# also wrapper
# make incompatible classes compatible
import abc


class animal(abc.ABC):
    @abc.abstractmethod
    def check_pulse(self) -> bool:
        raise NotImplementedError


class wild_dog(animal):
    ''' adaptee'''

    def belly_rub(self) -> str:
        return 'woof'

    def throw_bone(self) -> str:
        return 'huff and puff'

    def check_pulse(self) -> bool:
        return True


class wild_cat(animal):
    ''' adaptee'''

    def head_rub(self) -> str:
        return 'meow'

    def point_laser(self) -> str:
        return 'scratch scratch'

    def check_pulse(self) -> bool:
        return True


class iPet(abc.ABC):
    ''' adaptor'''
    @abc.abstractmethod
    def pet(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def play(self) -> str:
        raise NotImplementedError


class adapter_dog(iPet):

    def __init__(self):
        self._wild_dog = wild_dog()

    def pet(self) -> str:
        return self._wild_dog.belly_rub()

    def play(self) -> str:
        return self._wild_dog.throw_bone()


class adatper_cat(iPet):

    def __init__(self):
        self._wild_cat = wild_cat()

    def pet(self) -> str:
        return self._wild_cat.head_rub()

    def play(self) -> str:
        return self._wild_cat.point_laser()
