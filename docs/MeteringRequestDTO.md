# MeteringRequestDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** |  | [optional] 
**product_key** | **str** | The Product Key ID | [optional] 
**application** | **str** | The Application ID | [optional] 
**method** | **str** | The HTTP method being invoked | [optional] 
**url** | **str** | The HTTP URL being invoked | [optional] 
**metadata** | **str** | Additional billing metadata (currently only supports numeric values) | [optional] 
**backend_latency** | **float** | Backend API response time | [optional] 
**gateway_latency** | **float** | Latency introduced by the API GW | [optional] 
**response_code** | **int** | Backend HTTP response code | [optional] 
**timed_out** | **bool** | Whether or not the backend timed out | [optional] 
**request_message_size** | **int** | The size of the API request in bytes | [optional] 
**response_message_size** | **int** | The size of the API response in bytes | [optional] 
**request_headers** | **list[str]** | The comma seperated list of names of the headers in the request | 
**response_headers** | **list[str]** | The comma seperated list of names of the headers in the response | 
**user_agent** | **str** | The HTTP User Agent | [optional] 
**remote_user** | **str** | The Remote User | [optional] 
**remote_host** | **str** | The Remote Host | [optional] 
**http_protocol** | **str** | The HTTP Protocol | [optional] 
**content_type** | **str** | The Content Type | [optional] 
**correlation_id** | **str** | The Correlation ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

