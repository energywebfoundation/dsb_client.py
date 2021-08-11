# coding: utf-8

"""
    DSB Message Broker API

    Swagger documentation for the DSB Message Broker API  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PublishMessageDto(object):
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
        'fqcn': 'str',
        'payload': 'str',
        'signature': 'str'
    }

    attribute_map = {
        'fqcn': 'fqcn',
        'payload': 'payload',
        'signature': 'signature'
    }

    def __init__(self, fqcn=None, payload=None, signature=None):  # noqa: E501
        """PublishMessageDto - a model defined in Swagger"""  # noqa: E501
        self._fqcn = None
        self._payload = None
        self._signature = None
        self.discriminator = None
        self.fqcn = fqcn
        self.payload = payload
        self.signature = signature

    @property
    def fqcn(self):
        """Gets the fqcn of this PublishMessageDto.  # noqa: E501

        Fully qualified channel name (fcqn)  # noqa: E501

        :return: The fqcn of this PublishMessageDto.  # noqa: E501
        :rtype: str
        """
        return self._fqcn

    @fqcn.setter
    def fqcn(self, fqcn):
        """Sets the fqcn of this PublishMessageDto.

        Fully qualified channel name (fcqn)  # noqa: E501

        :param fqcn: The fqcn of this PublishMessageDto.  # noqa: E501
        :type: str
        """
        if fqcn is None:
            raise ValueError("Invalid value for `fqcn`, must not be `None`")  # noqa: E501

        self._fqcn = fqcn

    @property
    def payload(self):
        """Gets the payload of this PublishMessageDto.  # noqa: E501

        Any stringified payload like JSON, BASE64 etc  # noqa: E501

        :return: The payload of this PublishMessageDto.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this PublishMessageDto.

        Any stringified payload like JSON, BASE64 etc  # noqa: E501

        :param payload: The payload of this PublishMessageDto.  # noqa: E501
        :type: str
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def signature(self):
        """Gets the signature of this PublishMessageDto.  # noqa: E501

        Compacted EcdsaSecp256k1Signature2019  # noqa: E501

        :return: The signature of this PublishMessageDto.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this PublishMessageDto.

        Compacted EcdsaSecp256k1Signature2019  # noqa: E501

        :param signature: The signature of this PublishMessageDto.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

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
        if issubclass(PublishMessageDto, dict):
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
        if not isinstance(other, PublishMessageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
