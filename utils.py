import pandas as pd

class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @classmethod
    def success(cls, message):
        print('{}{}{}'.format(cls.OKGREEN, message, cls.ENDC))

    @classmethod
    def warning(cls, message):
        print('{}{}{}'.format(cls.WARNING, message, cls.ENDC))

    @classmethod
    def error(cls, message):
        print('{}{}{}'.format(cls.FAIL, message, cls.ENDC))

class FormatterError(Exception):
    pass

class Formatter(object):
    """Convert file/file as string to DataFrame"""

    columns = ('Location', 'Part', 'Quantity', 'Notes')

    def __call__(self, file_=None, file_as_string=None):
        """When Formatter is called, convert file/file_as_string to DataFrame.
        Args:
            file_(file): BOM as file.
            file_as_string (string): BOM as string.

        Returns:
            df (pd.DataFrame)
        """
        if not (file_ or file_as_string):
            raise FormatterError
        if file_:
            #TODO convert to file_as_string
            pass
        df = self.create_frame(file_as_string)
        return df

    @staticmethod
    def to_list(string, as_string=False):
        #FIXME: too broad, needs to be more specific
        """Return file as long string without spaces or new lines."""
        string_list = string.split(sep=None)
        if as_string:
            return ' '.join(string_list)
        return string_list

    def create_frame(self, file_as_string):
        for list_item in self.to_list(file_as_string):
            print(list_item)
