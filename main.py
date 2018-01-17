import requests

from bs4 import BeautifulSoup


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


def get_site():
    """
    Get site from user and validate.
    Returns:
        Validated url.
    """
    while True:
        site = raw_input('Enter url with BOM on page: ')
        try:
            request = requests.get(site)
        except requests.exceptions.MissingSchema, err:
            Colors.error(err)
        else:
            if request.status_code == 200:
                break
    Colors.success('Url validated')
    return site


if __name__ == '__main__':
    site = get_site()
