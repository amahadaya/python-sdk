# coding: utf-8

# flake8: noqa

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "3.0.0"

# import apis into sdk package
from freeclimb.api.default_api import DefaultApi

# import ApiClient
from freeclimb.api_client import ApiClient
from freeclimb.configuration import Configuration
from freeclimb.exceptions import OpenApiException
from freeclimb.exceptions import ApiTypeError
from freeclimb.exceptions import ApiValueError
from freeclimb.exceptions import ApiKeyError
from freeclimb.exceptions import ApiException
from freeclimb.utils import Utils
# import models into sdk package
from freeclimb.models.account_request import AccountRequest
from freeclimb.models.account_result import AccountResult
from freeclimb.models.account_result_all_of import AccountResultAllOf
from freeclimb.models.add_to_conference import AddToConference
from freeclimb.models.add_to_conference_all_of import AddToConferenceAllOf
from freeclimb.models.application_list import ApplicationList
from freeclimb.models.application_list_all_of import ApplicationListAllOf
from freeclimb.models.application_request import ApplicationRequest
from freeclimb.models.application_result import ApplicationResult
from freeclimb.models.application_result_all_of import ApplicationResultAllOf
from freeclimb.models.available_number import AvailableNumber
from freeclimb.models.available_number_list import AvailableNumberList
from freeclimb.models.available_number_list_all_of import AvailableNumberListAllOf
from freeclimb.models.buy_incoming_number_request import BuyIncomingNumberRequest
from freeclimb.models.call_list import CallList
from freeclimb.models.call_list_all_of import CallListAllOf
from freeclimb.models.call_result import CallResult
from freeclimb.models.call_result_all_of import CallResultAllOf
from freeclimb.models.conference_list import ConferenceList
from freeclimb.models.conference_list_all_of import ConferenceListAllOf
from freeclimb.models.conference_participant_list import ConferenceParticipantList
from freeclimb.models.conference_participant_list_all_of import ConferenceParticipantListAllOf
from freeclimb.models.conference_participant_result import ConferenceParticipantResult
from freeclimb.models.conference_participant_result_all_of import ConferenceParticipantResultAllOf
from freeclimb.models.conference_result import ConferenceResult
from freeclimb.models.conference_result_all_of import ConferenceResultAllOf
from freeclimb.models.create_conference import CreateConference
from freeclimb.models.create_conference_all_of import CreateConferenceAllOf
from freeclimb.models.create_conference_request import CreateConferenceRequest
from freeclimb.models.dequeue import Dequeue
from freeclimb.models.enqueue import Enqueue
from freeclimb.models.enqueue_all_of import EnqueueAllOf
from freeclimb.models.filter_logs_request import FilterLogsRequest
from freeclimb.models.get_digits import GetDigits
from freeclimb.models.get_digits_all_of import GetDigitsAllOf
from freeclimb.models.get_speech import GetSpeech
from freeclimb.models.get_speech_all_of import GetSpeechAllOf
from freeclimb.models.hangup import Hangup
from freeclimb.models.hangup_all_of import HangupAllOf
from freeclimb.models.incoming_number_list import IncomingNumberList
from freeclimb.models.incoming_number_list_all_of import IncomingNumberListAllOf
from freeclimb.models.incoming_number_request import IncomingNumberRequest
from freeclimb.models.incoming_number_result import IncomingNumberResult
from freeclimb.models.incoming_number_result_all_of import IncomingNumberResultAllOf
from freeclimb.models.log_list import LogList
from freeclimb.models.log_list_all_of import LogListAllOf
from freeclimb.models.log_result import LogResult
from freeclimb.models.make_call_request import MakeCallRequest
from freeclimb.models.message_request import MessageRequest
from freeclimb.models.message_request_all_of import MessageRequestAllOf
from freeclimb.models.message_result import MessageResult
from freeclimb.models.message_result_all_of import MessageResultAllOf
from freeclimb.models.messages_list import MessagesList
from freeclimb.models.messages_list_all_of import MessagesListAllOf
from freeclimb.models.mutable_resource_model import MutableResourceModel
from freeclimb.models.out_dial import OutDial
from freeclimb.models.out_dial_all_of import OutDialAllOf
from freeclimb.models.pagination_model import PaginationModel
from freeclimb.models.pause import Pause
from freeclimb.models.pause_all_of import PauseAllOf
from freeclimb.models.percl_command import PerclCommand
from freeclimb.models.percl_script import PerclScript
from freeclimb.models.play import Play
from freeclimb.models.play_all_of import PlayAllOf
from freeclimb.models.play_early_media import PlayEarlyMedia
from freeclimb.models.play_early_media_all_of import PlayEarlyMediaAllOf
from freeclimb.models.queue_list import QueueList
from freeclimb.models.queue_list_all_of import QueueListAllOf
from freeclimb.models.queue_member import QueueMember
from freeclimb.models.queue_member_list import QueueMemberList
from freeclimb.models.queue_member_list_all_of import QueueMemberListAllOf
from freeclimb.models.queue_request import QueueRequest
from freeclimb.models.queue_result import QueueResult
from freeclimb.models.queue_result_all_of import QueueResultAllOf
from freeclimb.models.record_utterance import RecordUtterance
from freeclimb.models.record_utterance_all_of import RecordUtteranceAllOf
from freeclimb.models.recording_list import RecordingList
from freeclimb.models.recording_list_all_of import RecordingListAllOf
from freeclimb.models.recording_result import RecordingResult
from freeclimb.models.recording_result_all_of import RecordingResultAllOf
from freeclimb.models.redirect import Redirect
from freeclimb.models.redirect_all_of import RedirectAllOf
from freeclimb.models.reject import Reject
from freeclimb.models.reject_all_of import RejectAllOf
from freeclimb.models.remove_from_conference import RemoveFromConference
from freeclimb.models.remove_from_conference_all_of import RemoveFromConferenceAllOf
from freeclimb.models.say import Say
from freeclimb.models.say_all_of import SayAllOf
from freeclimb.models.send_digits import SendDigits
from freeclimb.models.send_digits_all_of import SendDigitsAllOf
from freeclimb.models.set_listen import SetListen
from freeclimb.models.set_listen_all_of import SetListenAllOf
from freeclimb.models.set_talk import SetTalk
from freeclimb.models.set_talk_all_of import SetTalkAllOf
from freeclimb.models.sms import Sms
from freeclimb.models.sms_all_of import SmsAllOf
from freeclimb.models.start_record_call import StartRecordCall
from freeclimb.models.terminate_conference import TerminateConference
from freeclimb.models.terminate_conference_all_of import TerminateConferenceAllOf
from freeclimb.models.update_call_request import UpdateCallRequest
from freeclimb.models.update_conference_participant_request import UpdateConferenceParticipantRequest
from freeclimb.models.update_conference_request import UpdateConferenceRequest


import json

def serialize_command_list(percl_list):
    percl_array = []
    for command in percl_list:
        class_name = type(command).__name__
        if hasattr(command, 'prompts'):
            percl_command = {
                class_name: serialize_prompts_command(command)
            }
        else:
            percl_command = {
                class_name: command.to_dict()
            }
        percl_array.append(percl_command)
    return percl_array


def serialize_prompts_command(command):
    prompts = command.prompts
    command.prompts = None
    percl_dict = command.to_dict()
    percl_dict['prompts'] = serialize_command_list(prompts)
    return percl_dict
    


def percl_to_json(percl_script):
    return json.dumps(serialize_command_list(percl_script.commands))
