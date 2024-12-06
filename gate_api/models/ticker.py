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


class Ticker(object):
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
        'last': 'str',
        'lowest_ask': 'str',
        'lowest_size': 'str',
        'highest_bid': 'str',
        'highest_size': 'str',
        'change_percentage': 'str',
        'change_utc0': 'str',
        'change_utc8': 'str',
        'base_volume': 'str',
        'quote_volume': 'str',
        'high_24h': 'str',
        'low_24h': 'str',
        'etf_net_value': 'str',
        'etf_pre_net_value': 'str',
        'etf_pre_timestamp': 'int',
        'etf_leverage': 'str'
    }

    attribute_map = {
        'currency_pair': 'currency_pair',
        'last': 'last',
        'lowest_ask': 'lowest_ask',
        'lowest_size': 'lowest_size',
        'highest_bid': 'highest_bid',
        'highest_size': 'highest_size',
        'change_percentage': 'change_percentage',
        'change_utc0': 'change_utc0',
        'change_utc8': 'change_utc8',
        'base_volume': 'base_volume',
        'quote_volume': 'quote_volume',
        'high_24h': 'high_24h',
        'low_24h': 'low_24h',
        'etf_net_value': 'etf_net_value',
        'etf_pre_net_value': 'etf_pre_net_value',
        'etf_pre_timestamp': 'etf_pre_timestamp',
        'etf_leverage': 'etf_leverage'
    }

    def __init__(self, currency_pair=None, last=None, lowest_ask=None, lowest_size=None, highest_bid=None, highest_size=None, change_percentage=None, change_utc0=None, change_utc8=None, base_volume=None, quote_volume=None, high_24h=None, low_24h=None, etf_net_value=None, etf_pre_net_value=None, etf_pre_timestamp=None, etf_leverage=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, int, str, Configuration) -> None
        """Ticker - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_pair = None
        self._last = None
        self._lowest_ask = None
        self._lowest_size = None
        self._highest_bid = None
        self._highest_size = None
        self._change_percentage = None
        self._change_utc0 = None
        self._change_utc8 = None
        self._base_volume = None
        self._quote_volume = None
        self._high_24h = None
        self._low_24h = None
        self._etf_net_value = None
        self._etf_pre_net_value = None
        self._etf_pre_timestamp = None
        self._etf_leverage = None
        self.discriminator = None

        if currency_pair is not None:
            self.currency_pair = currency_pair
        if last is not None:
            self.last = last
        if lowest_ask is not None:
            self.lowest_ask = lowest_ask
        if lowest_size is not None:
            self.lowest_size = lowest_size
        if highest_bid is not None:
            self.highest_bid = highest_bid
        if highest_size is not None:
            self.highest_size = highest_size
        if change_percentage is not None:
            self.change_percentage = change_percentage
        if change_utc0 is not None:
            self.change_utc0 = change_utc0
        if change_utc8 is not None:
            self.change_utc8 = change_utc8
        if base_volume is not None:
            self.base_volume = base_volume
        if quote_volume is not None:
            self.quote_volume = quote_volume
        if high_24h is not None:
            self.high_24h = high_24h
        if low_24h is not None:
            self.low_24h = low_24h
        if etf_net_value is not None:
            self.etf_net_value = etf_net_value
        self.etf_pre_net_value = etf_pre_net_value
        self.etf_pre_timestamp = etf_pre_timestamp
        self.etf_leverage = etf_leverage

    @property
    def currency_pair(self):
        """Gets the currency_pair of this Ticker.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The currency_pair of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this Ticker.

        Currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this Ticker.  # noqa: E501
        :type: str
        """

        self._currency_pair = currency_pair

    @property
    def last(self):
        """Gets the last of this Ticker.  # noqa: E501

        Last trading price  # noqa: E501

        :return: The last of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this Ticker.

        Last trading price  # noqa: E501

        :param last: The last of this Ticker.  # noqa: E501
        :type: str
        """

        self._last = last

    @property
    def lowest_ask(self):
        """Gets the lowest_ask of this Ticker.  # noqa: E501

        Recent lowest ask  # noqa: E501

        :return: The lowest_ask of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._lowest_ask

    @lowest_ask.setter
    def lowest_ask(self, lowest_ask):
        """Sets the lowest_ask of this Ticker.

        Recent lowest ask  # noqa: E501

        :param lowest_ask: The lowest_ask of this Ticker.  # noqa: E501
        :type: str
        """

        self._lowest_ask = lowest_ask

    @property
    def lowest_size(self):
        """Gets the lowest_size of this Ticker.  # noqa: E501

        The latest seller's lowest price quantity; does not exist for batch query; exists for single query, and is empty if there is no data  # noqa: E501

        :return: The lowest_size of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._lowest_size

    @lowest_size.setter
    def lowest_size(self, lowest_size):
        """Sets the lowest_size of this Ticker.

        The latest seller's lowest price quantity; does not exist for batch query; exists for single query, and is empty if there is no data  # noqa: E501

        :param lowest_size: The lowest_size of this Ticker.  # noqa: E501
        :type: str
        """

        self._lowest_size = lowest_size

    @property
    def highest_bid(self):
        """Gets the highest_bid of this Ticker.  # noqa: E501

        Recent highest bid  # noqa: E501

        :return: The highest_bid of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._highest_bid

    @highest_bid.setter
    def highest_bid(self, highest_bid):
        """Sets the highest_bid of this Ticker.

        Recent highest bid  # noqa: E501

        :param highest_bid: The highest_bid of this Ticker.  # noqa: E501
        :type: str
        """

        self._highest_bid = highest_bid

    @property
    def highest_size(self):
        """Gets the highest_size of this Ticker.  # noqa: E501

        The latest buyer's highest price quantity; does not exist for batch query; exists for single query, and is empty if there is no data  # noqa: E501

        :return: The highest_size of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._highest_size

    @highest_size.setter
    def highest_size(self, highest_size):
        """Sets the highest_size of this Ticker.

        The latest buyer's highest price quantity; does not exist for batch query; exists for single query, and is empty if there is no data  # noqa: E501

        :param highest_size: The highest_size of this Ticker.  # noqa: E501
        :type: str
        """

        self._highest_size = highest_size

    @property
    def change_percentage(self):
        """Gets the change_percentage of this Ticker.  # noqa: E501

        Change percentage in the last 24h  # noqa: E501

        :return: The change_percentage of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._change_percentage

    @change_percentage.setter
    def change_percentage(self, change_percentage):
        """Sets the change_percentage of this Ticker.

        Change percentage in the last 24h  # noqa: E501

        :param change_percentage: The change_percentage of this Ticker.  # noqa: E501
        :type: str
        """

        self._change_percentage = change_percentage

    @property
    def change_utc0(self):
        """Gets the change_utc0 of this Ticker.  # noqa: E501

        utc0 timezone, the percentage change in the last 24 hours  # noqa: E501

        :return: The change_utc0 of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._change_utc0

    @change_utc0.setter
    def change_utc0(self, change_utc0):
        """Sets the change_utc0 of this Ticker.

        utc0 timezone, the percentage change in the last 24 hours  # noqa: E501

        :param change_utc0: The change_utc0 of this Ticker.  # noqa: E501
        :type: str
        """

        self._change_utc0 = change_utc0

    @property
    def change_utc8(self):
        """Gets the change_utc8 of this Ticker.  # noqa: E501

        utc8 timezone, the percentage change in the last 24 hours  # noqa: E501

        :return: The change_utc8 of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._change_utc8

    @change_utc8.setter
    def change_utc8(self, change_utc8):
        """Sets the change_utc8 of this Ticker.

        utc8 timezone, the percentage change in the last 24 hours  # noqa: E501

        :param change_utc8: The change_utc8 of this Ticker.  # noqa: E501
        :type: str
        """

        self._change_utc8 = change_utc8

    @property
    def base_volume(self):
        """Gets the base_volume of this Ticker.  # noqa: E501

        Base currency trade volume in the last 24h  # noqa: E501

        :return: The base_volume of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._base_volume

    @base_volume.setter
    def base_volume(self, base_volume):
        """Sets the base_volume of this Ticker.

        Base currency trade volume in the last 24h  # noqa: E501

        :param base_volume: The base_volume of this Ticker.  # noqa: E501
        :type: str
        """

        self._base_volume = base_volume

    @property
    def quote_volume(self):
        """Gets the quote_volume of this Ticker.  # noqa: E501

        Quote currency trade volume in the last 24h  # noqa: E501

        :return: The quote_volume of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._quote_volume

    @quote_volume.setter
    def quote_volume(self, quote_volume):
        """Sets the quote_volume of this Ticker.

        Quote currency trade volume in the last 24h  # noqa: E501

        :param quote_volume: The quote_volume of this Ticker.  # noqa: E501
        :type: str
        """

        self._quote_volume = quote_volume

    @property
    def high_24h(self):
        """Gets the high_24h of this Ticker.  # noqa: E501

        Highest price in 24h  # noqa: E501

        :return: The high_24h of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._high_24h

    @high_24h.setter
    def high_24h(self, high_24h):
        """Sets the high_24h of this Ticker.

        Highest price in 24h  # noqa: E501

        :param high_24h: The high_24h of this Ticker.  # noqa: E501
        :type: str
        """

        self._high_24h = high_24h

    @property
    def low_24h(self):
        """Gets the low_24h of this Ticker.  # noqa: E501

        Lowest price in 24h  # noqa: E501

        :return: The low_24h of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._low_24h

    @low_24h.setter
    def low_24h(self, low_24h):
        """Sets the low_24h of this Ticker.

        Lowest price in 24h  # noqa: E501

        :param low_24h: The low_24h of this Ticker.  # noqa: E501
        :type: str
        """

        self._low_24h = low_24h

    @property
    def etf_net_value(self):
        """Gets the etf_net_value of this Ticker.  # noqa: E501

        ETF net value  # noqa: E501

        :return: The etf_net_value of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._etf_net_value

    @etf_net_value.setter
    def etf_net_value(self, etf_net_value):
        """Sets the etf_net_value of this Ticker.

        ETF net value  # noqa: E501

        :param etf_net_value: The etf_net_value of this Ticker.  # noqa: E501
        :type: str
        """

        self._etf_net_value = etf_net_value

    @property
    def etf_pre_net_value(self):
        """Gets the etf_pre_net_value of this Ticker.  # noqa: E501

        ETF previous net value at re-balancing time  # noqa: E501

        :return: The etf_pre_net_value of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._etf_pre_net_value

    @etf_pre_net_value.setter
    def etf_pre_net_value(self, etf_pre_net_value):
        """Sets the etf_pre_net_value of this Ticker.

        ETF previous net value at re-balancing time  # noqa: E501

        :param etf_pre_net_value: The etf_pre_net_value of this Ticker.  # noqa: E501
        :type: str
        """

        self._etf_pre_net_value = etf_pre_net_value

    @property
    def etf_pre_timestamp(self):
        """Gets the etf_pre_timestamp of this Ticker.  # noqa: E501

        ETF previous re-balancing time  # noqa: E501

        :return: The etf_pre_timestamp of this Ticker.  # noqa: E501
        :rtype: int
        """
        return self._etf_pre_timestamp

    @etf_pre_timestamp.setter
    def etf_pre_timestamp(self, etf_pre_timestamp):
        """Sets the etf_pre_timestamp of this Ticker.

        ETF previous re-balancing time  # noqa: E501

        :param etf_pre_timestamp: The etf_pre_timestamp of this Ticker.  # noqa: E501
        :type: int
        """

        self._etf_pre_timestamp = etf_pre_timestamp

    @property
    def etf_leverage(self):
        """Gets the etf_leverage of this Ticker.  # noqa: E501

        ETF current leverage  # noqa: E501

        :return: The etf_leverage of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._etf_leverage

    @etf_leverage.setter
    def etf_leverage(self, etf_leverage):
        """Sets the etf_leverage of this Ticker.

        ETF current leverage  # noqa: E501

        :param etf_leverage: The etf_leverage of this Ticker.  # noqa: E501
        :type: str
        """

        self._etf_leverage = etf_leverage

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
        if not isinstance(other, Ticker):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Ticker):
            return True

        return self.to_dict() != other.to_dict()
