import json

from freeclimb.percl.language import Language

class Say(object):
    openapi_types = {
        'text': 'str',
        'language': 'str',
        'conference_id': 'str',
        'loop': 'int',
        'enforce_PCI': 'bool'
    }

    attribute_map = {
        'text': 'text',
        'language': 'language',
        'conference_id': 'conference_id',
        'loop': 'loop',
        'enforce_PCI': 'enforce_PCI'
    }

    def __init__(self, text):
        self._text = text
        self._language = Language('en-US')
        self._loop = None
        self._conference_id = None
        self._enforce_PCI = None

    @property
    def text(self):
        return self._text
    
    @property
    def language(self):
        return self._language

    @property
    def loop(self):
        return self._loop
    
    @property
    def conference_id(self):
        return self._conference_id

    @property
    def enforce_PCI(self):
        return self._enforce_PCI

    @text.setter
    def text(self, text):
        self._text = text

    @language.setter
    def language(self, language):
        if(isinstance(language, Language)):
            self._language = language
        else:
            raise ValueError("Language must be set to one of the following values: 'CHINESE_TW', 'CHINESE_HK', 'CHINESE_CN', 'SWEDISH', 'RUSSIAN', 'PORTUGUESE_PT', 'PORTUGUESE_BR', 'POLISH', 'DUTCH', 'NORWEGIAN', 'KOREAN', 'JAPANESE', 'ITALIAN', 'FRENCH_CA', 'FRENCH_FR', 'FINNISH', 'SPANISH_MX', 'SPANISH_ES', 'ENGLISH_US', 'ENGLISH_IN','ENGLISH_GB', 'ENGLISH_CA', 'ENGLISH_AU', 'GERMAN', 'DANISH', 'CATALAN'. Default value is ENGLISH_US")
    
    @loop.setter
    def loop(self, loop):
        self._loop = loop
    
    @conference_id.setter
    def conference_id(self, conference_id):
        self._conference_id = conference_id

    @enforce_PCI.setter
    def enforce_PCI(self, enforce_PCI):
        self._enforce_PCI = enforce_PCI
 
    def to_dict(self):
        """Returns the dictionary representation of say"""
        as_dict = {
            self.__class__.__name__ : {
                "text": self._text,
                "language": self._language.value,
                "loop": self._loop,
                "conference_id": self._conference_id,
                "enforce_PCI": self._enforce_PCI
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
