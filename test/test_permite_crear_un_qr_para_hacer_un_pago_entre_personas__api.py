# coding: utf-8

"""
    QRAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import enzona-qr
from enzona-qr.api.permite_crear_un_qr_para_hacer_un_pago_entre_personas__api import PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api  # noqa: E501
from enzona-qr.rest import ApiException


class TestPermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api(unittest.TestCase):
    """PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api unit test stubs"""

    def setUp(self):
        self.api = enzona-qr.api.permite_crear_un_qr_para_hacer_un_pago_entre_personas__api.PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_qr_account_post(self):
        """Test case for qr_account_post

        """
        pass


if __name__ == '__main__':
    unittest.main()