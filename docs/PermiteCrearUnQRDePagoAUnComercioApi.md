# enzona-qr.PermiteCrearUnQRDePagoAUnComercioApi

All URIs are relative to *https://api.enzona.net/qr/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qr_merchant_post**](PermiteCrearUnQRDePagoAUnComercioApi.md#qr_merchant_post) | **POST** /qr/merchant | 


# **qr_merchant_post**
> InlineResponse2002 qr_merchant_post(payload=payload)



### Example
```python
from __future__ import print_function
import time
import enzona-qr
from enzona-qr.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
configuration = enzona-qr.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enzona-qr.PermiteCrearUnQRDePagoAUnComercioApi(enzona-qr.ApiClient(configuration))
payload = enzona-qr.Payload1() # Payload1 | Parámetros de entrada (optional)

try:
    api_response = api_instance.qr_merchant_post(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermiteCrearUnQRDePagoAUnComercioApi->qr_merchant_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Payload1**](Payload1.md)| Parámetros de entrada | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

