import os
import pandas
import random


class Model:
    __data_size = 20
    __data_path = '../Data'
    __data_file_name = 'Gender.csv'
    
    def __init__(self):
        self.__data = self.__create_data()
        self.__save_data()

    def __create_data(self):
        height = self.__create_height(self.__data_size)
        weight = self.__create_weight(self.__data_size)
        gender = self.__create_gender(self.__data_size)
        return pandas.DataFrame({'Height': height, 'Weight': weight, 'Gender': gender})

    @staticmethod
    def __create_height(size):
        return [random.uniform(4.5, 6.5) for _ in range(size)]

    @staticmethod
    def __create_weight(size):
        return [random.uniform(30.5, 100.011) for _ in range(size)]

    @staticmethod
    def __create_gender(size):
        gender = pandas.DataFrame(['Male', 'Female']).sample(n=size, replace=True).values
        return [sex[0] for sex in gender]

    def __save_data(self):
        file_path = os.path.abspath(self.__data_path)
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        self.__data.to_csv(os.path.join(file_path, self.__data_file_name), index=False)
        print('{} is saved at {}'.format(self.__data_file_name, file_path))
        

if __name__ == '__main__':
    model = Model()
