import collections
import re
from src.Validator.EmailValidator import EmailValidator


class GroupByDomainEmailProcessor:
    DOMAIN_REGEX = "^[^@]+@([^@]+\\.[a-zA-Z0-9]{1,4})$"
    __grouped_by_domains = {}

    def __init__(self, email_validator: EmailValidator):
        self.__email_validator = email_validator

    def process(self, email):
        if self.__email_validator.is_valid(email):
            domain = re.search(self.DOMAIN_REGEX, email).group(1)
            if domain not in self.__grouped_by_domains:
                self.__grouped_by_domains[domain] = [email]
            else:
                self.__grouped_by_domains[domain].append(email)

    def get_result(self):
        result = collections.OrderedDict(sorted(self.__grouped_by_domains.items()))
        for i in result:
            result[i] = list(dict.fromkeys(result[i]))
            result[i].sort()
        return result
