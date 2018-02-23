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

class FormattingError(Exception):
    pass

class Formatter(object):
    """Convert file/file as string to DataFrame"""

    columns = ('Location', 'Part', 'Quantity')

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
        #TODO: too broad, needs to be more specific
        """Return file as long string without spaces or new lines."""
        string_list = string.split(sep=None)
        if as_string:
            return ' '.join(string_list)
        return string_list

    @classmethod
    def create_frame(cls, file_as_string):
        """From the contents of a file, convert to DataFrame.
        Args:
            file_as_string (str): Contents of a file in string format.

        Returns:
            Populated DataFrame.
        """
        # TODO: More pythonic/pandas way
        file_as_list = cls.to_list(file_as_string)
        df = pd.DataFrame(
            columns=cls.columns, index=range(len(file_as_list) // 3)
        )
        row_counter = 0
        for i, list_item in enumerate(file_as_list):
            index = i % len(cls.columns)
            df.iat[row_counter, index] = list_item
            if index == 2:
                row_counter += 1
        return df
