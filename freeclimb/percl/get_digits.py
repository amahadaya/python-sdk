import json

class GetDigits(object):
    openapi_types = {
        'action_url': 'str',
        'initial_timeout_ms': 'int',
        'digit_timeout_ms': 'str',
        'finish_on_key': 'str',
        'min_digits': 'int',
        'max_digits': 'int',
        'flush_buffer': 'bool',
        'prompts': 'array',
        'enforcePCI': 'bool'
    }

    attribute_map = {
        'action_url': 'action_url',
        'initial_timeout_ms': 'initial_timeout_ms',
        'digit_timeout_ms': 'digit_timeout_ms',
        'finish_on_key': 'finish_on_key',
        'min_digits': 'min_digits',
        'max_digits': 'max_digits',
        'flush_buffer': 'flush_buffer',
        'prompts': 'prompts',
        'enforcePCI': 'enforcePCI'
    }

    def __init__(self, action_url, initial_timeout_ms=None, digit_timeout_ms=None, finish_on_key=None, min_digits=None, max_digits=None, flush_buffer=None, prompts=None, enforcePCI=None):
        self._action_url = action_url
        self._initial_timeout_ms = None
        self._digit_timeout_ms = None
        self._finish_on_key = None
        self._min_digits = None
        self._max_digits = None
        self._flush_buffer = None
        self._prompts = None
        self._enforcePCI = None

        if initial_timeout_ms is not None:
            self._initial_timeout_ms = initial_timeout_ms
        if digit_timeout_ms is not None:
            self._digit_timeout_ms = digit_timeout_ms
        if finish_on_key is not None:
            self._finish_on_key = finish_on_key
        if min_digits is not None:
            self._min_digits = min_digits
        if max_digits is not None:
            self._max_digits = max_digits
        if flush_buffer is not None:
            self._flush_buffer = flush_buffer
        if prompts is not None:
            self._prompts = [prompts]
        if enforcePCI is not None:
            self._enforcePCI = enforcePCI

    @property
    def initial_timeout_ms(self):
        return self._initial_timeout_ms

    @property
    def digit_timeout_ms(self):
        return self._digit_timeout_ms

    @property
    def action_url(self):
        return self._action_url

    @property
    def finish_on_key(self):
        return self._finish_on_key

    @property
    def min_digits(self):
        return self._min_digits
    
    @property
    def max_digits(self):
        return self._max_digits

    @property
    def flush_buffer(self):
        return self._flush_buffer
 
    @property
    def prompts(self):
        return self._prompts

    @property
    def enforcePCI(self):
        return self._enforcePCI

    @initial_timeout_ms.setter
    def initial_timeout_ms(self, initial_timeout_ms):
        self._initial_timeout_ms = initial_timeout_ms

    @digit_timeout_ms.setter
    def digit_timeout_ms(self, digit_timeout_ms):
        self._digit_timeout_ms = digit_timeout_ms

    @action_url.setter
    def action_url(self, action_url):
        self._action_url = action_url

    @finish_on_key.setter
    def finish_on_key(self, finish_on_key):
        allowed_values = ['1','2','3','4','5','6','7','8','9','0','#', '*']
        if finish_on_key not in allowed_values:
            raise ValueError("finish_on_key must be set to any stringified numeric digit, '#' or '*'. Default value is '#'")
        self._finish_on_key = finish_on_key

    @min_digits.setter
    def min_digits(self, min_digits):
        self._min_digits = min_digits

    @max_digits.setter
    def max_digits(self, max_digits):
        self._max_digits = max_digits

    @flush_buffer.setter
    def flush_buffer(self, flush_buffer):
        self._flush_buffer = flush_buffer

    @prompts.setter
    def prompts(self, prompts):
        self._prompts = [prompts]

    @prompts.setter
    def enforcePCI(self, enforcePCI):
        self._enforcePCI = enforcePCI

    def to_dict(self):
        as_dict = {
            self.__class__.__name__ : {
                'actionUrl': self._action_url,
                'initialTimeoutMs': self._initial_timeout_ms,
                'digitTimeoutMs': self._digit_timeout_ms,
                'finishOnKey': self._finish_on_key,
                'minDigits': self._min_digits,
                'maxDigits': self._max_digits,
                'flushBuffer': self._flush_buffer,
                'prompts': self._prompts,
                'enforcePCI': self._enforcePCI
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
