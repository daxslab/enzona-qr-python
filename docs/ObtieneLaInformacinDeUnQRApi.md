# enzona-qr.ObtieneLaInformacinDeUnQRApi

All URIs are relative to *https://api.enzona.net/qr/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qr_qr_code_get**](ObtieneLaInformacinDeUnQRApi.md#qr_qr_code_get) | **GET** /qr/{qr_code} | 


# **qr_qr_code_get**
> InlineResponse2001 qr_qr_code_get(qr_code)



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
api_instance = enzona-qr.ObtieneLaInformacinDeUnQRApi(enzona-qr.ApiClient(configuration))
qr_code = 'qr_code_example' # str | Código del QR a buscar

try:
    api_response = api_instance.qr_qr_code_get(qr_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObtieneLaInformacinDeUnQRApi->qr_qr_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qr_code** | **str**| Código del QR a buscar | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

