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


class SpotPriceTrigger(object):
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
    openapi_types = {'price': 'str', 'rule': 'str', 'expiration': 'int'}

    attribute_map = {'price': 'price', 'rule': 'rule', 'expiration': 'expiration'}

    def __init__(self, price=None, rule=None, expiration=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, int, Configuration) -> None
        """SpotPriceTrigger - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._price = None
        self._rule = None
        self._expiration = None
        self.discriminator = None

        self.price = price
        self.rule = rule
        self.expiration = expiration

    @property
    def price(self):
        """Gets the price of this SpotPriceTrigger.  # noqa: E501

        Trigger price  # noqa: E501

        :return: The price of this SpotPriceTrigger.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SpotPriceTrigger.

        Trigger price  # noqa: E501

        :param price: The price of this SpotPriceTrigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def rule(self):
        """Gets the rule of this SpotPriceTrigger.  # noqa: E501

        Price trigger condition  - >=: triggered when market price larger than or equal to `price` field - <=: triggered when market price less than or equal to `price` field   # noqa: E501

        :return: The rule of this SpotPriceTrigger.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this SpotPriceTrigger.

        Price trigger condition  - >=: triggered when market price larger than or equal to `price` field - <=: triggered when market price less than or equal to `price` field   # noqa: E501

        :param rule: The rule of this SpotPriceTrigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rule is None:  # noqa: E501
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501
        allowed_values = [">=", "<="]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and rule not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `rule` ({0}), must be one of {1}".format(rule, allowed_values)  # noqa: E501
            )

        self._rule = rule

    @property
    def expiration(self):
        """Gets the expiration of this SpotPriceTrigger.  # noqa: E501

        How many seconds will the order wait for the condition being triggered. Order will be cancelled on timed out  # noqa: E501

        :return: The expiration of this SpotPriceTrigger.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this SpotPriceTrigger.

        How many seconds will the order wait for the condition being triggered. Order will be cancelled on timed out  # noqa: E501

        :param expiration: The expiration of this SpotPriceTrigger.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expiration is None:  # noqa: E501
            raise ValueError("Invalid value for `expiration`, must not be `None`")  # noqa: E501

        self._expiration = expiration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, SpotPriceTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpotPriceTrigger):
            return True

        return self.to_dict() != other.to_dict()
