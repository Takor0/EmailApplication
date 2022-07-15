from src.Error import InputError

from src.EmailReader.TxtEmailReader import TxtEmailReader
from src.EmailReader.CsvEmailReader import CsvEmailReader


class EmailReaderFactory:
    def make(self, file_type):
        if file_type == '.txt':
            return TxtEmailReader()
        if file_type == '.csv':
            return CsvEmailReader()
        raise InputError.UnknownEmailReaderTypeError
