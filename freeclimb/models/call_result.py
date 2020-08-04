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


class CallResult(object):
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
        'uri': 'str',
        'date_created': 'str',
        'date_updated': 'str',
        'revision': 'int',
        'call_id': 'str',
        'parent_call_id': 'str',
        'account_id': 'str',
        '_from': 'str',
        'to': 'str',
        'phone_number_id': 'str',
        'status': 'str',
        'start_time': 'str',
        'connect_time': 'str',
        'end_time': 'str',
        'duration': 'int',
        'connect_duration': 'int',
        'direction': 'str',
        'answered_by': 'str',
        'subresource_uris': 'object'
    }

    attribute_map = {
        'uri': 'uri',
        'date_created': 'dateCreated',
        'date_updated': 'dateUpdated',
        'revision': 'revision',
        'call_id': 'callId',
        'parent_call_id': 'parentCallId',
        'account_id': 'accountId',
        '_from': 'from',
        'to': 'to',
        'phone_number_id': 'phoneNumberId',
        'status': 'status',
        'start_time': 'startTime',
        'connect_time': 'connectTime',
        'end_time': 'endTime',
        'duration': 'duration',
        'connect_duration': 'connectDuration',
        'direction': 'direction',
        'answered_by': 'answeredBy',
        'subresource_uris': 'subresourceUris'
    }

    def __init__(self, uri=None, date_created=None, date_updated=None, revision=None, call_id=None, parent_call_id=None, account_id=None, _from=None, to=None, phone_number_id=None, status=None, start_time=None, connect_time=None, end_time=None, duration=None, connect_duration=None, direction=None, answered_by=None, subresource_uris=None, local_vars_configuration=None):  # noqa: E501
        """CallResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uri = None
        self._date_created = None
        self._date_updated = None
        self._revision = None
        self._call_id = None
        self._parent_call_id = None
        self._account_id = None
        self.__from = None
        self._to = None
        self._phone_number_id = None
        self._status = None
        self._start_time = None
        self._connect_time = None
        self._end_time = None
        self._duration = None
        self._connect_duration = None
        self._direction = None
        self._answered_by = None
        self._subresource_uris = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if date_created is not None:
            self.date_created = date_created
        if date_updated is not None:
            self.date_updated = date_updated
        if revision is not None:
            self.revision = revision
        if call_id is not None:
            self.call_id = call_id
        if parent_call_id is not None:
            self.parent_call_id = parent_call_id
        if account_id is not None:
            self.account_id = account_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if phone_number_id is not None:
            self.phone_number_id = phone_number_id
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if connect_time is not None:
            self.connect_time = connect_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if connect_duration is not None:
            self.connect_duration = connect_duration
        if direction is not None:
            self.direction = direction
        if answered_by is not None:
            self.answered_by = answered_by
        if subresource_uris is not None:
            self.subresource_uris = subresource_uris

    @property
    def uri(self):
        """Gets the uri of this CallResult.  # noqa: E501

        The URI for this resource, relative to /apiserver.  # noqa: E501

        :return: The uri of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CallResult.

        The URI for this resource, relative to /apiserver.  # noqa: E501

        :param uri: The uri of this CallResult.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def date_created(self):
        """Gets the date_created of this CallResult.  # noqa: E501

        The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :return: The date_created of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this CallResult.

        The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :param date_created: The date_created of this CallResult.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this CallResult.  # noqa: E501

        The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :return: The date_updated of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this CallResult.

        The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :param date_updated: The date_updated of this CallResult.  # noqa: E501
        :type: str
        """

        self._date_updated = date_updated

    @property
    def revision(self):
        """Gets the revision of this CallResult.  # noqa: E501

        Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.  # noqa: E501

        :return: The revision of this CallResult.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this CallResult.

        Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.  # noqa: E501

        :param revision: The revision of this CallResult.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def call_id(self):
        """Gets the call_id of this CallResult.  # noqa: E501

        String that uniquely identifies this Call resource.  # noqa: E501

        :return: The call_id of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._call_id

    @call_id.setter
    def call_id(self, call_id):
        """Sets the call_id of this CallResult.

        String that uniquely identifies this Call resource.  # noqa: E501

        :param call_id: The call_id of this CallResult.  # noqa: E501
        :type: str
        """

        self._call_id = call_id

    @property
    def parent_call_id(self):
        """Gets the parent_call_id of this CallResult.  # noqa: E501

        ID of the Call that created this leg (child Call).  # noqa: E501

        :return: The parent_call_id of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._parent_call_id

    @parent_call_id.setter
    def parent_call_id(self, parent_call_id):
        """Sets the parent_call_id of this CallResult.

        ID of the Call that created this leg (child Call).  # noqa: E501

        :param parent_call_id: The parent_call_id of this CallResult.  # noqa: E501
        :type: str
        """

        self._parent_call_id = parent_call_id

    @property
    def account_id(self):
        """Gets the account_id of this CallResult.  # noqa: E501

        ID of the account that owns this Call.  # noqa: E501

        :return: The account_id of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CallResult.

        ID of the account that owns this Call.  # noqa: E501

        :param account_id: The account_id of this CallResult.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def _from(self):
        """Gets the _from of this CallResult.  # noqa: E501

        Phone number that initiated this Call.  # noqa: E501

        :return: The _from of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this CallResult.

        Phone number that initiated this Call.  # noqa: E501

        :param _from: The _from of this CallResult.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this CallResult.  # noqa: E501

        Phone number that received this Call.  # noqa: E501

        :return: The to of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this CallResult.

        Phone number that received this Call.  # noqa: E501

        :param to: The to of this CallResult.  # noqa: E501
        :type: str
        """

        self._to = to

    @property
    def phone_number_id(self):
        """Gets the phone_number_id of this CallResult.  # noqa: E501

        If the Call was inbound, this is the ID of the IncomingPhoneNumber that received the Call (DNIS). If the Call was outbound, this is the ID of the phone number from which the Call was placed (ANI).  # noqa: E501

        :return: The phone_number_id of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_id

    @phone_number_id.setter
    def phone_number_id(self, phone_number_id):
        """Sets the phone_number_id of this CallResult.

        If the Call was inbound, this is the ID of the IncomingPhoneNumber that received the Call (DNIS). If the Call was outbound, this is the ID of the phone number from which the Call was placed (ANI).  # noqa: E501

        :param phone_number_id: The phone_number_id of this CallResult.  # noqa: E501
        :type: str
        """

        self._phone_number_id = phone_number_id

    @property
    def status(self):
        """Gets the status of this CallResult.  # noqa: E501

        * `queued` &ndash; Call is ready and waiting in line before going out. * `ringing` &ndash; Call is currently ringing. * `inProgress` &ndash; Call was answered and is currently in progress. * `canceled` &ndash; Call was hung up while it was queued or ringing. * `completed` &ndash; Call was answered and has ended normally. * `busy` &ndash; Caller received a busy signal. * `failed` &ndash; Call could not be completed as dialed, most likely because the phone number was non-existent. * `noAnswer` &ndash; Call ended without being answered.  # noqa: E501

        :return: The status of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CallResult.

        * `queued` &ndash; Call is ready and waiting in line before going out. * `ringing` &ndash; Call is currently ringing. * `inProgress` &ndash; Call was answered and is currently in progress. * `canceled` &ndash; Call was hung up while it was queued or ringing. * `completed` &ndash; Call was answered and has ended normally. * `busy` &ndash; Caller received a busy signal. * `failed` &ndash; Call could not be completed as dialed, most likely because the phone number was non-existent. * `noAnswer` &ndash; Call ended without being answered.  # noqa: E501

        :param status: The status of this CallResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["queued", "ringing", "inProgress", "canceled", "completed", "busy", "failed", "noAnswer"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this CallResult.  # noqa: E501

        Start time of the Call (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call has not yet been dialed.  # noqa: E501

        :return: The start_time of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CallResult.

        Start time of the Call (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call has not yet been dialed.  # noqa: E501

        :param start_time: The start_time of this CallResult.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def connect_time(self):
        """Gets the connect_time of this CallResult.  # noqa: E501

        Time the Call was answered (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call has not yet been dialed.  # noqa: E501

        :return: The connect_time of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._connect_time

    @connect_time.setter
    def connect_time(self, connect_time):
        """Sets the connect_time of this CallResult.

        Time the Call was answered (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call has not yet been dialed.  # noqa: E501

        :param connect_time: The connect_time of this CallResult.  # noqa: E501
        :type: str
        """

        self._connect_time = connect_time

    @property
    def end_time(self):
        """Gets the end_time of this CallResult.  # noqa: E501

        End time of the Call (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call did not complete successfully.  # noqa: E501

        :return: The end_time of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CallResult.

        End time of the Call (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call did not complete successfully.  # noqa: E501

        :param end_time: The end_time of this CallResult.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def duration(self):
        """Gets the duration of this CallResult.  # noqa: E501

        Total length of the Call in seconds. Measures time between startTime and endTime. This value is empty for busy, failed, unanswered or ongoing Calls.  # noqa: E501

        :return: The duration of this CallResult.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this CallResult.

        Total length of the Call in seconds. Measures time between startTime and endTime. This value is empty for busy, failed, unanswered or ongoing Calls.  # noqa: E501

        :param duration: The duration of this CallResult.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def connect_duration(self):
        """Gets the connect_duration of this CallResult.  # noqa: E501

        Length of time that the Call was connected in seconds. Measures time between connectTime and endTime. This value is empty for busy, failed, unanswered or ongoing Calls.  # noqa: E501

        :return: The connect_duration of this CallResult.  # noqa: E501
        :rtype: int
        """
        return self._connect_duration

    @connect_duration.setter
    def connect_duration(self, connect_duration):
        """Sets the connect_duration of this CallResult.

        Length of time that the Call was connected in seconds. Measures time between connectTime and endTime. This value is empty for busy, failed, unanswered or ongoing Calls.  # noqa: E501

        :param connect_duration: The connect_duration of this CallResult.  # noqa: E501
        :type: int
        """

        self._connect_duration = connect_duration

    @property
    def direction(self):
        """Gets the direction of this CallResult.  # noqa: E501

        Direction of the Call. `inbound` for Calls into FreeClimb, `outboundAPI` for Calls initiated via the REST API,  `outboundDial` for Calls initiated by the `OutDial` PerCL command.  # noqa: E501

        :return: The direction of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this CallResult.

        Direction of the Call. `inbound` for Calls into FreeClimb, `outboundAPI` for Calls initiated via the REST API,  `outboundDial` for Calls initiated by the `OutDial` PerCL command.  # noqa: E501

        :param direction: The direction of this CallResult.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def answered_by(self):
        """Gets the answered_by of this CallResult.  # noqa: E501

        If this Call was initiated with answering machine detection, either `human` or `machine`. Empty otherwise.  # noqa: E501

        :return: The answered_by of this CallResult.  # noqa: E501
        :rtype: str
        """
        return self._answered_by

    @answered_by.setter
    def answered_by(self, answered_by):
        """Sets the answered_by of this CallResult.

        If this Call was initiated with answering machine detection, either `human` or `machine`. Empty otherwise.  # noqa: E501

        :param answered_by: The answered_by of this CallResult.  # noqa: E501
        :type: str
        """

        self._answered_by = answered_by

    @property
    def subresource_uris(self):
        """Gets the subresource_uris of this CallResult.  # noqa: E501

        The list of subresources for this Call. These include things like logs and recordings associated with the Call.  # noqa: E501

        :return: The subresource_uris of this CallResult.  # noqa: E501
        :rtype: object
        """
        return self._subresource_uris

    @subresource_uris.setter
    def subresource_uris(self, subresource_uris):
        """Sets the subresource_uris of this CallResult.

        The list of subresources for this Call. These include things like logs and recordings associated with the Call.  # noqa: E501

        :param subresource_uris: The subresource_uris of this CallResult.  # noqa: E501
        :type: object
        """

        self._subresource_uris = subresource_uris

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
        if not isinstance(other, CallResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CallResult):
            return True

        return self.to_dict() != other.to_dict()

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
