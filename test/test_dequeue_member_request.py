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
from freeclimb.models.dequeue_member_request import DequeueMemberRequest  # noqa: E501
from freeclimb.rest import ApiException


class TestDequeueMemberRequest(unittest.TestCase):
    """DequeueMemberRequest unit test stubs"""

    def setUp(self):
        self.dequeue_member_request = DequeueMemberRequest()

    def tearDown(self):
        pass

    def testDequeueMemberRequest(self):
        """Test DequeueMemberRequest"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.dequeue_member_request.DequeueMemberRequest()  # noqa: E501
        self.assertTrue(isinstance(self.dequeue_member_request, DequeueMemberRequest))


if __name__ == '__main__':
    unittest.main()
