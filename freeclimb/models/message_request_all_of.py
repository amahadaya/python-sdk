# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from freeclimb.configuration import Configuration


class MessageRequestAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        '_from': 'str',
        'to': 'str',
        'text': 'str',
        'notification_url': 'str',
        'request_id': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'text': 'text',
        'notification_url': 'notificationUrl',
        'request_id': 'requestId',
        'account_id': 'accountId'
    }

    def __init__(self, _from=None, to=None, text=None, notification_url=None, request_id=None, account_id=None, local_vars_configuration=None):  # noqa: E501
        """MessageRequestAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__from = None
        self._to = None
        self._text = None
        self._notification_url = None
        self._request_id = None
        self._account_id = None
        self.discriminator = None

        self._from = _from
        self.to = to
        self.text = text
        if notification_url is not None:
            self.notification_url = notification_url
        if request_id is not None:
            self.request_id = request_id
        if account_id is not None:
            self.account_id = account_id

    @property
    def _from(self):
        """Gets the _from of this MessageRequestAllOf.  # noqa: E501

        Phone number to use as the sender. This must be an incoming phone number that you have purchased from FreeClimb.  # noqa: E501

        :return: The _from of this MessageRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this MessageRequestAllOf.

        Phone number to use as the sender. This must be an incoming phone number that you have purchased from FreeClimb.  # noqa: E501

        :param _from: The _from of this MessageRequestAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this MessageRequestAllOf.  # noqa: E501

        Phone number to receive the message. Must be within FreeClimb's service area.  # noqa: E501

        :return: The to of this MessageRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this MessageRequestAllOf.

        Phone number to receive the message. Must be within FreeClimb's service area.  # noqa: E501

        :param to: The to of this MessageRequestAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def text(self):
        """Gets the text of this MessageRequestAllOf.  # noqa: E501

        Text contained in the message (maximum 160 characters).   **Note:** For text, only ASCII characters are supported.  # noqa: E501

        :return: The text of this MessageRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this MessageRequestAllOf.

        Text contained in the message (maximum 160 characters).   **Note:** For text, only ASCII characters are supported.  # noqa: E501

        :param text: The text of this MessageRequestAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def notification_url(self):
        """Gets the notification_url of this MessageRequestAllOf.  # noqa: E501

        When the Message changes status, this URL is invoked using HTTP POST with the messageStatus parameters.  **Note:** This is a notification only; any PerCL returned is ignored.  # noqa: E501

        :return: The notification_url of this MessageRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._notification_url

    @notification_url.setter
    def notification_url(self, notification_url):
        """Sets the notification_url of this MessageRequestAllOf.

        When the Message changes status, this URL is invoked using HTTP POST with the messageStatus parameters.  **Note:** This is a notification only; any PerCL returned is ignored.  # noqa: E501

        :param notification_url: The notification_url of this MessageRequestAllOf.  # noqa: E501
        :type: str
        """

        self._notification_url = notification_url

    @property
    def request_id(self):
        """Gets the request_id of this MessageRequestAllOf.  # noqa: E501

        RequestId for this request, starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response (e.g., X-Pulse-Request-Id: <requestId>).  # noqa: E501

        :return: The request_id of this MessageRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this MessageRequestAllOf.

        RequestId for this request, starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response (e.g., X-Pulse-Request-Id: <requestId>).  # noqa: E501

        :param request_id: The request_id of this MessageRequestAllOf.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def account_id(self):
        """Gets the account_id of this MessageRequestAllOf.  # noqa: E501

        String that uniquely identifies this account resource.  # noqa: E501

        :return: The account_id of this MessageRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this MessageRequestAllOf.

        String that uniquely identifies this account resource.  # noqa: E501

        :param account_id: The account_id of this MessageRequestAllOf.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.to_camel_case(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif value is None:
                continue
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MessageRequestAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageRequestAllOf):
            return True

        return self.to_dict() != other.to_dict()

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
