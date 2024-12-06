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


class RiskUnits(object):
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
        'symbol': 'str',
        'spot_in_use': 'str',
        'maintain_margin': 'str',
        'initial_margin': 'str',
        'delta': 'str',
        'gamma': 'str',
        'theta': 'str',
        'vega': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'spot_in_use': 'spot_in_use',
        'maintain_margin': 'maintain_margin',
        'initial_margin': 'initial_margin',
        'delta': 'delta',
        'gamma': 'gamma',
        'theta': 'theta',
        'vega': 'vega'
    }

    def __init__(self, symbol=None, spot_in_use=None, maintain_margin=None, initial_margin=None, delta=None, gamma=None, theta=None, vega=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, str, str, str, str, str, Configuration) -> None
        """RiskUnits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol = None
        self._spot_in_use = None
        self._maintain_margin = None
        self._initial_margin = None
        self._delta = None
        self._gamma = None
        self._theta = None
        self._vega = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if spot_in_use is not None:
            self.spot_in_use = spot_in_use
        if maintain_margin is not None:
            self.maintain_margin = maintain_margin
        if initial_margin is not None:
            self.initial_margin = initial_margin
        if delta is not None:
            self.delta = delta
        if gamma is not None:
            self.gamma = gamma
        if theta is not None:
            self.theta = theta
        if vega is not None:
            self.vega = vega

    @property
    def symbol(self):
        """Gets the symbol of this RiskUnits.  # noqa: E501

        Risk unit flag  # noqa: E501

        :return: The symbol of this RiskUnits.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this RiskUnits.

        Risk unit flag  # noqa: E501

        :param symbol: The symbol of this RiskUnits.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def spot_in_use(self):
        """Gets the spot_in_use of this RiskUnits.  # noqa: E501

        Spot hedging utilization  # noqa: E501

        :return: The spot_in_use of this RiskUnits.  # noqa: E501
        :rtype: str
        """
        return self._spot_in_use

    @spot_in_use.setter
    def spot_in_use(self, spot_in_use):
        """Sets the spot_in_use of this RiskUnits.

        Spot hedging utilization  # noqa: E501

        :param spot_in_use: The spot_in_use of this RiskUnits.  # noqa: E501
        :type: str
        """

        self._spot_in_use = spot_in_use

    @property
    def maintain_margin(self):
        """Gets the maintain_margin of this RiskUnits.  # noqa: E501

        Maintenance margin for risk unit  # noqa: E501

        :return: The maintain_margin of this RiskUnits.  # noqa: E501
        :rtype: str
        """
        return self._maintain_margin

    @maintain_margin.setter
    def maintain_margin(self, maintain_margin):
        """Sets the maintain_margin of this RiskUnits.

        Maintenance margin for risk unit  # noqa: E501

        :param maintain_margin: The maintain_margin of this RiskUnits.  # noqa: E501
        :type: str
        """

        self._maintain_margin = maintain_margin

    @property
    def initial_margin(self):
        """Gets the initial_margin of this RiskUnits.  # noqa: E501

        Initial margin for risk unit  # noqa: E501

        :return: The initial_margin of this RiskUnits.  # noqa: E501
        :rtype: str
        """
        return self._initial_margin

    @initial_margin.setter
    def initial_margin(self, initial_margin):
        """Sets the initial_margin of this RiskUnits.

        Initial margin for risk unit  # noqa: E501

        :param initial_margin: The initial_margin of this RiskUnits.  # noqa: E501
        :type: str
        """

        self._initial_margin = initial_margin

    @property
    def delta(self):
        """Gets the delta of this RiskUnits.  # noqa: E501

        Total Delta of risk unit  # noqa: E501

        :return: The delta of this RiskUnits.  # noqa: E501
        :rtype: str
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this RiskUnits.

        Total Delta of risk unit  # noqa: E501

        :param delta: The delta of this RiskUnits.  # noqa: E501
        :type: str
        """

        self._delta = delta

    @property
    def gamma(self):
        """Gets the gamma of this RiskUnits.  # noqa: E501

        Total Gamma of risk unit  # noqa: E501

        :return: The gamma of this RiskUnits.  # noqa: E501
        :rtype: str
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this RiskUnits.

        Total Gamma of risk unit  # noqa: E501

        :param gamma: The gamma of this RiskUnits.  # noqa: E501
        :type: str
        """

        self._gamma = gamma

    @property
    def theta(self):
        """Gets the theta of this RiskUnits.  # noqa: E501

        Total Theta of risk unit  # noqa: E501

        :return: The theta of this RiskUnits.  # noqa: E501
        :rtype: str
        """
        return self._theta

    @theta.setter
    def theta(self, theta):
        """Sets the theta of this RiskUnits.

        Total Theta of risk unit  # noqa: E501

        :param theta: The theta of this RiskUnits.  # noqa: E501
        :type: str
        """

        self._theta = theta

    @property
    def vega(self):
        """Gets the vega of this RiskUnits.  # noqa: E501

        Total Vega of risk unit  # noqa: E501

        :return: The vega of this RiskUnits.  # noqa: E501
        :rtype: str
        """
        return self._vega

    @vega.setter
    def vega(self, vega):
        """Sets the vega of this RiskUnits.

        Total Vega of risk unit  # noqa: E501

        :param vega: The vega of this RiskUnits.  # noqa: E501
        :type: str
        """

        self._vega = vega

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
        if not isinstance(other, RiskUnits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RiskUnits):
            return True

        return self.to_dict() != other.to_dict()
