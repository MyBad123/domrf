import sys
import datetime

from file_work import File


class ArrWorker:
    """work with array with 0 and 1"""

    def __init__(self, arr: str) -> None:
        self.arr: str = arr

        # control struct of arr and their values
        self.control_arr()

    def __clean_str(self):
        return self.arr.replace(']', '').replace('[', '').replace(',', '').replace(' ', '')

    def control_arr(self) -> None:
        """raise an exception if there are characters not equal to 1 or 0"""

        for i in self.__clean_str():
            if i != '0' and i != '1':
                raise ValueError('Введите в массив 0 или 1')

    def get_count_sequence(self) -> int:
        """get count of sequence for values of arr"""

        # get str without other symbols
        work_value = self.__clean_str()

        # script for getting count of sequence for values of arr
        max_sequence: int = 0
        current_sequence: int = 0

        for char in work_value:
            if char == '1':
                current_sequence += 1
                if current_sequence > max_sequence:
                    max_sequence = current_sequence
            else:
                current_sequence = 0

        return max_sequence


try:
    result = ArrWorker(sys.argv[1]).get_count_sequence()

    # write result to file
    file_name: str = datetime.datetime.now().strftime('%H:%%d.%m.%Y')
    File().create_file(file_name, result)
except IndexError:
    print('Введите массив')
except ValueError:
    print('Введите валидные данные')
