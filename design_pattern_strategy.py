# strategy design pattern
#   A design pattern that shows composition
#   should be prefered over inheritance

# just like interfaces in c# or java

from abc import ABC, abstractmethod
from typing import NoReturn, Type


class car(ABC):
    ''' strategy '''

    @abstractmethod
    def start_engine(self, key) -> NoReturn:
        pass

    @abstractmethod
    def engage_handbrake(self) -> NoReturn:
        pass

    @abstractmethod
    def disengage_handbrake(self) -> NoReturn:
        pass

    @abstractmethod
    def turn_off_engine(self, key) -> NoReturn:
        pass


class hybrid_car(car):
    '''  implements strategy '''

    def start_engine(self, key) -> NoReturn:
        print('start eletric motor')
        print('start gas engine')

    def engage_handbrake(self) -> NoReturn:
        print('turn on full regen mode')
        print('engage all physical brakes')

    def disengage_handbrake(self) -> NoReturn:
        print('disable regen mode')
        print('disengage all pyhsical brakes')

    def turn_off_engine(self, key) -> NoReturn:
        print('stop gas engine')
        print('turn off eletric motor')


class internal_combustion_car(car):
    def start_engine(self, key) -> NoReturn:
        print('start gas engine')

    def engage_handbrake(self) -> NoReturn:
        print('engage all physical brakes')

    def disengage_handbrake(self) -> NoReturn:
        print('disengage all pyhsical brakes')

    def turn_off_engine(self, key) -> NoReturn:
        print('turn off eletric motor')


class smart_car_controller():

    def __init__(self, somecar: Type[car]):
        self._car = somecar

    def start_car(self):
        self._car.disengage_handbrake()
        self._car.start_engine()
