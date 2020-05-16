# enzona-qr

***This is a work in progress, there are rough corners and the 
API can change witouth previuos warnings. 
Not recommended for production usage.***

PHP Client library for interacting with [EnZona's QR API](https://api.enzona.net). 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.0.0
- Package version: 0.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import enzona-qr 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import enzona-qr
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import enzona_qr
from enzona_qr.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
configuration = enzona_qr.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enzona_qr.ObtieneLaInformacinDeUnQRApi(enzona_qr.ApiClient(configuration))
qr_code = 'qr_code_example' # str | Código del QR a buscar

try:
    api_response = api_instance.qr_qr_code_get(qr_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObtieneLaInformacinDeUnQRApi->qr_qr_code_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.enzona.net/qr/v1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ObtieneLaInformacinDeUnQRApi* | [**qr_qr_code_get**](docs/ObtieneLaInformacinDeUnQRApi.md#qr_qr_code_get) | **GET** /qr/{qr_code} | 
*PermiteCrearUnQRDePagoAUnComercioApi* | [**qr_merchant_post**](docs/PermiteCrearUnQRDePagoAUnComercioApi.md#qr_merchant_post) | **POST** /qr/merchant | 
*PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api* | [**qr_account_post**](docs/PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api.md#qr_account_post) | **POST** /qr/account | 


## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [Payload](docs/Payload.md)
 - [Payload1](docs/Payload1.md)


## Documentation For Authorization


## default

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://api.enzona.net/authorize
- **Scopes**: 
 - **enzona_business_qr**: enzona_business_qr


## Author



