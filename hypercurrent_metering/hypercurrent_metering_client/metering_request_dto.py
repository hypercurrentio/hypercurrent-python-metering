# coding: utf-8

"""
    HyperCurrent Metering API

    HyperCurrent Metering API  # noqa: E501

    OpenAPI spec version: 1.11.0-SNAPSHOT
    Contact: info@hypercurrent.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MeteringRequestDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api': 'str',
        'product_key': 'str',
        'application': 'str',
        'method': 'str',
        'url': 'str',
        'metadata': 'str',
        'backend_latency': 'float',
        'gateway_latency': 'float',
        'response_code': 'int',
        'timed_out': 'bool',
        'request_message_size': 'int',
        'response_message_size': 'int',
        'request_headers': 'list[str]',
        'response_headers': 'list[str]',
        'user_agent': 'str',
        'remote_user': 'str',
        'remote_host': 'str',
        'http_protocol': 'str',
        'content_type': 'str',
        'correlation_id': 'str'
    }

    attribute_map = {
        'api': 'api',
        'product_key': 'productKey',
        'application': 'application',
        'method': 'method',
        'url': 'url',
        'metadata': 'metadata',
        'backend_latency': 'backendLatency',
        'gateway_latency': 'gatewayLatency',
        'response_code': 'responseCode',
        'timed_out': 'timedOut',
        'request_message_size': 'requestMessageSize',
        'response_message_size': 'responseMessageSize',
        'request_headers': 'requestHeaders',
        'response_headers': 'responseHeaders',
        'user_agent': 'userAgent',
        'remote_user': 'remoteUser',
        'remote_host': 'remoteHost',
        'http_protocol': 'httpProtocol',
        'content_type': 'contentType',
        'correlation_id': 'correlationId'
    }

    def __init__(self, api=None, product_key=None, application=None, method=None, url=None, metadata=None, backend_latency=None, gateway_latency=None, response_code=None, timed_out=None, request_message_size=None, response_message_size=None, request_headers=None, response_headers=None, user_agent=None, remote_user=None, remote_host=None, http_protocol=None, content_type=None, correlation_id=None):  # noqa: E501
        """MeteringRequestDTO - a model defined in Swagger"""  # noqa: E501
        self._api = None
        self._product_key = None
        self._application = None
        self._method = None
        self._url = None
        self._metadata = None
        self._backend_latency = None
        self._gateway_latency = None
        self._response_code = None
        self._timed_out = None
        self._request_message_size = None
        self._response_message_size = None
        self._request_headers = None
        self._response_headers = None
        self._user_agent = None
        self._remote_user = None
        self._remote_host = None
        self._http_protocol = None
        self._content_type = None
        self._correlation_id = None
        self.discriminator = None
        if api is not None:
            self.api = api
        if product_key is not None:
            self.product_key = product_key
        if application is not None:
            self.application = application
        if method is not None:
            self.method = method
        if url is not None:
            self.url = url
        if metadata is not None:
            self.metadata = metadata
        if backend_latency is not None:
            self.backend_latency = backend_latency
        if gateway_latency is not None:
            self.gateway_latency = gateway_latency
        if response_code is not None:
            self.response_code = response_code
        if timed_out is not None:
            self.timed_out = timed_out
        if request_message_size is not None:
            self.request_message_size = request_message_size
        if response_message_size is not None:
            self.response_message_size = response_message_size
        self.request_headers = request_headers
        self.response_headers = response_headers
        if user_agent is not None:
            self.user_agent = user_agent
        if remote_user is not None:
            self.remote_user = remote_user
        if remote_host is not None:
            self.remote_host = remote_host
        if http_protocol is not None:
            self.http_protocol = http_protocol
        if content_type is not None:
            self.content_type = content_type
        if correlation_id is not None:
            self.correlation_id = correlation_id

    @property
    def api(self):
        """Gets the api of this MeteringRequestDTO.  # noqa: E501


        :return: The api of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this MeteringRequestDTO.


        :param api: The api of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._api = api

    @property
    def product_key(self):
        """Gets the product_key of this MeteringRequestDTO.  # noqa: E501

        The Product Key ID  # noqa: E501

        :return: The product_key of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._product_key

    @product_key.setter
    def product_key(self, product_key):
        """Sets the product_key of this MeteringRequestDTO.

        The Product Key ID  # noqa: E501

        :param product_key: The product_key of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._product_key = product_key

    @property
    def application(self):
        """Gets the application of this MeteringRequestDTO.  # noqa: E501

        The Application ID  # noqa: E501

        :return: The application of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this MeteringRequestDTO.

        The Application ID  # noqa: E501

        :param application: The application of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def method(self):
        """Gets the method of this MeteringRequestDTO.  # noqa: E501

        The HTTP method being invoked  # noqa: E501

        :return: The method of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this MeteringRequestDTO.

        The HTTP method being invoked  # noqa: E501

        :param method: The method of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def url(self):
        """Gets the url of this MeteringRequestDTO.  # noqa: E501

        The HTTP URL being invoked  # noqa: E501

        :return: The url of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MeteringRequestDTO.

        The HTTP URL being invoked  # noqa: E501

        :param url: The url of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def metadata(self):
        """Gets the metadata of this MeteringRequestDTO.  # noqa: E501

        Additional billing metadata (currently only supports numeric values)  # noqa: E501

        :return: The metadata of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MeteringRequestDTO.

        Additional billing metadata (currently only supports numeric values)  # noqa: E501

        :param metadata: The metadata of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def backend_latency(self):
        """Gets the backend_latency of this MeteringRequestDTO.  # noqa: E501

        Backend API response time  # noqa: E501

        :return: The backend_latency of this MeteringRequestDTO.  # noqa: E501
        :rtype: float
        """
        return self._backend_latency

    @backend_latency.setter
    def backend_latency(self, backend_latency):
        """Sets the backend_latency of this MeteringRequestDTO.

        Backend API response time  # noqa: E501

        :param backend_latency: The backend_latency of this MeteringRequestDTO.  # noqa: E501
        :type: float
        """

        self._backend_latency = backend_latency

    @property
    def gateway_latency(self):
        """Gets the gateway_latency of this MeteringRequestDTO.  # noqa: E501

        Latency introduced by the API GW  # noqa: E501

        :return: The gateway_latency of this MeteringRequestDTO.  # noqa: E501
        :rtype: float
        """
        return self._gateway_latency

    @gateway_latency.setter
    def gateway_latency(self, gateway_latency):
        """Sets the gateway_latency of this MeteringRequestDTO.

        Latency introduced by the API GW  # noqa: E501

        :param gateway_latency: The gateway_latency of this MeteringRequestDTO.  # noqa: E501
        :type: float
        """

        self._gateway_latency = gateway_latency

    @property
    def response_code(self):
        """Gets the response_code of this MeteringRequestDTO.  # noqa: E501

        Backend HTTP response code  # noqa: E501

        :return: The response_code of this MeteringRequestDTO.  # noqa: E501
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this MeteringRequestDTO.

        Backend HTTP response code  # noqa: E501

        :param response_code: The response_code of this MeteringRequestDTO.  # noqa: E501
        :type: int
        """

        self._response_code = response_code

    @property
    def timed_out(self):
        """Gets the timed_out of this MeteringRequestDTO.  # noqa: E501

        Whether or not the backend timed out  # noqa: E501

        :return: The timed_out of this MeteringRequestDTO.  # noqa: E501
        :rtype: bool
        """
        return self._timed_out

    @timed_out.setter
    def timed_out(self, timed_out):
        """Sets the timed_out of this MeteringRequestDTO.

        Whether or not the backend timed out  # noqa: E501

        :param timed_out: The timed_out of this MeteringRequestDTO.  # noqa: E501
        :type: bool
        """

        self._timed_out = timed_out

    @property
    def request_message_size(self):
        """Gets the request_message_size of this MeteringRequestDTO.  # noqa: E501

        The size of the API request in bytes  # noqa: E501

        :return: The request_message_size of this MeteringRequestDTO.  # noqa: E501
        :rtype: int
        """
        return self._request_message_size

    @request_message_size.setter
    def request_message_size(self, request_message_size):
        """Sets the request_message_size of this MeteringRequestDTO.

        The size of the API request in bytes  # noqa: E501

        :param request_message_size: The request_message_size of this MeteringRequestDTO.  # noqa: E501
        :type: int
        """

        self._request_message_size = request_message_size

    @property
    def response_message_size(self):
        """Gets the response_message_size of this MeteringRequestDTO.  # noqa: E501

        The size of the API response in bytes  # noqa: E501

        :return: The response_message_size of this MeteringRequestDTO.  # noqa: E501
        :rtype: int
        """
        return self._response_message_size

    @response_message_size.setter
    def response_message_size(self, response_message_size):
        """Sets the response_message_size of this MeteringRequestDTO.

        The size of the API response in bytes  # noqa: E501

        :param response_message_size: The response_message_size of this MeteringRequestDTO.  # noqa: E501
        :type: int
        """

        self._response_message_size = response_message_size

    @property
    def request_headers(self):
        """Gets the request_headers of this MeteringRequestDTO.  # noqa: E501

        The comma seperated list of names of the headers in the request  # noqa: E501

        :return: The request_headers of this MeteringRequestDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """Sets the request_headers of this MeteringRequestDTO.

        The comma seperated list of names of the headers in the request  # noqa: E501

        :param request_headers: The request_headers of this MeteringRequestDTO.  # noqa: E501
        :type: list[str]
        """
        if request_headers is None:
            raise ValueError("Invalid value for `request_headers`, must not be `None`")  # noqa: E501

        self._request_headers = request_headers

    @property
    def response_headers(self):
        """Gets the response_headers of this MeteringRequestDTO.  # noqa: E501

        The comma seperated list of names of the headers in the response  # noqa: E501

        :return: The response_headers of this MeteringRequestDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        """Sets the response_headers of this MeteringRequestDTO.

        The comma seperated list of names of the headers in the response  # noqa: E501

        :param response_headers: The response_headers of this MeteringRequestDTO.  # noqa: E501
        :type: list[str]
        """
        if response_headers is None:
            raise ValueError("Invalid value for `response_headers`, must not be `None`")  # noqa: E501

        self._response_headers = response_headers

    @property
    def user_agent(self):
        """Gets the user_agent of this MeteringRequestDTO.  # noqa: E501

        The HTTP User Agent  # noqa: E501

        :return: The user_agent of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this MeteringRequestDTO.

        The HTTP User Agent  # noqa: E501

        :param user_agent: The user_agent of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

    @property
    def remote_user(self):
        """Gets the remote_user of this MeteringRequestDTO.  # noqa: E501

        The Remote User  # noqa: E501

        :return: The remote_user of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._remote_user

    @remote_user.setter
    def remote_user(self, remote_user):
        """Sets the remote_user of this MeteringRequestDTO.

        The Remote User  # noqa: E501

        :param remote_user: The remote_user of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._remote_user = remote_user

    @property
    def remote_host(self):
        """Gets the remote_host of this MeteringRequestDTO.  # noqa: E501

        The Remote Host  # noqa: E501

        :return: The remote_host of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._remote_host

    @remote_host.setter
    def remote_host(self, remote_host):
        """Sets the remote_host of this MeteringRequestDTO.

        The Remote Host  # noqa: E501

        :param remote_host: The remote_host of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._remote_host = remote_host

    @property
    def http_protocol(self):
        """Gets the http_protocol of this MeteringRequestDTO.  # noqa: E501

        The HTTP Protocol  # noqa: E501

        :return: The http_protocol of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._http_protocol

    @http_protocol.setter
    def http_protocol(self, http_protocol):
        """Sets the http_protocol of this MeteringRequestDTO.

        The HTTP Protocol  # noqa: E501

        :param http_protocol: The http_protocol of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._http_protocol = http_protocol

    @property
    def content_type(self):
        """Gets the content_type of this MeteringRequestDTO.  # noqa: E501

        The Content Type  # noqa: E501

        :return: The content_type of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this MeteringRequestDTO.

        The Content Type  # noqa: E501

        :param content_type: The content_type of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def correlation_id(self):
        """Gets the correlation_id of this MeteringRequestDTO.  # noqa: E501

        The Correlation ID  # noqa: E501

        :return: The correlation_id of this MeteringRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this MeteringRequestDTO.

        The Correlation ID  # noqa: E501

        :param correlation_id: The correlation_id of this MeteringRequestDTO.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MeteringRequestDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MeteringRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
