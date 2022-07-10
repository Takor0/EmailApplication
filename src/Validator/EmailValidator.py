import re


class EmailValidator:
    CORRECT_EMAIL_REGEX = "^[\\w!#$%&'*+\\-\\/=?^`{|}~\\.]+@[a-zA-Z0-9\\-]+\\.[a-zA-Z0-9]{1,4}$"

    def is_valid(self, email):
        if re.match(self.CORRECT_EMAIL_REGEX, email) is not None:
            return True
        return False
