import os
from os import listdir
from os.path import isfile, join

from src.Error.InputError import TextIsTooLongError, FileDoesNotExistError, UnknownEmailProcessorArgError,\
    UnreadableLogFileError, UnknownEmailReaderTypeError
from src.EmailReader.EmailReaderFactory import EmailReaderFactory
from src.Validator.InputValidator import InputValidator
from src.OutputPrinter.ConsoleOutputPrinter import ConsoleOutputPrinter
from src.EmailProcessor.EmailProcessorFactory import EmailProcessorFactory


class Application:
    EMAIL_FILES_DIRECTORY = './storage/emails'

    def __init__(self, email_reader_factory: EmailReaderFactory,
                 email_processor_factory: EmailProcessorFactory,
                 input_validator: InputValidator,
                 output_printer: ConsoleOutputPrinter):

        self.__email_reader_factory = email_reader_factory
        self.__email_processor_factory = email_processor_factory
        self.__input_validator = input_validator
        self.__output_printer = output_printer

    def run(self):
        try:
            args = self.__input_validator.validate()
            result = self.__process_emails(args)
            self.__output_printer.print_result(result, args)
        except (TextIsTooLongError, FileDoesNotExistError, UnknownEmailProcessorArgError, UnreadableLogFileError) as e:
            self.__output_printer.print_error(e)

    def __get_email_files(self):
        email_files = [file for file in listdir(self.EMAIL_FILES_DIRECTORY) if
                       isfile(join(self.EMAIL_FILES_DIRECTORY, file))]
        return email_files

    def __process_emails(self, args):
        email_processor = self.__email_processor_factory.make(args)
        email_files = self.__get_email_files()
        for file_name in email_files:
            split_file_name = os.path.splitext(file_name)
            file_extension = split_file_name[1]
            try:
                email_reader = self.__email_reader_factory.make(file_extension)
            except UnknownEmailReaderTypeError:
                continue
            email_reader.open_file(os.path.join(self.EMAIL_FILES_DIRECTORY, file_name))
            while True:
                email = email_reader.read_next()
                if email is False:
                    break
                email_processor.process(email)
            email_reader.close_file()
        return email_processor.get_result()
