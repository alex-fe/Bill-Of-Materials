class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @classmethod
    def success(cls, message):
        print '{}{}{}'.format(cls.OKGREEN, message, cls.ENDC)

    @classmethod
    def warning(cls, message):
        print '{}{}{}'.format(cls.WARNING, message, cls.ENDC)

    @classmethod
    def error(cls, message):
        print '{}{}{}'.format(cls.FAIL, message, cls.ENDC)
