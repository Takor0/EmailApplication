from src.Validator.InputValidator import InputValidator
from src.Application import Application
from src.OutputPrinter.ConsoleOutputPrinter import ConsoleOutputPrinter
from src.EmailProcessor.EmailProcessorFactory import EmailProcessorFactory
from src.EmailReader.EmailReaderFactory import EmailReaderFactory
from src.LogReader.TextFileLogReader import TextFileLogReader
from src.Validator.EmailValidator import EmailValidator


def main():
    logs_reader = TextFileLogReader()
    email_validator = EmailValidator()
    email_reader_factory = EmailReaderFactory()
    email_processor_factory = EmailProcessorFactory(email_validator, logs_reader)
    input_validator = InputValidator()
    output_printer = ConsoleOutputPrinter()

    application = Application(email_reader_factory, email_processor_factory, input_validator, output_printer)
    try:
        application.run()
    except Exception:
        print("Unexpected Error")


if __name__ == '__main__':
    main()
