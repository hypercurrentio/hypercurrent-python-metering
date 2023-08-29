# hypercurrent_metering.MeteringControllerApi

All URIs are relative to *https://api.hypercurrent.io/meter/v1/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meter**](MeteringControllerApi.md#meter) | **POST** /meter | Insert API metering data
[**valid**](MeteringControllerApi.md#valid) | **GET** /meter/product-key | Determine if a ProductKey is valid or not

# **meter**
> meter(body)

Insert API metering data

Insert API metering data

### Example
```python
from __future__ import print_function
import time
import hypercurrent_metering
from hypercurrent_metering.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hypercurrent_metering.MeteringControllerApi()
body = hypercurrent_metering.MeteringRequestDTO() # MeteringRequestDTO | 

try:
    # Insert API metering data
    api_instance.meter(body)
except ApiException as e:
    print("Exception when calling MeteringControllerApi->meter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MeteringRequestDTO**](MeteringRequestDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **valid**
> object valid(product_key=product_key, application=application)

Determine if a ProductKey is valid or not

Determine if a ProductKey is valid or not

### Example
```python
from __future__ import print_function
import time
import hypercurrent_metering
from hypercurrent_metering.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hypercurrent_metering.MeteringControllerApi()
product_key = 'product_key_example' # str | The Product Key (optional)
application = 'application_example' # str | The Application ID (optional)

try:
    # Determine if a ProductKey is valid or not
    api_response = api_instance.valid(product_key=product_key, application=application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeteringControllerApi->valid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_key** | **str**| The Product Key | [optional] 
 **application** | **str**| The Application ID | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

