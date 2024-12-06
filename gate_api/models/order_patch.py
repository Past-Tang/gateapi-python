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


class OrderPatch(object):
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
        'account': 'str',
        'amount': 'str',
        'price': 'str',
        'amend_text': 'str',
        'action_mode': 'str'
    }

    attribute_map = {
        'currency_pair': 'currency_pair',
        'account': 'account',
        'amount': 'amount',
        'price': 'price',
        'amend_text': 'amend_text',
        'action_mode': 'action_mode'
    }

    def __init__(self, currency_pair=None, account=None, amount=None, price=None, amend_text=None, action_mode=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, str, str, str, Configuration) -> None
        """OrderPatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_pair = None
        self._account = None
        self._amount = None
        self._price = None
        self._amend_text = None
        self._action_mode = None
        self.discriminator = None

        if currency_pair is not None:
            self.currency_pair = currency_pair
        if account is not None:
            self.account = account
        if amount is not None:
            self.amount = amount
        if price is not None:
            self.price = price
        if amend_text is not None:
            self.amend_text = amend_text
        if action_mode is not None:
            self.action_mode = action_mode

    @property
    def currency_pair(self):
        """Gets the currency_pair of this OrderPatch.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The currency_pair of this OrderPatch.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this OrderPatch.

        Currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this OrderPatch.  # noqa: E501
        :type: str
        """

        self._currency_pair = currency_pair

    @property
    def account(self):
        """Gets the account of this OrderPatch.  # noqa: E501

        指定查询账户。  # noqa: E501

        :return: The account of this OrderPatch.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this OrderPatch.

        指定查询账户。  # noqa: E501

        :param account: The account of this OrderPatch.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def amount(self):
        """Gets the amount of this OrderPatch.  # noqa: E501

        New order amount. `amount` and `price` must specify one of them  # noqa: E501

        :return: The amount of this OrderPatch.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OrderPatch.

        New order amount. `amount` and `price` must specify one of them  # noqa: E501

        :param amount: The amount of this OrderPatch.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this OrderPatch.  # noqa: E501

        New order price. `amount` and `Price` must specify one of them\"  # noqa: E501

        :return: The price of this OrderPatch.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderPatch.

        New order price. `amount` and `Price` must specify one of them\"  # noqa: E501

        :param price: The price of this OrderPatch.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def amend_text(self):
        """Gets the amend_text of this OrderPatch.  # noqa: E501

        Custom info during amending order  # noqa: E501

        :return: The amend_text of this OrderPatch.  # noqa: E501
        :rtype: str
        """
        return self._amend_text

    @amend_text.setter
    def amend_text(self, amend_text):
        """Sets the amend_text of this OrderPatch.

        Custom info during amending order  # noqa: E501

        :param amend_text: The amend_text of this OrderPatch.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                amend_text is not None and len(amend_text) > 31):
            raise ValueError("Invalid value for `amend_text`, length must be less than or equal to `31`")  # noqa: E501

        self._amend_text = amend_text

    @property
    def action_mode(self):
        """Gets the action_mode of this OrderPatch.  # noqa: E501

        Processing Mode: When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result ACK: Asynchronous mode, only returns key order fields RESULT: No clearing information FULL: Full mode (default)  # noqa: E501

        :return: The action_mode of this OrderPatch.  # noqa: E501
        :rtype: str
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        """Sets the action_mode of this OrderPatch.

        Processing Mode: When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result ACK: Asynchronous mode, only returns key order fields RESULT: No clearing information FULL: Full mode (default)  # noqa: E501

        :param action_mode: The action_mode of this OrderPatch.  # noqa: E501
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
        if not isinstance(other, OrderPatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderPatch):
            return True

        return self.to_dict() != other.to_dict()
