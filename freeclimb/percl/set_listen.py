import json

class SetListen(object):
    openapi_types = {
        'call_id': 'str',
        'listen': 'bool'
    }

    attribute_map = {
        'call_id': 'call_id',
        'listen': 'listen'
    }

    def __init__(self, call_id, listen=None):
        self._call_id = call_id
        self._listen = None

        if listen is not None:
            self._listen = listen

    @property
    def call_id(self):
        return self._call_id
    
    @property
    def listen(self):
        return self._listen

    @call_id.setter
    def call_id(self, call_id):
        self._call_id = call_id

    @listen.setter
    def listen(self, listen):
        self._listen = listen
 
    def to_dict(self):
        """Returns the dictionary representation of set_listen"""
        as_dict = {
            self.__class__.__name__ : {
                "callId": self._call_id,
                "listen": self._listen
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
