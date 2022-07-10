from src.Error import InputError

from src.EmailReader.TxtEmailReader import TxtEmailReader
from src.EmailReader.CsvEmailReader import CsvEmailReader


class EmailReaderFactory:
    def make(self, type):
        if type == '.txt':
            return TxtEmailReader()
        if type == '.csv':
            return CsvEmailReader()
        raise InputError.UnknownEmailReaderTypeError
