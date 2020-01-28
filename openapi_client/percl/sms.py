import json

class Sms(object):
    openapi_types = {
        'destination': 'str',
        'messaging_number': 'str',
        'text': 'str',
        'notification_url': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'messaging_number': 'messaging_number',
        'text': 'text',
        'notification_url': 'notification_url'
    }

    def __init__(self, destination, messaging_number, text):
        self._destination = destination
        self._messaging_number = messaging_number
        self._text = text
        self._notification_url = None

    @property
    def destination(self):
        return self._destination
    
    @property
    def messaging_number(self):
        return self._messaging_number

    @property
    def notification_url(self):
        return self._notification_url
    
    @property
    def text(self):
        return self._text

    @destination.setter
    def destination(self, destination):
        self._destination = destination

    @messaging_number.setter
    def messaging_number(self, messaging_number):
        self._messaging_number = messaging_number
    
    @notification_url.setter
    def notification_url(self, notification_url):
        self._notification_url = notification_url
    
    @text.setter
    def text(self, text):
        self._text = text
 
    def to_dict(self):
        """Returns the json representation of sms"""
        as_dict = {
            self.__class__.__name__ : {
                "destination": self._destination,
                "messaging_number": self._messaging_number,
                "notification_url": self._notification_url,
                "text": self._text 
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
