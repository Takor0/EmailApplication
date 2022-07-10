import csv


class CsvEmailReader:
    __file = None
    __reader = None
    __email_index = None

    def open_file(self, file_path):
        self.__file = open(file_path, 'r')
        self.__reader = csv.reader(self.__file, delimiter=';')
        self.__email_index = next(self.__reader).index('email')

    def read_next(self):
        try:
            email = next(self.__reader)
            return email[self.__email_index]
        except StopIteration:
            return False

    def close_file(self):
        self.__file.close()
