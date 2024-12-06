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


class SpotFee(object):
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
        'user_id': 'int',
        'taker_fee': 'str',
        'maker_fee': 'str',
        'gt_discount': 'bool',
        'gt_taker_fee': 'str',
        'gt_maker_fee': 'str',
        'loan_fee': 'str',
        'point_type': 'str',
        'currency_pair': 'str',
        'debit_fee': 'int'
    }

    attribute_map = {
        'user_id': 'user_id',
        'taker_fee': 'taker_fee',
        'maker_fee': 'maker_fee',
        'gt_discount': 'gt_discount',
        'gt_taker_fee': 'gt_taker_fee',
        'gt_maker_fee': 'gt_maker_fee',
        'loan_fee': 'loan_fee',
        'point_type': 'point_type',
        'currency_pair': 'currency_pair',
        'debit_fee': 'debit_fee'
    }

    def __init__(self, user_id=None, taker_fee=None, maker_fee=None, gt_discount=None, gt_taker_fee=None, gt_maker_fee=None, loan_fee=None, point_type=None, currency_pair=None, debit_fee=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, str, str, bool, str, str, str, str, str, int, Configuration) -> None
        """SpotFee - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._taker_fee = None
        self._maker_fee = None
        self._gt_discount = None
        self._gt_taker_fee = None
        self._gt_maker_fee = None
        self._loan_fee = None
        self._point_type = None
        self._currency_pair = None
        self._debit_fee = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if taker_fee is not None:
            self.taker_fee = taker_fee
        if maker_fee is not None:
            self.maker_fee = maker_fee
        if gt_discount is not None:
            self.gt_discount = gt_discount
        if gt_taker_fee is not None:
            self.gt_taker_fee = gt_taker_fee
        if gt_maker_fee is not None:
            self.gt_maker_fee = gt_maker_fee
        if loan_fee is not None:
            self.loan_fee = loan_fee
        if point_type is not None:
            self.point_type = point_type
        if currency_pair is not None:
            self.currency_pair = currency_pair
        if debit_fee is not None:
            self.debit_fee = debit_fee

    @property
    def user_id(self):
        """Gets the user_id of this SpotFee.  # noqa: E501

        User ID  # noqa: E501

        :return: The user_id of this SpotFee.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SpotFee.

        User ID  # noqa: E501

        :param user_id: The user_id of this SpotFee.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def taker_fee(self):
        """Gets the taker_fee of this SpotFee.  # noqa: E501

        taker fee rate  # noqa: E501

        :return: The taker_fee of this SpotFee.  # noqa: E501
        :rtype: str
        """
        return self._taker_fee

    @taker_fee.setter
    def taker_fee(self, taker_fee):
        """Sets the taker_fee of this SpotFee.

        taker fee rate  # noqa: E501

        :param taker_fee: The taker_fee of this SpotFee.  # noqa: E501
        :type: str
        """

        self._taker_fee = taker_fee

    @property
    def maker_fee(self):
        """Gets the maker_fee of this SpotFee.  # noqa: E501

        maker fee rate  # noqa: E501

        :return: The maker_fee of this SpotFee.  # noqa: E501
        :rtype: str
        """
        return self._maker_fee

    @maker_fee.setter
    def maker_fee(self, maker_fee):
        """Sets the maker_fee of this SpotFee.

        maker fee rate  # noqa: E501

        :param maker_fee: The maker_fee of this SpotFee.  # noqa: E501
        :type: str
        """

        self._maker_fee = maker_fee

    @property
    def gt_discount(self):
        """Gets the gt_discount of this SpotFee.  # noqa: E501

        If GT deduction is enabled  # noqa: E501

        :return: The gt_discount of this SpotFee.  # noqa: E501
        :rtype: bool
        """
        return self._gt_discount

    @gt_discount.setter
    def gt_discount(self, gt_discount):
        """Sets the gt_discount of this SpotFee.

        If GT deduction is enabled  # noqa: E501

        :param gt_discount: The gt_discount of this SpotFee.  # noqa: E501
        :type: bool
        """

        self._gt_discount = gt_discount

    @property
    def gt_taker_fee(self):
        """Gets the gt_taker_fee of this SpotFee.  # noqa: E501

        Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  # noqa: E501

        :return: The gt_taker_fee of this SpotFee.  # noqa: E501
        :rtype: str
        """
        return self._gt_taker_fee

    @gt_taker_fee.setter
    def gt_taker_fee(self, gt_taker_fee):
        """Sets the gt_taker_fee of this SpotFee.

        Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  # noqa: E501

        :param gt_taker_fee: The gt_taker_fee of this SpotFee.  # noqa: E501
        :type: str
        """

        self._gt_taker_fee = gt_taker_fee

    @property
    def gt_maker_fee(self):
        """Gets the gt_maker_fee of this SpotFee.  # noqa: E501

        Maker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  # noqa: E501

        :return: The gt_maker_fee of this SpotFee.  # noqa: E501
        :rtype: str
        """
        return self._gt_maker_fee

    @gt_maker_fee.setter
    def gt_maker_fee(self, gt_maker_fee):
        """Sets the gt_maker_fee of this SpotFee.

        Maker fee rate if using GT deduction. It will be 0 if GT deduction is disabled  # noqa: E501

        :param gt_maker_fee: The gt_maker_fee of this SpotFee.  # noqa: E501
        :type: str
        """

        self._gt_maker_fee = gt_maker_fee

    @property
    def loan_fee(self):
        """Gets the loan_fee of this SpotFee.  # noqa: E501

        Loan fee rate of margin lending  # noqa: E501

        :return: The loan_fee of this SpotFee.  # noqa: E501
        :rtype: str
        """
        return self._loan_fee

    @loan_fee.setter
    def loan_fee(self, loan_fee):
        """Sets the loan_fee of this SpotFee.

        Loan fee rate of margin lending  # noqa: E501

        :param loan_fee: The loan_fee of this SpotFee.  # noqa: E501
        :type: str
        """

        self._loan_fee = loan_fee

    @property
    def point_type(self):
        """Gets the point_type of this SpotFee.  # noqa: E501

        Point type. 0 - Initial version. 1 - new version since 202009  # noqa: E501

        :return: The point_type of this SpotFee.  # noqa: E501
        :rtype: str
        """
        return self._point_type

    @point_type.setter
    def point_type(self, point_type):
        """Sets the point_type of this SpotFee.

        Point type. 0 - Initial version. 1 - new version since 202009  # noqa: E501

        :param point_type: The point_type of this SpotFee.  # noqa: E501
        :type: str
        """

        self._point_type = point_type

    @property
    def currency_pair(self):
        """Gets the currency_pair of this SpotFee.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The currency_pair of this SpotFee.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this SpotFee.

        Currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this SpotFee.  # noqa: E501
        :type: str
        """

        self._currency_pair = currency_pair

    @property
    def debit_fee(self):
        """Gets the debit_fee of this SpotFee.  # noqa: E501

        Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  # noqa: E501

        :return: The debit_fee of this SpotFee.  # noqa: E501
        :rtype: int
        """
        return self._debit_fee

    @debit_fee.setter
    def debit_fee(self, debit_fee):
        """Sets the debit_fee of this SpotFee.

        Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates  # noqa: E501

        :param debit_fee: The debit_fee of this SpotFee.  # noqa: E501
        :type: int
        """

        self._debit_fee = debit_fee

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
        if not isinstance(other, SpotFee):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpotFee):
            return True

        return self.to_dict() != other.to_dict()
