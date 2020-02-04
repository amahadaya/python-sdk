import json

from freeclimb.percl.out_dial_if_machine import OutDialIfMachine

class OutDial(object):
    openapi_types = {
        'destination': 'str',
        'calling_number': 'str',
        'action_url': 'str',
        'call_connect_url': 'str',
        'send_digits': 'str',
        'timeout': 'int',
        'if_machine': 'str',
        'if_machine_url': 'str',
        'status_callback_url': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'calling_number': 'calling_number',
        'action_url': 'action_url',
        'call_connect_url': 'call_connect_url',
        'send_digits': 'send_digits',
        'timeout': 'timeout',
        'if_machine': 'if_machine',
        'if_machine_url': 'if_machine_url',
        'status_callback_url': 'status_callback_url'
    }

    def __init__(self, destination, calling_number, action_url, call_connect_url):
        self._destination = destination
        self._calling_number = calling_number
        self._action_url = action_url
        self._call_connect_url = call_connect_url
        self._send_digits = None
        self._timeout = None
        self._if_machine = None
        self._if_machine_url = None
        self._status_callback_url = None

    @property
    def destination(self):
        return self._destination

    @property
    def calling_number(self):
        return self._calling_number

    @property
    def action_url(self):
        return self._action_url

    @property
    def call_connect_url(self):
        return self._call_connect_url

    @property
    def send_digits(self):
        return self._send_digits
    
    @property
    def timeout(self):
        return self._timeout

    @property
    def if_machine(self):
        return self._if_machine
 
    @property
    def if_machine_url(self):
        return self._if_machine_url

    @property
    def status_callback_url(self):
        return self._status_callback_url

    @destination.setter
    def destination(self, destination):
        self._destination = destination

    @calling_number.setter
    def calling_number(self, calling_number):
        self._calling_number = calling_number

    @action_url.setter
    def action_url(self, action_url):
        self._action_url = action_url

    @call_connect_url.setter
    def call_connect_url(self, call_connect_url):
        self._call_connect_url = call_connect_url

    @send_digits.setter
    def send_digits(self, send_digits):
        self._send_digits = send_digits

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout

    @if_machine.setter
    def if_machine(self, if_machine):
        if(isinstance(if_machine, OutDialIfMachine)):
            self._if_machine = if_machine
        else:
            raise ValueError("if_machine must be an OutDialIfMachine PerCL object set to one of the following values: 'redirect' or 'hangup'. Default value is null.")

    @if_machine_url.setter
    def if_machine_url(self, if_machine_url):
        self._if_machine_url = if_machine_url

    @status_callback_url.setter
    def status_callback_url(self, status_callback_url):
        self._status_callback_url = status_callback_url

    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'destination': self._destination,
                'calling_number': self._calling_number,
                'action_url': self._action_url,
                'call_connect_url': self._call_connect_url,
                'send_digits': self._send_digits,
                'timeout': self._timeout,
                'if_machine': (self._if_machine.value if(isinstance(self._if_machine, OutDialIfMachine)) else None),
                'if_machine_url': self._if_machine_url,
                'status_callback_url': self._status_callback_url
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
