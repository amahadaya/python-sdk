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
from freeclimb.models.application_list_all_of import ApplicationListAllOf  # noqa: E501
from freeclimb.models.application_result import ApplicationResult
from freeclimb.rest import ApiException


class TestApplicationListAllOf(unittest.TestCase):
    """ApplicationListAllOf unit test stubs"""

    def setUp(self):
        self.application1 = ApplicationResult(uri='http://localhost:80/application1')
        self.application2 = ApplicationResult(uri='http://localhost:80/application2')
        self.application_list_all_of = ApplicationListAllOf([self.application1, self.application2])

    def tearDown(self):
        pass

    def testApplicationListAllOf(self):
        """Test ApplicationListAllOf"""
        # construct object with mandatory attributes with example values
        # model = freeclimb.models.application_list_all_of.ApplicationListAllOf()  # noqa: E501
        self.assertTrue(isinstance(self.application_list_all_of, ApplicationListAllOf))


if __name__ == '__main__':
    unittest.main()
