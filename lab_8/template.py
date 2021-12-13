import csv
from abc import ABC, abstractmethod
from itertools import groupby

import numpy as np
import pandas as pd
from matplotlib.pyplot import pie, axis, show
import matplotlib.pyplot as plt


class Pipeline(ABC):
    def __init__(self, data_file):
        self.data_file = data_file

    def template_method(self) -> None:
        pass
        # self.base_operation1()
        # self.required_operations1()
        # self.base_operation2()
        # self.hook1()
        # self.required_operations2()
        # self.base_operation3()
        # self.hook2()

    # These operations already have implementations.

    def read_data(self) -> None:
        self.data_file = pd.read_csv("playstation_4_games.csv")
        return self.data_file

    def extract_features(self) -> None:
        print(self.data_file.columns)

    def visualize_features(self, index, column) -> None:
        self.index = ()
        self.data_file = pd.DataFrame(3 * np.random.rand(4), index=index, columns=column)
        self.data_file.plot.pie(subplots=True)
        plt.show()

    # def hook1(self):
    #     pass

    # @abstractmethod
    # def proceed_request_1(self, *args) -> None:
    #     pass
    #
    # @abstractmethod
    # def proceed_request_2(self, *args) -> None:
    #     pass


class GenreProcessor(Pipeline):
    def hook1(self, dict_from_csv):
        self.dict_from_csv = pd.read_csv('playstation_4_games.csv').to_dict()
        return print(self.dict_from_csv)

    def proceed_request_1(self, *args) -> None:
        print(self.dict_from_csv[self.dict_from_csv['Genre'] == 'Puzzle'])

    def proceed_request_2(self, *args) -> None:
        self.visualize_features(index=['Adventure', 'Platformer', 'Puzzle', 'Action'], column='Genre')


class DeveloperProcessor(Pipeline):

    def proceed_request_1(self, *args) -> None:
        pass

    def proceed_request_2(self, *args) -> None:
        print("ConcreteClass2 says: Implemented Operation2")


# def client_code(abstract_class: AbstractClass) -> None:
#     """
#     The client code calls the template method to execute the algorithm. Client
#     code does not have to know the concrete class of an object it works with, as
#     long as it works with objects through the interface of their base class.
#     """
#
#     # ...
#     abstract_class.template_method()
#     # ...
#
#
# if __name__ == "__main__":
#     print("Same client code can work with different subclasses:")
#     client_code(ConcreteClass1())
#     print("")
#
#     print("Same client code can work with different subclasses:")
#     client_code(ConcreteClass2())

# pipeline = Pipeline(data_file='')
#
# pipeline.read_data()
# pipeline.extract_features()
# pipeline.hook1()
# pipeline.visualize_features(, column=['Genre'])

genre = GenreProcessor(data_file='')
genre.hook1(dict_from_csv='playstation_4_games.csv')
# genre.proceed_request_1()
