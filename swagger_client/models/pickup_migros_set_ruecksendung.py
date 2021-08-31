# coding: utf-8

"""
    Quickpac API

    Here you will find all public interfaces to the Quickpac system.  # noqa: E501

    OpenAPI spec version: v1.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PickupMigrosSetRuecksendung(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'use_production': 'bool',
        'validation_only': 'bool',
        'password': 'str',
        'barcode_nr': 'str',
        'abholort_id': 'str'
    }

    attribute_map = {
        'use_production': 'UseProduction',
        'validation_only': 'ValidationOnly',
        'password': 'Password',
        'barcode_nr': 'BarcodeNr',
        'abholort_id': 'AbholortID'
    }

    def __init__(self, use_production=None, validation_only=None, password=None, barcode_nr=None, abholort_id=None):  # noqa: E501
        """PickupMigrosSetRuecksendung - a model defined in Swagger"""  # noqa: E501
        self._use_production = None
        self._validation_only = None
        self._password = None
        self._barcode_nr = None
        self._abholort_id = None
        self.discriminator = None
        if use_production is not None:
            self.use_production = use_production
        if validation_only is not None:
            self.validation_only = validation_only
        if password is not None:
            self.password = password
        if barcode_nr is not None:
            self.barcode_nr = barcode_nr
        if abholort_id is not None:
            self.abholort_id = abholort_id

    @property
    def use_production(self):
        """Gets the use_production of this PickupMigrosSetRuecksendung.  # noqa: E501


        :return: The use_production of this PickupMigrosSetRuecksendung.  # noqa: E501
        :rtype: bool
        """
        return self._use_production

    @use_production.setter
    def use_production(self, use_production):
        """Sets the use_production of this PickupMigrosSetRuecksendung.


        :param use_production: The use_production of this PickupMigrosSetRuecksendung.  # noqa: E501
        :type: bool
        """

        self._use_production = use_production

    @property
    def validation_only(self):
        """Gets the validation_only of this PickupMigrosSetRuecksendung.  # noqa: E501


        :return: The validation_only of this PickupMigrosSetRuecksendung.  # noqa: E501
        :rtype: bool
        """
        return self._validation_only

    @validation_only.setter
    def validation_only(self, validation_only):
        """Sets the validation_only of this PickupMigrosSetRuecksendung.


        :param validation_only: The validation_only of this PickupMigrosSetRuecksendung.  # noqa: E501
        :type: bool
        """

        self._validation_only = validation_only

    @property
    def password(self):
        """Gets the password of this PickupMigrosSetRuecksendung.  # noqa: E501


        :return: The password of this PickupMigrosSetRuecksendung.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PickupMigrosSetRuecksendung.


        :param password: The password of this PickupMigrosSetRuecksendung.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def barcode_nr(self):
        """Gets the barcode_nr of this PickupMigrosSetRuecksendung.  # noqa: E501


        :return: The barcode_nr of this PickupMigrosSetRuecksendung.  # noqa: E501
        :rtype: str
        """
        return self._barcode_nr

    @barcode_nr.setter
    def barcode_nr(self, barcode_nr):
        """Sets the barcode_nr of this PickupMigrosSetRuecksendung.


        :param barcode_nr: The barcode_nr of this PickupMigrosSetRuecksendung.  # noqa: E501
        :type: str
        """

        self._barcode_nr = barcode_nr

    @property
    def abholort_id(self):
        """Gets the abholort_id of this PickupMigrosSetRuecksendung.  # noqa: E501


        :return: The abholort_id of this PickupMigrosSetRuecksendung.  # noqa: E501
        :rtype: str
        """
        return self._abholort_id

    @abholort_id.setter
    def abholort_id(self, abholort_id):
        """Sets the abholort_id of this PickupMigrosSetRuecksendung.


        :param abholort_id: The abholort_id of this PickupMigrosSetRuecksendung.  # noqa: E501
        :type: str
        """

        self._abholort_id = abholort_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PickupMigrosSetRuecksendung, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PickupMigrosSetRuecksendung):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
