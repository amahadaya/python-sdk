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
from freeclimb.percl.set_talk import SetTalk  # noqa: E501
from freeclimb.rest import ApiException


class TestSetTalk(unittest.TestCase):
    """SetTalk unit test stubs"""
    call_id='CA-fake-call-id'

    def setUp(self):
        self.set_talk = SetTalk(call_id=self.call_id)

    def tearDown(self):
        pass

    def testSetTalk(self):
        """Test SetTalk"""
        # construct object with mandatory attributes with example values
        # percl = freeclimb.percl.SetTalk()  # noqa: E501
        self.assertTrue(isinstance(self.set_talk, SetTalk))
        self.assertEqual(self.call_id, self.set_talk.call_id)
        self.assertTrue(hasattr(self.set_talk, 'talk'))

    def testToDict(self):
        """Test SetTalk to dictionary"""
        self.assertTrue(isinstance(self.set_talk.to_dict(), dict))
        self.assertEqual(list(self.set_talk.to_dict().keys())[0], self.set_talk.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
