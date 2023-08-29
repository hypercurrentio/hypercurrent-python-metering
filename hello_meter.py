import hypercurrent_metering
from hypercurrent_metering.rest import ApiException
from hypercurrent_metering import Configuration, ApiClient

hypercurrent = hypercurrent_metering.MeteringControllerApi(hypercurrent_metering.ApiClient())
hypercurrent.api_client.default_headers["x-api-key"] = "hak_5o212l_feecf628b27c880b0c711c3796929b6ece376bad3b1a6c71310273e2c440eb6a"
body = hypercurrent_metering.MeteringRequestDTO(
        #api = "5o212l:2c6ea3c7-e4e7-497c-960e-47fd03b37cb9", 
        application = "77273cd5-02be-46da-8022-87e237f25393",
        method="GET", 
        url="foo", 
        request_headers=[], 
        response_headers=[]) 
try:
        hypercurrent.meter(body)
except ApiException as e:
        print("Exception when metering API request: %s\n" % e)
