import re
from os.path import exists

from src.Error.InputError import FileDoesNotExistError, UnreadableLogFileError


class TextFileLogReader:
    EMAIL_SEARCH_REGEX = "^.+'(.+)'.*$"
    __file = None

    def is_file_opened(self):
        return self.__file is not None

    def open_file(self, path_to_log_file):
        if exists(path_to_log_file):
            self.__file = open(path_to_log_file, 'r')
        else:
            raise FileDoesNotExistError("Cannot find log file by given path")

    def reset_position(self):
        self.__file.seek(0)

    def read_next_email(self):
        try:
            log = self.__file.readline()
        except UnicodeDecodeError:
            raise UnreadableLogFileError("Given log file is unreadable")
        if len(log) == 0:
            return False
        else:
            email = re.search(self.EMAIL_SEARCH_REGEX, log).group(1)
            return email

    def close_file(self):
        self.__file.close()
