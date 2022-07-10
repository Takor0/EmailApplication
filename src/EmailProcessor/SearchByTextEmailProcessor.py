from src.Validator.EmailValidator import EmailValidator


class SearchByTextEmailProcessor:
    __result = []

    def __init__(self, email_validator: EmailValidator, text_to_search):
        self.__email_validator = email_validator
        self.__text_to_search = text_to_search

    def process(self, email):
        if self.__email_validator.is_valid(email):
            if self.__text_to_search in email:
                self.__result.append(email)

    def get_result(self):
        self.__result.sort()
        return self.__result
