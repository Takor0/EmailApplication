from src.EmailProcessor.IncorrectEmailProcessor import IncorrectEmailProcessor
from src.EmailProcessor.SearchByTextEmailProcessor import SearchByTextEmailProcessor
from src.EmailProcessor.GroupByDomainEmailProcessor import GroupByDomainEmailProcessor
from src.EmailProcessor.FindEmailsNotInLogsEmailProcessor import FindEmailsNotInLogsEmailProcessor
from src.Validator.EmailValidator import EmailValidator
from src.LogReader.TextFileLogReader import TextFileLogReader
from src.Error import InputError


class EmailProcessorFactory:
    def __init__(self, email_validator: EmailValidator, logs_reader: TextFileLogReader):
        self.__email_validator = email_validator
        self.__logs_reader = logs_reader

    def make(self, args):
        if args.is_incorrect_emails_option_selected:
            return IncorrectEmailProcessor(self.__email_validator)
        elif args.is_search_by_text_option_selected:
            return SearchByTextEmailProcessor(self.__email_validator, args.text_to_search)
        elif args.is_group_by_domain_option_selected:
            return GroupByDomainEmailProcessor(self.__email_validator)
        elif args.is_find_email_not_in_logs_option_selected:
            return FindEmailsNotInLogsEmailProcessor(self.__email_validator, self.__logs_reader, args.path_to_log_file)
        else:
            raise InputError.UnknownEmailProcessorArgError("Required parameter")
