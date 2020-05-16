# enzona-qr.PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api

All URIs are relative to *https://api.enzona.net/qr/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qr_account_post**](PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api.md#qr_account_post) | **POST** /qr/account | 


# **qr_account_post**
> InlineResponse200 qr_account_post(payload=payload)



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
api_instance = enzona-qr.PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api(enzona-qr.ApiClient(configuration))
payload = enzona-qr.Payload() # Payload | Parámetros de entrada (optional)

try:
    api_response = api_instance.qr_account_post(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermiteCrearUnQRParaHacerUnPagoEntrePersonas_Api->qr_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Payload**](Payload.md)| Parámetros de entrada | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

