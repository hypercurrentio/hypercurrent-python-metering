# coding: utf-8

"""
    HyperCurrent Metering API

    HyperCurrent Metering API  # noqa: E501

    OpenAPI spec version: 1.11.0-SNAPSHOT
    Contact: info@hypercurrent.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hypercurrent_metering.api_client import ApiClient


class MeteringControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def meter(self, body, **kwargs):  # noqa: E501
        """Insert API metering data  # noqa: E501

        Insert API metering data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.meter(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MeteringRequestDTO body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.meter_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.meter_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def meter_with_http_info(self, body, **kwargs):  # noqa: E501
        """Insert API metering data  # noqa: E501

        Insert API metering data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.meter_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MeteringRequestDTO body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method meter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `meter`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/meter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def valid(self, **kwargs):  # noqa: E501
        """Determine if a ProductKey is valid or not  # noqa: E501

        Determine if a ProductKey is valid or not  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.valid(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_key: The Product Key
        :param str application: The Application ID
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.valid_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.valid_with_http_info(**kwargs)  # noqa: E501
            return data

    def valid_with_http_info(self, **kwargs):  # noqa: E501
        """Determine if a ProductKey is valid or not  # noqa: E501

        Determine if a ProductKey is valid or not  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.valid_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_key: The Product Key
        :param str application: The Application ID
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_key', 'application']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method valid" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_key' in params:
            query_params.append(('productKey', params['product_key']))  # noqa: E501
        if 'application' in params:
            query_params.append(('application', params['application']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/meter/product-key', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
