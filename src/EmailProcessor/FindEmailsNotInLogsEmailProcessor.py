from src.Validator.EmailValidator import EmailValidator
from src.LogReader.TextFileLogReader import TextFileLogReader


class FindEmailsNotInLogsEmailProcessor:
    __result = []

    def __init__(self, email_validator: EmailValidator, logs_reader: TextFileLogReader, path_to_log_file):
        self.__email_validator = email_validator
        self.__logs_reader = logs_reader
        self.__path_to_log_file = path_to_log_file

    def process(self, email):
        if self.__email_validator.is_valid(email):
            if not self.__logs_reader.is_file_opened():
                self.__logs_reader.open_file(self.__path_to_log_file)
            else:
                self.__logs_reader.reset_position()
            while True:
                log_email = self.__logs_reader.read_next_email()
                if log_email is False:
                    break
                if log_email == email:
                    return
            self.__result.append(email)

    def get_result(self):
        self.__result.sort()
        return self.__result
