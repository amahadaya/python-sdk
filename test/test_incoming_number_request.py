# coding: utf-8

"""
    FreeClimb API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import freeclimb
from freeclimb.models.incoming_number_request import IncomingNumberRequest  # noqa: E501
from freeclimb.rest import ApiException


class TestIncomingNumberRequest(unittest.TestCase):
    """IncomingNumberRequest unit test stubs"""

    def setUp(self):
        self.incoming_number_request = IncomingNumberRequest()

    def tearDown(self):
        pass

    def testIncomingNumberRequest(self):
        """Test IncomingNumberRequest"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.incoming_number_request.IncomingNumberRequest()  # noqa: E501
        self.assertTrue(isinstance(self.incoming_number_request, IncomingNumberRequest))


if __name__ == '__main__':
    unittest.main()
