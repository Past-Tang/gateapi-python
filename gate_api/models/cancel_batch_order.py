# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class CancelBatchOrder(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currency_pair': 'str',
        'id': 'str',
        'action_mode': 'str'
    }

    attribute_map = {
        'currency_pair': 'currency_pair',
        'id': 'id',
        'action_mode': 'action_mode'
    }

    def __init__(self, currency_pair=None, id=None, action_mode=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, Configuration) -> None
        """CancelBatchOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_pair = None
        self._id = None
        self._action_mode = None
        self.discriminator = None

        self.currency_pair = currency_pair
        self.id = id
        if action_mode is not None:
            self.action_mode = action_mode

    @property
    def currency_pair(self):
        """Gets the currency_pair of this CancelBatchOrder.  # noqa: E501

        Order currency pair  # noqa: E501

        :return: The currency_pair of this CancelBatchOrder.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this CancelBatchOrder.

        Order currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this CancelBatchOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_pair is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_pair`, must not be `None`")  # noqa: E501

        self._currency_pair = currency_pair

    @property
    def id(self):
        """Gets the id of this CancelBatchOrder.  # noqa: E501

        Order ID or user custom ID. Custom ID are accepted only within 30 minutes after order creation  # noqa: E501

        :return: The id of this CancelBatchOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CancelBatchOrder.

        Order ID or user custom ID. Custom ID are accepted only within 30 minutes after order creation  # noqa: E501

        :param id: The id of this CancelBatchOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def action_mode(self):
        """Gets the action_mode of this CancelBatchOrder.  # noqa: E501

        Processing Mode: When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result ACK: Asynchronous mode, only returns key order fields RESULT: No clearing information FULL: Full mode (default)  # noqa: E501

        :return: The action_mode of this CancelBatchOrder.  # noqa: E501
        :rtype: str
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        """Sets the action_mode of this CancelBatchOrder.

        Processing Mode: When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result ACK: Asynchronous mode, only returns key order fields RESULT: No clearing information FULL: Full mode (default)  # noqa: E501

        :param action_mode: The action_mode of this CancelBatchOrder.  # noqa: E501
        :type: str
        """

        self._action_mode = action_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CancelBatchOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CancelBatchOrder):
            return True

        return self.to_dict() != other.to_dict()
