import json

class RecordUtterance(object):
    openapi_types = {
        'action_url': 'str',
        'silence_timeout_ms': 'int',
        'finish_on_key': 'str',
        'max_length_sec': 'int',
        'play_beep': 'bool',
        'auto_start': 'bool'
    }

    attribute_map = {
        'action_url': 'action_url',
        'silence_timeout_ms': 'silence_timeout_ms',
        'finish_on_key': 'finish_on_key',
        'max_length_sec': 'max_length_sec',
        'play_beep': 'play_beep',
        'auto_start': 'auto_start'
    }

    def __init__(self, action_url, silence_timeout_ms=None, finish_on_key=None, max_length_sec=None, play_beep=None, auto_start=None):
        self._action_url = action_url
        self._silence_timeout_ms = None
        self._finish_on_key = None
        self._max_length_sec = None
        self._play_beep = None
        self._auto_start = None

        if silence_timeout_ms is not None:
            self._silence_timeout_ms = silence_timeout_ms
        if finish_on_key is not None:
            self._finish_on_key = finish_on_key
        if max_length_sec is not None:
            self._max_length_sec = max_length_sec
        if play_beep is not None:
            self._play_beep = play_beep
        if auto_start is not None:
            self._auto_start = auto_start

    @property
    def silence_timeout_ms(self):
        return self._silence_timeout_ms

    @property
    def action_url(self):
        return self._action_url

    @property
    def finish_on_key(self):
        return self._finish_on_key

    @property
    def max_length_sec(self):
        return self._max_length_sec
    
    @property
    def play_beep(self):
        return self._play_beep

    @property
    def auto_start(self):
        return self._auto_start

    @silence_timeout_ms.setter
    def silence_timeout_ms(self, silence_timeout_ms):
        self._silence_timeout_ms = silence_timeout_ms

    @action_url.setter
    def action_url(self, action_url):
        self._action_url = action_url

    @finish_on_key.setter
    def finish_on_key(self, finish_on_key):
        allowed_values = ['1','2','3','4','5','6','7','8','9','0','#', '*']
        if finish_on_key not in allowed_values:
            raise ValueError("finish_on_key must be set to any stringified numeric digit, '#' or '*'. Default value is '#'")
        self._finish_on_key = finish_on_key

    @max_length_sec.setter
    def max_length_sec(self, max_length_sec):
        self._max_length_sec = max_length_sec

    @play_beep.setter
    def play_beep(self, play_beep):
        self._play_beep = play_beep

    @auto_start.setter
    def auto_start(self, auto_start):
        self._auto_start = auto_start

    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'actionUrl': self._action_url,
                'silenceTimeoutMs': self._silence_timeout_ms,
                'finishOnKey': self._finish_on_key,
                'maxLengthSec': self._max_length_sec,
                'playBeep': self._play_beep,
                'autoStart': self._auto_start
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
