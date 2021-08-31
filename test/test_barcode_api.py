# coding: utf-8

"""
    Quickpac API

    Here you will find all public interfaces to the Quickpac system.  # noqa: E501

    OpenAPI spec version: v1.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.barcode_api import BarcodeApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBarcodeApi(unittest.TestCase):
    """BarcodeApi unit test stubs"""

    def setUp(self):
        self.api = BarcodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_barcode_generate_label_post(self):
        """Test case for barcode_generate_label_post

        Generates an address label  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
