from src.Validator.EmailValidator import EmailValidator


class IncorrectEmailProcessor:
    __result = []

    def __init__(self, email_validator: EmailValidator):
        self.__email_validator = email_validator

    def process(self, email):
        if not self.__email_validator.is_valid(email):
            self.__result.append(email)

    def get_result(self):
        return self.__result
