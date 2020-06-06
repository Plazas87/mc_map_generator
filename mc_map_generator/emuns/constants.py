from enum import Enum


class Extensions(Enum):
    FILE_EXTENSION_CSV = '.csv'
    FILE_EXTENSION_JSON = '.json'


class Separators(Enum):
    COMMA_SEPARATED_VALUES = ','
    SEMI_COLON = ';'


class Encodings(Enum):
    ENCODING_ISO8859_1 = 'iso-8859-1'
    ENCODING_UTF8 = 'utf-8'
    ENCODING_LATIN_1 = 'latin1'

