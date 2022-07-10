class Error(Exception):
    pass


class UnknownEmailReaderTypeError(Error):
    pass


class TextIsTooLongError(Error):
    pass


class FileDoesNotExistError(Error):
    pass


class UnknownEmailProcessorArgError(Error):
    pass


class UnreadableLogFileError(Error):
    pass
