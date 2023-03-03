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


class SubAccount(object):
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
        'remark': 'str',
        'login_name': 'str',
        'password': 'str',
        'email': 'str',
        'state': 'int',
        'type': 'int',
        'user_id': 'int',
        'create_time': 'int',
    }

    attribute_map = {
        'remark': 'remark',
        'login_name': 'login_name',
        'password': 'password',
        'email': 'email',
        'state': 'state',
        'type': 'type',
        'user_id': 'user_id',
        'create_time': 'create_time',
    }

    def __init__(
        self,
        remark=None,
        login_name=None,
        password=None,
        email=None,
        state=None,
        type=None,
        user_id=None,
        create_time=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, int, int, int, int, Configuration) -> None
        """SubAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._remark = None
        self._login_name = None
        self._password = None
        self._email = None
        self._state = None
        self._type = None
        self._user_id = None
        self._create_time = None
        self.discriminator = None

        if remark is not None:
            self.remark = remark
        self.login_name = login_name
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if user_id is not None:
            self.user_id = user_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def remark(self):
        """Gets the remark of this SubAccount.  # noqa: E501

        custom text  # noqa: E501

        :return: The remark of this SubAccount.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this SubAccount.

        custom text  # noqa: E501

        :param remark: The remark of this SubAccount.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def login_name(self):
        """Gets the login_name of this SubAccount.  # noqa: E501

        Sub-account login name: Only letters, numbers and underscores are supported, and cannot contain other illegal characters  # noqa: E501

        :return: The login_name of this SubAccount.  # noqa: E501
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this SubAccount.

        Sub-account login name: Only letters, numbers and underscores are supported, and cannot contain other illegal characters  # noqa: E501

        :param login_name: The login_name of this SubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and login_name is None:  # noqa: E501
            raise ValueError("Invalid value for `login_name`, must not be `None`")  # noqa: E501

        self._login_name = login_name

    @property
    def password(self):
        """Gets the password of this SubAccount.  # noqa: E501

        The sub-account's password. (Default: the same as main account's password)  # noqa: E501

        :return: The password of this SubAccount.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SubAccount.

        The sub-account's password. (Default: the same as main account's password)  # noqa: E501

        :param password: The password of this SubAccount.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """Gets the email of this SubAccount.  # noqa: E501

        The sub-account's email address. (Default: the same as main account's email address)  # noqa: E501

        :return: The email of this SubAccount.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SubAccount.

        The sub-account's email address. (Default: the same as main account's email address)  # noqa: E501

        :param email: The email of this SubAccount.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def state(self):
        """Gets the state of this SubAccount.  # noqa: E501

        State: 1-normal, 2-locked\"  # noqa: E501

        :return: The state of this SubAccount.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubAccount.

        State: 1-normal, 2-locked\"  # noqa: E501

        :param state: The state of this SubAccount.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def type(self):
        """Gets the type of this SubAccount.  # noqa: E501

        Type: 1-Sub-account  # noqa: E501

        :return: The type of this SubAccount.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubAccount.

        Type: 1-Sub-account  # noqa: E501

        :param type: The type of this SubAccount.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def user_id(self):
        """Gets the user_id of this SubAccount.  # noqa: E501

        The user id of the sub-account  # noqa: E501

        :return: The user_id of this SubAccount.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SubAccount.

        The user id of the sub-account  # noqa: E501

        :param user_id: The user_id of this SubAccount.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def create_time(self):
        """Gets the create_time of this SubAccount.  # noqa: E501

        Created time  # noqa: E501

        :return: The create_time of this SubAccount.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SubAccount.

        Created time  # noqa: E501

        :param create_time: The create_time of this SubAccount.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

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
        if not isinstance(other, SubAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubAccount):
            return True

        return self.to_dict() != other.to_dict()
