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
from freeclimb.models.account_result_all_of import AccountResultAllOf  # noqa: E501
from freeclimb.rest import ApiException


class TestAccountResultAllOf(unittest.TestCase):
    """AccountResultAllOf unit test stubs"""

    def setUp(self):
        self.account_result_all_of = AccountResultAllOf('account_id', 'auth_token', 'alias', 'label')

    def tearDown(self):
        pass

    def testAccountResultAllOf(self):
        """Test AccountResultAllOf"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.account_result_all_of.AccountResultAllOf()  # noqa: E501
        self.assertTrue(isinstance(self.account_result_all_of, AccountResultAllOf))


if __name__ == '__main__':
    unittest.main()
