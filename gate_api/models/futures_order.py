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


class FuturesOrder(object):
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
        'id': 'int',
        'user': 'int',
        'create_time': 'float',
        'finish_time': 'float',
        'finish_as': 'str',
        'status': 'str',
        'contract': 'str',
        'size': 'int',
        'iceberg': 'int',
        'price': 'str',
        'close': 'bool',
        'is_close': 'bool',
        'reduce_only': 'bool',
        'is_reduce_only': 'bool',
        'is_liq': 'bool',
        'tif': 'str',
        'left': 'int',
        'fill_price': 'str',
        'text': 'str',
        'tkfr': 'str',
        'mkfr': 'str',
        'refu': 'int',
        'auto_size': 'str',
        'stp_id': 'int',
        'stp_act': 'str',
        'amend_text': 'str',
        'biz_info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'finish_as': 'finish_as',
        'status': 'status',
        'contract': 'contract',
        'size': 'size',
        'iceberg': 'iceberg',
        'price': 'price',
        'close': 'close',
        'is_close': 'is_close',
        'reduce_only': 'reduce_only',
        'is_reduce_only': 'is_reduce_only',
        'is_liq': 'is_liq',
        'tif': 'tif',
        'left': 'left',
        'fill_price': 'fill_price',
        'text': 'text',
        'tkfr': 'tkfr',
        'mkfr': 'mkfr',
        'refu': 'refu',
        'auto_size': 'auto_size',
        'stp_id': 'stp_id',
        'stp_act': 'stp_act',
        'amend_text': 'amend_text',
        'biz_info': 'biz_info'
    }

    def __init__(self, id=None, user=None, create_time=None, finish_time=None, finish_as=None, status=None, contract=None, size=None, iceberg=None, price=None, close=False, is_close=None, reduce_only=False, is_reduce_only=None, is_liq=None, tif='gtc', left=None, fill_price=None, text=None, tkfr=None, mkfr=None, refu=None, auto_size=None, stp_id=None, stp_act=None, amend_text=None, biz_info=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, int, float, float, str, str, str, int, int, str, bool, bool, bool, bool, bool, str, int, str, str, str, str, int, str, int, str, str, str, Configuration) -> None
        """FuturesOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user = None
        self._create_time = None
        self._finish_time = None
        self._finish_as = None
        self._status = None
        self._contract = None
        self._size = None
        self._iceberg = None
        self._price = None
        self._close = None
        self._is_close = None
        self._reduce_only = None
        self._is_reduce_only = None
        self._is_liq = None
        self._tif = None
        self._left = None
        self._fill_price = None
        self._text = None
        self._tkfr = None
        self._mkfr = None
        self._refu = None
        self._auto_size = None
        self._stp_id = None
        self._stp_act = None
        self._amend_text = None
        self._biz_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if finish_as is not None:
            self.finish_as = finish_as
        if status is not None:
            self.status = status
        self.contract = contract
        self.size = size
        if iceberg is not None:
            self.iceberg = iceberg
        if price is not None:
            self.price = price
        if close is not None:
            self.close = close
        if is_close is not None:
            self.is_close = is_close
        if reduce_only is not None:
            self.reduce_only = reduce_only
        if is_reduce_only is not None:
            self.is_reduce_only = is_reduce_only
        if is_liq is not None:
            self.is_liq = is_liq
        if tif is not None:
            self.tif = tif
        if left is not None:
            self.left = left
        if fill_price is not None:
            self.fill_price = fill_price
        if text is not None:
            self.text = text
        if tkfr is not None:
            self.tkfr = tkfr
        if mkfr is not None:
            self.mkfr = mkfr
        if refu is not None:
            self.refu = refu
        if auto_size is not None:
            self.auto_size = auto_size
        if stp_id is not None:
            self.stp_id = stp_id
        if stp_act is not None:
            self.stp_act = stp_act
        if amend_text is not None:
            self.amend_text = amend_text
        if biz_info is not None:
            self.biz_info = biz_info

    @property
    def id(self):
        """Gets the id of this FuturesOrder.  # noqa: E501

        Futures order ID  # noqa: E501

        :return: The id of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FuturesOrder.

        Futures order ID  # noqa: E501

        :param id: The id of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this FuturesOrder.  # noqa: E501

        User ID  # noqa: E501

        :return: The user of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FuturesOrder.

        User ID  # noqa: E501

        :param user: The user of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def create_time(self):
        """Gets the create_time of this FuturesOrder.  # noqa: E501

        Creation time of order  # noqa: E501

        :return: The create_time of this FuturesOrder.  # noqa: E501
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FuturesOrder.

        Creation time of order  # noqa: E501

        :param create_time: The create_time of this FuturesOrder.  # noqa: E501
        :type: float
        """

        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this FuturesOrder.  # noqa: E501

        Order finished time. Not returned if order is open  # noqa: E501

        :return: The finish_time of this FuturesOrder.  # noqa: E501
        :rtype: float
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this FuturesOrder.

        Order finished time. Not returned if order is open  # noqa: E501

        :param finish_time: The finish_time of this FuturesOrder.  # noqa: E501
        :type: float
        """

        self._finish_time = finish_time

    @property
    def finish_as(self):
        """Gets the finish_as of this FuturesOrder.  # noqa: E501

        How the order was finished.  - filled: all filled - cancelled: manually cancelled - liquidated: cancelled because of liquidation - ioc: time in force is `IOC`, finish immediately - auto_deleveraged: finished by ADL - reduce_only: cancelled because of increasing position while `reduce-only` set- position_closed: cancelled because of position close - position_closed: canceled because the position was closed - reduce_out: only reduce positions by excluding hard-to-fill orders - stp: cancelled because self trade prevention   # noqa: E501

        :return: The finish_as of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._finish_as

    @finish_as.setter
    def finish_as(self, finish_as):
        """Sets the finish_as of this FuturesOrder.

        How the order was finished.  - filled: all filled - cancelled: manually cancelled - liquidated: cancelled because of liquidation - ioc: time in force is `IOC`, finish immediately - auto_deleveraged: finished by ADL - reduce_only: cancelled because of increasing position while `reduce-only` set- position_closed: cancelled because of position close - position_closed: canceled because the position was closed - reduce_out: only reduce positions by excluding hard-to-fill orders - stp: cancelled because self trade prevention   # noqa: E501

        :param finish_as: The finish_as of this FuturesOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["filled", "cancelled", "liquidated", "ioc", "auto_deleveraged", "reduce_only", "position_closed", "reduce_out", "stp"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and finish_as not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `finish_as` ({0}), must be one of {1}"  # noqa: E501
                .format(finish_as, allowed_values)
            )

        self._finish_as = finish_as

    @property
    def status(self):
        """Gets the status of this FuturesOrder.  # noqa: E501

        Order status  - `open`: waiting to be traded - `finished`: finished  # noqa: E501

        :return: The status of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FuturesOrder.

        Order status  - `open`: waiting to be traded - `finished`: finished  # noqa: E501

        :param status: The status of this FuturesOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "finished"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def contract(self):
        """Gets the contract of this FuturesOrder.  # noqa: E501

        Futures contract  # noqa: E501

        :return: The contract of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this FuturesOrder.

        Futures contract  # noqa: E501

        :param contract: The contract of this FuturesOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contract is None:  # noqa: E501
            raise ValueError("Invalid value for `contract`, must not be `None`")  # noqa: E501

        self._contract = contract

    @property
    def size(self):
        """Gets the size of this FuturesOrder.  # noqa: E501

        Order size. Specify positive number to make a bid, and negative number to ask  # noqa: E501

        :return: The size of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FuturesOrder.

        Order size. Specify positive number to make a bid, and negative number to ask  # noqa: E501

        :param size: The size of this FuturesOrder.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def iceberg(self):
        """Gets the iceberg of this FuturesOrder.  # noqa: E501

        Display size for iceberg order. 0 for non-iceberg. Note that you will have to pay the taker fee for the hidden size  # noqa: E501

        :return: The iceberg of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._iceberg

    @iceberg.setter
    def iceberg(self, iceberg):
        """Sets the iceberg of this FuturesOrder.

        Display size for iceberg order. 0 for non-iceberg. Note that you will have to pay the taker fee for the hidden size  # noqa: E501

        :param iceberg: The iceberg of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._iceberg = iceberg

    @property
    def price(self):
        """Gets the price of this FuturesOrder.  # noqa: E501

        Order price. 0 for market order with `tif` set as `ioc`  # noqa: E501

        :return: The price of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this FuturesOrder.

        Order price. 0 for market order with `tif` set as `ioc`  # noqa: E501

        :param price: The price of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def close(self):
        """Gets the close of this FuturesOrder.  # noqa: E501

        Set as `true` to close the position, with `size` set to 0  # noqa: E501

        :return: The close of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this FuturesOrder.

        Set as `true` to close the position, with `size` set to 0  # noqa: E501

        :param close: The close of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._close = close

    @property
    def is_close(self):
        """Gets the is_close of this FuturesOrder.  # noqa: E501

        Is the order to close position  # noqa: E501

        :return: The is_close of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_close

    @is_close.setter
    def is_close(self, is_close):
        """Sets the is_close of this FuturesOrder.

        Is the order to close position  # noqa: E501

        :param is_close: The is_close of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._is_close = is_close

    @property
    def reduce_only(self):
        """Gets the reduce_only of this FuturesOrder.  # noqa: E501

        Set as `true` to be reduce-only order  # noqa: E501

        :return: The reduce_only of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._reduce_only

    @reduce_only.setter
    def reduce_only(self, reduce_only):
        """Sets the reduce_only of this FuturesOrder.

        Set as `true` to be reduce-only order  # noqa: E501

        :param reduce_only: The reduce_only of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._reduce_only = reduce_only

    @property
    def is_reduce_only(self):
        """Gets the is_reduce_only of this FuturesOrder.  # noqa: E501

        Is the order reduce-only  # noqa: E501

        :return: The is_reduce_only of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_reduce_only

    @is_reduce_only.setter
    def is_reduce_only(self, is_reduce_only):
        """Sets the is_reduce_only of this FuturesOrder.

        Is the order reduce-only  # noqa: E501

        :param is_reduce_only: The is_reduce_only of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._is_reduce_only = is_reduce_only

    @property
    def is_liq(self):
        """Gets the is_liq of this FuturesOrder.  # noqa: E501

        Is the order for liquidation  # noqa: E501

        :return: The is_liq of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_liq

    @is_liq.setter
    def is_liq(self, is_liq):
        """Sets the is_liq of this FuturesOrder.

        Is the order for liquidation  # noqa: E501

        :param is_liq: The is_liq of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._is_liq = is_liq

    @property
    def tif(self):
        """Gets the tif of this FuturesOrder.  # noqa: E501

        Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee - fok: FillOrKill, fill either completely or none  # noqa: E501

        :return: The tif of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._tif

    @tif.setter
    def tif(self, tif):
        """Sets the tif of this FuturesOrder.

        Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee - fok: FillOrKill, fill either completely or none  # noqa: E501

        :param tif: The tif of this FuturesOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["gtc", "ioc", "poc", "fok"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tif not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tif` ({0}), must be one of {1}"  # noqa: E501
                .format(tif, allowed_values)
            )

        self._tif = tif

    @property
    def left(self):
        """Gets the left of this FuturesOrder.  # noqa: E501

        Size left to be traded  # noqa: E501

        :return: The left of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this FuturesOrder.

        Size left to be traded  # noqa: E501

        :param left: The left of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._left = left

    @property
    def fill_price(self):
        """Gets the fill_price of this FuturesOrder.  # noqa: E501

        Fill price of the order  # noqa: E501

        :return: The fill_price of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._fill_price

    @fill_price.setter
    def fill_price(self, fill_price):
        """Sets the fill_price of this FuturesOrder.

        Fill price of the order  # noqa: E501

        :param fill_price: The fill_price of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._fill_price = fill_price

    @property
    def text(self):
        """Gets the text of this FuturesOrder.  # noqa: E501

        User defined information. If not empty, must follow the rules below:  1. prefixed with `t-` 2. no longer than 28 bytes without `t-` prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.) Besides user defined information, reserved contents are listed below, denoting how the order is created:  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance   # noqa: E501

        :return: The text of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FuturesOrder.

        User defined information. If not empty, must follow the rules below:  1. prefixed with `t-` 2. no longer than 28 bytes without `t-` prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.) Besides user defined information, reserved contents are listed below, denoting how the order is created:  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance   # noqa: E501

        :param text: The text of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def tkfr(self):
        """Gets the tkfr of this FuturesOrder.  # noqa: E501

        Taker fee  # noqa: E501

        :return: The tkfr of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._tkfr

    @tkfr.setter
    def tkfr(self, tkfr):
        """Sets the tkfr of this FuturesOrder.

        Taker fee  # noqa: E501

        :param tkfr: The tkfr of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._tkfr = tkfr

    @property
    def mkfr(self):
        """Gets the mkfr of this FuturesOrder.  # noqa: E501

        Maker fee  # noqa: E501

        :return: The mkfr of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._mkfr

    @mkfr.setter
    def mkfr(self, mkfr):
        """Sets the mkfr of this FuturesOrder.

        Maker fee  # noqa: E501

        :param mkfr: The mkfr of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._mkfr = mkfr

    @property
    def refu(self):
        """Gets the refu of this FuturesOrder.  # noqa: E501

        Reference user ID  # noqa: E501

        :return: The refu of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._refu

    @refu.setter
    def refu(self, refu):
        """Sets the refu of this FuturesOrder.

        Reference user ID  # noqa: E501

        :param refu: The refu of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._refu = refu

    @property
    def auto_size(self):
        """Gets the auto_size of this FuturesOrder.  # noqa: E501

        Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  # noqa: E501

        :return: The auto_size of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._auto_size

    @auto_size.setter
    def auto_size(self, auto_size):
        """Sets the auto_size of this FuturesOrder.

        Set side to close dual-mode position. `close_long` closes the long side; while `close_short` the short one. Note `size` also needs to be set to 0  # noqa: E501

        :param auto_size: The auto_size of this FuturesOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["close_long", "close_short"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and auto_size not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `auto_size` ({0}), must be one of {1}"  # noqa: E501
                .format(auto_size, allowed_values)
            )

        self._auto_size = auto_size

    @property
    def stp_id(self):
        """Gets the stp_id of this FuturesOrder.  # noqa: E501

        Orders between users in the same `stp_id` group are not allowed to be self-traded  1. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker. 2. `stp_id` returns `0` by default for orders that have not been set for `STP group`  # noqa: E501

        :return: The stp_id of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._stp_id

    @stp_id.setter
    def stp_id(self, stp_id):
        """Sets the stp_id of this FuturesOrder.

        Orders between users in the same `stp_id` group are not allowed to be self-traded  1. If the `stp_id` of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the `stp_act` of the taker. 2. `stp_id` returns `0` by default for orders that have not been set for `STP group`  # noqa: E501

        :param stp_id: The stp_id of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._stp_id = stp_id

    @property
    def stp_act(self):
        """Gets the stp_act of this FuturesOrder.  # noqa: E501

        Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  1. After users join the `STP Group`, he can pass `stp_act` to limit the user's self-trade prevetion strategy. If `stp_act` is not passed, the default is `cn` strategy。 2. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter。 3. If the user did not use 'stp_act' when placing the order, 'stp_act' will return '-'  - cn: Cancel newest, Cancel new orders and keep old ones - co: Cancel oldest, Cancel old orders and keep new ones - cb: Cancel both, Both old and new orders will be cancelled  # noqa: E501

        :return: The stp_act of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._stp_act

    @stp_act.setter
    def stp_act(self, stp_act):
        """Sets the stp_act of this FuturesOrder.

        Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  1. After users join the `STP Group`, he can pass `stp_act` to limit the user's self-trade prevetion strategy. If `stp_act` is not passed, the default is `cn` strategy。 2. When the user does not join the `STP group`, an error will be returned when passing the `stp_act` parameter。 3. If the user did not use 'stp_act' when placing the order, 'stp_act' will return '-'  - cn: Cancel newest, Cancel new orders and keep old ones - co: Cancel oldest, Cancel old orders and keep new ones - cb: Cancel both, Both old and new orders will be cancelled  # noqa: E501

        :param stp_act: The stp_act of this FuturesOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["co", "cn", "cb", "-"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and stp_act not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `stp_act` ({0}), must be one of {1}"  # noqa: E501
                .format(stp_act, allowed_values)
            )

        self._stp_act = stp_act

    @property
    def amend_text(self):
        """Gets the amend_text of this FuturesOrder.  # noqa: E501

        The custom data that the user remarked when amending the order  # noqa: E501

        :return: The amend_text of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._amend_text

    @amend_text.setter
    def amend_text(self, amend_text):
        """Sets the amend_text of this FuturesOrder.

        The custom data that the user remarked when amending the order  # noqa: E501

        :param amend_text: The amend_text of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._amend_text = amend_text

    @property
    def biz_info(self):
        """Gets the biz_info of this FuturesOrder.  # noqa: E501

        Additional information  # noqa: E501

        :return: The biz_info of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._biz_info

    @biz_info.setter
    def biz_info(self, biz_info):
        """Sets the biz_info of this FuturesOrder.

        Additional information  # noqa: E501

        :param biz_info: The biz_info of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._biz_info = biz_info

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
        if not isinstance(other, FuturesOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FuturesOrder):
            return True

        return self.to_dict() != other.to_dict()
