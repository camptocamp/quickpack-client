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

class LabelDataProviderSending(object):
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
        'sending_id': 'str',
        'item': 'list[Item]'
    }

    attribute_map = {
        'sending_id': 'SendingID',
        'item': 'Item'
    }

    def __init__(self, sending_id=None, item=None):  # noqa: E501
        """LabelDataProviderSending - a model defined in Swagger"""  # noqa: E501
        self._sending_id = None
        self._item = None
        self.discriminator = None
        if sending_id is not None:
            self.sending_id = sending_id
        if item is not None:
            self.item = item

    @property
    def sending_id(self):
        """Gets the sending_id of this LabelDataProviderSending.  # noqa: E501


        :return: The sending_id of this LabelDataProviderSending.  # noqa: E501
        :rtype: str
        """
        return self._sending_id

    @sending_id.setter
    def sending_id(self, sending_id):
        """Sets the sending_id of this LabelDataProviderSending.


        :param sending_id: The sending_id of this LabelDataProviderSending.  # noqa: E501
        :type: str
        """

        self._sending_id = sending_id

    @property
    def item(self):
        """Gets the item of this LabelDataProviderSending.  # noqa: E501


        :return: The item of this LabelDataProviderSending.  # noqa: E501
        :rtype: list[Item]
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this LabelDataProviderSending.


        :param item: The item of this LabelDataProviderSending.  # noqa: E501
        :type: list[Item]
        """

        self._item = item

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
        if issubclass(LabelDataProviderSending, dict):
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
        if not isinstance(other, LabelDataProviderSending):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
