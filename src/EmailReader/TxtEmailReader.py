class TxtEmailReader:
    __file = None

    def open_file(self, file_path):
        self.__file = open(file_path, 'r')

    def read_next(self):
        email = self.__file.readline()
        if len(email) == 0:
            return False
        else:
            return email.strip()

    def close_file(self):
        self.__file.close()
