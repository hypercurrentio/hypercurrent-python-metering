# hypercurrent_metering.ApiEventsControllerApi

All URIs are relative to *https://api.hypercurrent.io/meter/v1/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event**](ApiEventsControllerApi.md#event) | **POST** /event | Log API event

# **event**
> event(body)

Log API event

Log API event

### Example
```python
from __future__ import print_function
import time
import hypercurrent_metering
from hypercurrent_metering.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hypercurrent_metering.ApiEventsControllerApi()
body = hypercurrent_metering.ApiEventDTO() # ApiEventDTO | 

try:
    # Log API event
    api_instance.event(body)
except ApiException as e:
    print("Exception when calling ApiEventsControllerApi->event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiEventDTO**](ApiEventDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

