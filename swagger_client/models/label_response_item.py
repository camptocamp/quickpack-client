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

class LabelResponseItem(object):
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
        'ident_code': 'str',
        'label': 'str',
        'item_id': 'str',
        'errors': 'list[MessageType]',
        'warnings': 'list[MessageType]'
    }

    attribute_map = {
        'ident_code': 'IdentCode',
        'label': 'Label',
        'item_id': 'ItemID',
        'errors': 'Errors',
        'warnings': 'Warnings'
    }

    def __init__(self, ident_code=None, label=None, item_id=None, errors=None, warnings=None):  # noqa: E501
        """LabelResponseItem - a model defined in Swagger"""  # noqa: E501
        self._ident_code = None
        self._label = None
        self._item_id = None
        self._errors = None
        self._warnings = None
        self.discriminator = None
        if ident_code is not None:
            self.ident_code = ident_code
        if label is not None:
            self.label = label
        if item_id is not None:
            self.item_id = item_id
        if errors is not None:
            self.errors = errors
        if warnings is not None:
            self.warnings = warnings

    @property
    def ident_code(self):
        """Gets the ident_code of this LabelResponseItem.  # noqa: E501


        :return: The ident_code of this LabelResponseItem.  # noqa: E501
        :rtype: str
        """
        return self._ident_code

    @ident_code.setter
    def ident_code(self, ident_code):
        """Sets the ident_code of this LabelResponseItem.


        :param ident_code: The ident_code of this LabelResponseItem.  # noqa: E501
        :type: str
        """

        self._ident_code = ident_code

    @property
    def label(self):
        """Gets the label of this LabelResponseItem.  # noqa: E501


        :return: The label of this LabelResponseItem.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LabelResponseItem.


        :param label: The label of this LabelResponseItem.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def item_id(self):
        """Gets the item_id of this LabelResponseItem.  # noqa: E501


        :return: The item_id of this LabelResponseItem.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this LabelResponseItem.


        :param item_id: The item_id of this LabelResponseItem.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def errors(self):
        """Gets the errors of this LabelResponseItem.  # noqa: E501


        :return: The errors of this LabelResponseItem.  # noqa: E501
        :rtype: list[MessageType]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this LabelResponseItem.


        :param errors: The errors of this LabelResponseItem.  # noqa: E501
        :type: list[MessageType]
        """

        self._errors = errors

    @property
    def warnings(self):
        """Gets the warnings of this LabelResponseItem.  # noqa: E501


        :return: The warnings of this LabelResponseItem.  # noqa: E501
        :rtype: list[MessageType]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this LabelResponseItem.


        :param warnings: The warnings of this LabelResponseItem.  # noqa: E501
        :type: list[MessageType]
        """

        self._warnings = warnings

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
        if issubclass(LabelResponseItem, dict):
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
        if not isinstance(other, LabelResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
