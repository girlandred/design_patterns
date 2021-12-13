from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Pipeline(ABC):
    def __init__(self, data_file):
        self.data_file = data_file

    def template_method(self) -> None:
        self.read_data()
        self.proceed_request_1()
        self.visualize_features(index=['Adventure', 'Platformer', 'Puzzle', 'Action'], column='Genre')
        self.proceed_request_2()

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

    @abstractmethod
    def proceed_request_1(self, *args) -> None:
        pass

    @abstractmethod
    def proceed_request_2(self, *args) -> None:
        pass


class GenreProcessor(Pipeline):
    def proceed_request_1(self, *args) -> None:
        genres = self.data_file.loc[self.data_file['Genre'] == 'Puzzle']
        return print(genres)

    def proceed_request_2(self, *args) -> None:
        self.visualize_features(index=['Adventure', 'Platformer', 'Puzzle', 'Action'], column='Genre')


class DeveloperProcessor(Pipeline):
    def proceed_request_1(self, *args) -> None:
        developer = self.data_file.loc[self.data_file['Developer'] == 'Funbox Media']
        print(developer)

    def proceed_request_2(self, *args) -> None:
        self.visualize_features(index=['Gonzo Games', 'Toxic Games', 'ON3D Studios', 'Funbox Media'],
                                column='Developer')


def client_code(pipe_line: Pipeline) -> None:
    pipe_line.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(GenreProcessor(data_file=''))
    print("")

    print("Same client code can work with different subclasses:")
    client_code(DeveloperProcessor(data_file=''))

# pipeline = Pipeline(data_file='')
#
# pipeline.read_data()
# pipeline.extract_features()
# pipeline.hook1()
# genre = GenreProcessor(data_file='')
# genre.proceed_request_1()
