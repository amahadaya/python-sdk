import json

class Say(object):
    openapi_types = {
        'text': 'str',
        'language': 'str',
        'conference_id': 'str',
        'loop': 'int',
        'enforcePCI': 'bool'
    }

    attribute_map = {
        'text': 'text',
        'language': 'language',
        'conference_id': 'conference_id',
        'loop': 'loop',
        'enforcePCI': 'enforcePCI'
    }

    def __init__(self, text, language=None, loop=None, conference_id=None, enforcePCI=None):
        self._text = text
        self._language = None
        self._loop = None
        self._conference_id = None
        self._enforcePCI = None

        if language is not None:
            self._language = language
        if loop is not None:
            self._loop = loop
        if conference_id is not None:
            self._conference_id = conference_id
        if enforcePCI is not None:
            self._enforcePCI = enforcePCI

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
    def enforcePCI(self):
        return self._enforcePCI

    @text.setter
    def text(self, text):
        self._text = text

    @language.setter
    def language(self, language):
        allowed_values = ['zh-TW', 'zh-HK', 'zh-CN', 'sv-SE', 'ru-RU', 'pt-PT', 'pt-BR', 'pl-PL', 'nl-NL', 'nb-NO', 'ko-KR', 'ja-JP', 'it-IT', 'fr-CA', 'fr-FR', 'fi-FI', 'es-MX', 'es-ES', 'en-US', 'en-IN','en-gb', 'en-CA', 'en-AU', 'de-DE', 'da-DK', 'ca-ES']
        if language not in allowed_values:
            raise ValueError("Language must be set to one of the following values: 'zh-TW', 'zh-HK', 'zh-CN', 'sv-SE', 'ru-RU', 'pt-PT', 'pt-BR', 'pl-PL', 'nl-NL', 'nb-NO', 'ko-KR', 'ja-JP', 'it-IT', 'fr-CA', 'fr-FR', 'fi-FI', 'es-MX', 'es-ES', 'en-US', 'en-IN','en-gb', 'en-CA', 'en-AU', 'de-DE', 'da-DK', 'ca-ES'. Default value is en-US")
        self._language = language
    
    @loop.setter
    def loop(self, loop):
        self._loop = loop
    
    @conference_id.setter
    def conference_id(self, conference_id):
        self._conference_id = conference_id

    @enforcePCI.setter
    def enforcePCI(self, enforcePCI):
        self._enforcePCI = enforcePCI
 
    def to_dict(self):
        """Returns the dictionary representation of say"""
        as_dict = {
            self.__class__.__name__ : {
                "text": self._text,
                "language": self._language,
                "loop": self._loop,
                "conferenceId": self._conference_id,
                "enforcePCI": self._enforcePCI
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
