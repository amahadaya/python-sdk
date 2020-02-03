# coding: utf-8

"""
    FreeClimb API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import mock

import freeclimb
from freeclimb.api.default_api import DefaultApi  # noqa: E501
from freeclimb.rest import ApiException
import pprint


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = freeclimb.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_buy_a_phone_number(self):
        """Test case for buy_a_phone_number

        Buy a Phone Number  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:

            buy_incoming_number_request = freeclimb.BuyIncomingNumberRequest('+12345678900')
            self.test_buy_a_phone_number_response = self.api.buy_a_phone_number('ACCOUNT_ID', buy_incoming_number_request=buy_incoming_number_request)

            mock_method.assert_called_once()
            # TODO: Fails because actual result has newlines in dictionary and the following removes the newlines
            # mock_method.assert_called_once_with(
            #     '/Accounts/{accountId}/IncomingPhoneNumbers',
            #     'POST',
            #     {'accountId': 'ACCOUNT_ID'},
            #     [],
            #     {'Accept': 'application/json', 'Content-Type': 'application/json'},
            #     _preload_content=True,
            #     _request_timeout=None,
            #     _return_http_data_only=True, async_req=None, auth_settings=['fc'], body={'alias': None,
            #         'application_id': None,
            #         'phone_number': '+12345678900',
            #         'request_id': None},
            #     collection_formats={},
            #     files={},
            #     post_params=[],
            #     response_type='IncomingNumberResult'
            # )

    def test_create_a_conference(self):
        """Test case for create_a_conference

        Create a Conference  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            create_conference_request = freeclimb.CreateConferenceRequest('http://localhost:80')
            self.test_create_a_conference_response = self.api.create_a_conference('ACCOUNT_ID', create_conference_request=create_conference_request)

            mock_method.assert_called_once()

    def test_create_a_queue(self):
        """Test case for create_a_queue

        Create a Queue  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_create_a_queue_response = self.api.create_a_queue('ACCOUNT_ID', queue_request=freeclimb.QueueRequest())

            mock_method.assert_called_once()

    def test_create_an_application(self):
        """Test case for create_an_application

        Create an application  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_create_an_application = self.api.create_an_application('ACCOUNT_ID', application_request=freeclimb.ApplicationRequest())

            mock_method.assert_called_once()

    def test_delete_a_recording(self):
        """Test case for delete_a_recording

        Delete a Recording  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_delete_a_recording = self.api.delete_a_recording('ACCOUNT_ID', recording_id='fake_recording_id')

            mock_method.assert_called_once()

    def test_delete_an_application(self):
        """Test case for delete_an_application

        Delete an application  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_delete_an_application = self.api.delete_an_application('ACCOUNT_ID', application_id='fake_application_id')

            mock_method.assert_called_once()

    def test_delete_an_incoming_number(self):
        """Test case for delete_an_incoming_number

        Delete an Incoming Number  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_delete_an_incoming_number = self.api.delete_an_incoming_number('ACCOUNT_ID', phone_number_id='fake_incoming_number_id')

            mock_method.assert_called_once()

    def test_dequeue_a_member(self):
        """Test case for dequeue_a_member

        Dequeue a Member  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_dequeue_a_member = self.api.dequeue_a_member('ACCOUNT_ID', queue_id='fake_queue_id', call_id='fake_call_id')

            mock_method.assert_called_once()

    def test_dequeue_head_member(self):
        """Test case for dequeue_head_member

        Dequeue Head Member  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_dequeue_head_member = self.api.dequeue_head_member('ACCOUNT_ID', queue_id='fake_queue_id')

            mock_method.assert_called_once()

    def test_download_a_recording_file(self):
        """Test case for download_a_recording_file

        Download a Recording File  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_download_a_recording_file = self.api.download_a_recording_file('ACCOUNT_ID', recording_id='fake_recording_id')

            mock_method.assert_called_once()

    def test_filter_logs(self):
        """Test case for filter_logs

        Filter Logs  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_filter_logs = self.api.filter_logs('ACCOUNT_ID', filter_logs_request=freeclimb.FilterLogsRequest('fake_pql'))

            mock_method.assert_called_once()

    def test_get_a_call(self):
        """Test case for get_a_call

        Get a Call  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_a_call = self.api.get_a_call('ACCOUNT_ID', call_id='fake_call_id')

            mock_method.assert_called_once()

    def test_get_a_conference(self):
        """Test case for get_a_conference

        Get a Conference  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_a_conference = self.api.get_a_conference('ACCOUNT_ID', conference_id='fake_conference_id')

            mock_method.assert_called_once()

    def test_get_a_member(self):
        """Test case for get_a_member

        Get a Member  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_a_member = self.api.get_a_member('ACCOUNT_ID', queue_id='fake_queue_id', call_id='fake_call_id')

            mock_method.assert_called_once()

    def test_get_a_participant(self):
        """Test case for get_a_participant

        Get a Participant  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_a_participant = self.api.get_a_participant('ACCOUNT_ID', conference_id='fake_conference_id', call_id='fake_call_id')

            mock_method.assert_called_once()

    def test_get_a_queue(self):
        """Test case for get_a_queue

        Get a Queue  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_a_queue = self.api.get_a_queue('ACCOUNT_ID', queue_id='fake_queue_id')

            mock_method.assert_called_once()

    def test_get_a_recording(self):
        """Test case for get_a_recording

        Get a Recording  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_a_recording = self.api.get_a_recording('ACCOUNT_ID', recording_id='fake_recording_id')

            mock_method.assert_called_once()

    def test_get_an_account(self):
        """Test case for get_an_account

        Get an Account  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_an_account = self.api.get_an_account('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_get_an_application(self):
        """Test case for get_an_application

        Get an Application  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_an_application = self.api.get_an_application('ACCOUNT_ID', application_id='fake_application_id')

            mock_method.assert_called_once()

    def test_get_an_incoming_number(self):
        """Test case for get_an_incoming_number

        Get an Incoming Number  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_an_incoming_number = self.api.get_an_incoming_number('ACCOUNT_ID', phone_number_id='fake_phone_number_id')

            mock_method.assert_called_once()

    def test_get_an_sms_message(self):
        """Test case for get_an_sms_message

        Get an SMS Message  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_an_sms_message = self.api.get_an_sms_message('ACCOUNT_ID', message_id='fake_message_id')

            mock_method.assert_called_once()

    def test_get_head_member(self):
        """Test case for get_head_member

        Get Head Member  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_get_head_member = self.api.get_head_member('ACCOUNT_ID', queue_id='fake_queue_id')

            mock_method.assert_called_once()

    def test_list_active_queues(self):
        """Test case for list_active_queues

        List Active Queues  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_active_queues = self.api.list_active_queues('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_list_all_account_logs(self):
        """Test case for list_all_account_logs

        List All Account Logs  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_all_account_logs = self.api.list_all_account_logs('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_list_an_application(self):
        """Test case for list_an_application

        List applications  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_an_application = self.api.list_an_application('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_list_available_numbers(self):
        """Test case for list_available_numbers

        List available numbers  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_available_numbers = self.api.list_available_numbers()

            mock_method.assert_called_once()

    def test_list_call_logs(self):
        """Test case for list_call_logs

        List Call Logs  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_call_logs = self.api.list_call_logs('ACCOUNT_ID', call_id='fake_call_id')

            mock_method.assert_called_once()

    def test_list_call_recordings(self):
        """Test case for list_call_recordings

        List Call Recordings  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_call_recordings = self.api.list_call_recordings('ACCOUNT_ID', call_id='fake_call_id')

            mock_method.assert_called_once()

    def test_list_calls(self):
        """Test case for list_calls

        List Calls  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_calls = self.api.list_calls('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_list_conferences(self):
        """Test case for list_conferences

        List Conferences  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_conferences = self.api.list_conferences('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_list_incoming_numbers(self):
        """Test case for list_incoming_numbers

        List Incoming Numbers  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_incoming_numbers = self.api.list_incoming_numbers('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_list_members(self):
        """Test case for list_members

        List Members  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_members = self.api.list_members('ACCOUNT_ID', queue_id='fake_queue_id')

            mock_method.assert_called_once()

    def test_list_participants(self):
        """Test case for list_participants

        List Participants  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_participants = self.api.list_participants('ACCOUNT_ID', conference_id='fake_conference_id')

            mock_method.assert_called_once()

    def test_list_recordings(self):
        """Test case for list_recordings

        List Recordings  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_recordings = self.api.list_recordings('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_list_sms_messages(self):
        """Test case for list_sms_messages

        List SMS Messages  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_list_sms_messages = self.api.list_sms_messages('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_make_a_call(self):
        """Test case for make_a_call

        Make a Call  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_make_a_call = self.api.make_a_call('ACCOUNT_ID')

            mock_method.assert_called_once()

    def test_remove_a_participant(self):
        """Test case for remove_a_participant

        Remove a Participant  # noqa: E501
        """
        with mock.patch.object(freeclimb.ApiClient, 'call_api', return_value=None) as mock_method:
            self.test_remove_a_participant = self.api.remove_a_participant('ACCOUNT_ID', conference_id='fake_conference_id', call_id='fake_call_id')

            mock_method.assert_called_once()

    def test_send_an_sms_message(self):
        """Test case for send_an_sms_message

        Send an SMS Message  # noqa: E501
        """
        pass

    def test_stream_a_recording_file(self):
        """Test case for stream_a_recording_file

        Stream a Recording File  # noqa: E501
        """
        pass

    def test_update_a_conference(self):
        """Test case for update_a_conference

        Update a Conference  # noqa: E501
        """
        pass

    def test_update_a_live_call(self):
        """Test case for update_a_live_call

        Update a Live Call  # noqa: E501
        """
        pass

    def test_update_a_participant(self):
        """Test case for update_a_participant

        Update a Participant  # noqa: E501
        """
        pass

    def test_update_a_queue(self):
        """Test case for update_a_queue

        Update a Queue  # noqa: E501
        """
        pass

    def test_update_an_account(self):
        """Test case for update_an_account

        Manage an account  # noqa: E501
        """
        pass

    def test_update_an_application(self):
        """Test case for update_an_application

        Update an application  # noqa: E501
        """
        pass

    def test_update_an_incoming_number(self):
        """Test case for update_an_incoming_number

        Update an Incoming Number  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
