class Reject(object):
    openapi_types = {
        'reason': 'str'
    }

    attribute_map = {
        'reason': 'reason'
    }

    def __init__(self, reason=None):
        self._reason = None

        if reason is not None:
            self._reason = reason

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        self._reason = reason
 
    def to_dict(self):
        """Returns the dictionary representation of reject"""
        as_dict = {
            self.__class__.__name__ : {
                "reason": self._reason
            }
        }
        return as_dict

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
