class Environment:
    """ names of keys used in os.environ """
    BASE_PATH = 'BASE_PATH'


class Values:
    """ general values """
    BASE_FOLDER_NAME = 'python-framework-styling'


class GcpLoggerFormat:
    """ values related to formatting gcp logger """
    LOGGER_FORMAT = '{"severity": "%(levelname)s", "message": "%(message)s", "payload": %(payload)s}'
    LOGGER_NAME_FORMAT = '{}: {}'
    UNNAMED = 'UNNAMED'


# examples
class FruitColor:
    YELLOW = 'YELLOW'
    BLUE = 'BLUE'
    RED = 'RED'


class FruitSize:
    BIG = 'BIG'
    SMALL = 'SMALL'


class BananaDefaults:
    COLOR = FruitColor.YELLOW
    SIZE = FruitSize.BIG


class BerryDefaults:
    COLOR = FruitColor.RED
    SIZE = FruitSize.SMALL
