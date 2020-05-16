# coding: utf-8

from setuptools import setup, find_packages

NAME = "enzona_qr"
VERSION = "0.0.1"

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Python Client library for interacting with EnZona's QR API.",
    author_email="",
    url="",
    keywords=["Swagger", "QRAPI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    PHP Client library for interacting with EnZona's QR API.
    """
)
