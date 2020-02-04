# coding: utf-8

"""
    FreeClimb API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import enum

import freeclimb
from freeclimb.percl.play_beep import PlayBeep  # noqa: E501
from freeclimb.rest import ApiException


class TestPlayBeep(unittest.TestCase):
    """PlayBeep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlayBeepSuccess(self):
        """Test PlayBeep is successful"""
        # construct object with mandatory attributes with example values
        # percl = freeclimb.percl.PlayBeep()  # noqa: E501
        self.play_beep = PlayBeep('always')
        self.assertTrue(isinstance(self.play_beep, PlayBeep))
        self.assertEqual('always', self.play_beep.value)
        self.assertTrue(issubclass(PlayBeep, enum.Enum))

    def testPlayBeepFailure(self):
        """Test PlayBeep Fails properly"""
        with self.assertRaises(ValueError):
            PlayBeep('NotValidValue')

if __name__ == '__main__':
    unittest.main()
