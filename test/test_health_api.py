# coding: utf-8

"""
    DSB Message Broker API

    Swagger documentation for the DSB Message Broker API  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import dsb_client.swagger_client
from dsb_client.swagger_client.api.health_api import HealthApi  # noqa: E501
from dsb_client.swagger_client.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_controller_check(self):
        """Test case for health_controller_check

        """
        pass


if __name__ == '__main__':
    unittest.main()
