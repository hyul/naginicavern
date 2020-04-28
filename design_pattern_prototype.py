import copy
import abc
import datetime
import random
import time


class IPrototype(abc.ABC):

    @abc.abstractclassmethod
    def clone(self):
        pass


class TrackedValue(IPrototype):

    def __init__(self, number):
        self._type = "Type1"
        self._value = number
        self._creation_ts = datetime.datetime.now()

    def clone(self):
        self._creation_ts = datetime.datetime.now()
        return copy.deepcopy(self)

    def __str__(self):
        return f'type: {self._type} | value: {self._value} | timestampe: {self._creation_ts}'


class RandomValueWithSeed(IPrototype):

    """ Cheat a dice roll"""

    def __init__(self, seed):
        self._type = "not so random generator"
        self._value = None
        self._seed = seed
        random.seed(seed)
        self._seeded_random_state = random.getstate()

    def clone(self):
        random.setstate(self._seeded_random_state)
        self._value = random.randint(1, 100)
        self._seeded_random_state = random.getstate()

        return copy.deepcopy(self)

    def __str__(self):
        return f'type: {self._type} | value: {self._value}'


class ObjectFactory:

    """ Manages prototypes.
    Static factory, that encapsulates prototype
    initialization and then allows instatiation
    of the classes from these prototypes.
    """
    
    @staticmethod
    def initialize():
        ObjectFactory.__TrackedValue1 = TrackedValue(1)
        ObjectFactory.__TrackedValue2 = TrackedValue(2)
        ObjectFactory.__RandomValueWithSeed1 = RandomValueWithSeed(1)
        ObjectFactory.__RandomValueWithSeed200 = RandomValueWithSeed(200)

    @staticmethod
    def TrackedValueOf1():
        return ObjectFactory.__TrackedValue1.clone()

    @staticmethod
    def TrackedValueOf2():
        return ObjectFactory.__TrackedValue2.clone()

    @staticmethod
    def RandomValueWithSeed1():
        return ObjectFactory.__RandomValueWithSeed1.clone()

    @staticmethod
    def RandomValueWithSeed200():
        return ObjectFactory.__RandomValueWithSeed200.clone()


def main():
    ObjectFactory.initialize()

    sample_list = []

    samples = 10

    for _ in range(samples):
        sample_list.append(ObjectFactory.TrackedValueOf2())

    for sample_value in range(samples):
        for cross_compare_value in range(sample_value+1, samples):
            #  none of them has same reference
            print(
                f'Sample {sample_value} == Sample {cross_compare_value} => {sample_value is cross_compare_value}')

    for sample in sample_list:
        print(f'{id(sample)} - {sample}')

    print('----------------------------------------------------------------')
    sample_list = []
    for _ in range(samples):
        sample_list.append(ObjectFactory.RandomValueWithSeed200())

    for sample_value in range(samples):
        for cross_compare_value in range(sample_value+1, samples):
            #  none of them has same reference
            print(
                f'Sample {sample_value} == Sample {cross_compare_value} => {sample_value is cross_compare_value}')

    for sample in sample_list:
        print(f'{id(sample)} - {sample}')


if __name__ == "__main__":
    main()
