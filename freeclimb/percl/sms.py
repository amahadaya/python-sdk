import json

class Sms(object):
    openapi_types = {
        'to': 'str',
        'from_number': 'str',
        'text': 'str',
        'notification_url': 'str'
    }

    attribute_map = {
        'to': 'to',
        'from_number': 'from_number',
        'text': 'text',
        'notification_url': 'notification_url'
    }

    def __init__(self, to, from_number, text, notification_url=None):
        self._to = to
        self._from_number = from_number
        self._text = text
        self._notification_url = None

        if notification_url is not None:
            self._notification_url = notification_url

    @property
    def to(self):
        return self._to
    
    @property
    def from_number(self):
        return self._from_number

    @property
    def notification_url(self):
        return self._notification_url
    
    @property
    def text(self):
        return self._text

    @to.setter
    def to(self, to):
        self._to = to

    @from_number.setter
    def from_number(self, from_number):
        self._from_number = from_number
    
    @notification_url.setter
    def notification_url(self, notification_url):
        self._notification_url = notification_url
    
    @text.setter
    def text(self, text):
        self._text = text
 
    def to_dict(self):
        """Returns the dictionary representation of sms"""
        as_dict = {
            self.__class__.__name__ : {
                "from": self._from_number,
                "to": self._to,
                "text": self._text,
                "notificationUrl": self._notification_url 
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
