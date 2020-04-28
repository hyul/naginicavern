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
        self._value = random.randint(1,100)
        self._seeded_random_state = random.getstate()
        print(f"seed is : {self._seed} | value is : {self._value}")
        return copy.deepcopy(self)

    def __str__(self):
        return f'type: {self._type} | value: {self._value}'


class ObjectFactory:

    """ Manages prototypes.
    Static factory, that encapsulates prototype
    initialization and then allows instatiation
    of the classes from these prototypes.
    """

    __type1Value1 = None
    __type1Value2 = None
    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def initialize():
        ObjectFactory.__type1Value1 = TrackedValue(1)
        ObjectFactory.__type1Value2 = TrackedValue(2)
        ObjectFactory.__type2Value1 = RandomValueWithSeed(1)
        ObjectFactory.__type2Value2 = RandomValueWithSeed(2)

    @staticmethod
    def getType1Value1():
        return ObjectFactory.__type1Value1.clone()

    @staticmethod
    def getType1Value2():
        return ObjectFactory.__type1Value2.clone()

    @staticmethod
    def getType2Value1():
        return ObjectFactory.__type2Value1.clone()

    @staticmethod
    def getType2Value2():
        return ObjectFactory.__type2Value2.clone()


def main():
    ObjectFactory.initialize()

    type1_sample_list = []

    samples = 10

    
    for _ in range(samples):
        print(_)
        type1_sample_list.append(ObjectFactory.getType1Value1())

    for sample_value in range(samples):
        for cross_compare_value in range(sample_value+1, samples):
            #  none of them has same reference
            print(
                f'Sample {sample_value} == Sample {cross_compare_value} => {sample_value is cross_compare_value}')

    for sample in type1_sample_list:
        print(f'{id(sample)} - {sample}')


    for _ in range(samples):
        type1_sample_list.append(ObjectFactory.getType2Value1())

    for sample_value in range(samples):
        for cross_compare_value in range(sample_value+1, samples):
            #  none of them has same reference
            print(
                f'Sample {sample_value} == Sample {cross_compare_value} => {sample_value is cross_compare_value}')

    for sample in type1_sample_list:
        print(f'{id(sample)} - {sample}')


if __name__ == "__main__":
    main()
