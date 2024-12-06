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


class ProfitLossRange(object):
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
        'price_percentage': 'str',
        'implied_volatility_percentage': 'str',
        'profit_loss': 'str'
    }

    attribute_map = {
        'price_percentage': 'price_percentage',
        'implied_volatility_percentage': 'implied_volatility_percentage',
        'profit_loss': 'profit_loss'
    }

    def __init__(self, price_percentage=None, implied_volatility_percentage=None, profit_loss=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, Configuration) -> None
        """ProfitLossRange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._price_percentage = None
        self._implied_volatility_percentage = None
        self._profit_loss = None
        self.discriminator = None

        if price_percentage is not None:
            self.price_percentage = price_percentage
        if implied_volatility_percentage is not None:
            self.implied_volatility_percentage = implied_volatility_percentage
        if profit_loss is not None:
            self.profit_loss = profit_loss

    @property
    def price_percentage(self):
        """Gets the price_percentage of this ProfitLossRange.  # noqa: E501

        Percentage change in price  # noqa: E501

        :return: The price_percentage of this ProfitLossRange.  # noqa: E501
        :rtype: str
        """
        return self._price_percentage

    @price_percentage.setter
    def price_percentage(self, price_percentage):
        """Sets the price_percentage of this ProfitLossRange.

        Percentage change in price  # noqa: E501

        :param price_percentage: The price_percentage of this ProfitLossRange.  # noqa: E501
        :type: str
        """

        self._price_percentage = price_percentage

    @property
    def implied_volatility_percentage(self):
        """Gets the implied_volatility_percentage of this ProfitLossRange.  # noqa: E501

        Percentage change in implied volatility  # noqa: E501

        :return: The implied_volatility_percentage of this ProfitLossRange.  # noqa: E501
        :rtype: str
        """
        return self._implied_volatility_percentage

    @implied_volatility_percentage.setter
    def implied_volatility_percentage(self, implied_volatility_percentage):
        """Sets the implied_volatility_percentage of this ProfitLossRange.

        Percentage change in implied volatility  # noqa: E501

        :param implied_volatility_percentage: The implied_volatility_percentage of this ProfitLossRange.  # noqa: E501
        :type: str
        """

        self._implied_volatility_percentage = implied_volatility_percentage

    @property
    def profit_loss(self):
        """Gets the profit_loss of this ProfitLossRange.  # noqa: E501

        PNL  # noqa: E501

        :return: The profit_loss of this ProfitLossRange.  # noqa: E501
        :rtype: str
        """
        return self._profit_loss

    @profit_loss.setter
    def profit_loss(self, profit_loss):
        """Sets the profit_loss of this ProfitLossRange.

        PNL  # noqa: E501

        :param profit_loss: The profit_loss of this ProfitLossRange.  # noqa: E501
        :type: str
        """

        self._profit_loss = profit_loss

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
        if not isinstance(other, ProfitLossRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProfitLossRange):
            return True

        return self.to_dict() != other.to_dict()
