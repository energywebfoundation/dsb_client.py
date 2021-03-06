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

class LoginReturnDataDTO(object):
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
        'token': 'str',
        'did': 'str',
        'address': 'str',
        'signature': 'str'
    }

    attribute_map = {
        'token': 'token',
        'did': 'did',
        'address': 'address',
        'signature': 'signature'
    }

    def __init__(self, token=None, did=None, address=None, signature=None):  # noqa: E501
        """LoginReturnDataDTO - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._did = None
        self._address = None
        self._signature = None
        self.discriminator = None
        self.token = token
        self.did = did
        self.address = address
        self.signature = signature

    @property
    def token(self):
        """Gets the token of this LoginReturnDataDTO.  # noqa: E501

        Bearer token used in HTTP \"Authentication\" header to authorize subsequent requests  # noqa: E501

        :return: The token of this LoginReturnDataDTO.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this LoginReturnDataDTO.

        Bearer token used in HTTP \"Authentication\" header to authorize subsequent requests  # noqa: E501

        :param token: The token of this LoginReturnDataDTO.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def did(self):
        """Gets the did of this LoginReturnDataDTO.  # noqa: E501

        DID of messagebroker which is the DID identifier corresponding to env.PRIVATE_KEY  # noqa: E501

        :return: The did of this LoginReturnDataDTO.  # noqa: E501
        :rtype: str
        """
        return self._did

    @did.setter
    def did(self, did):
        """Sets the did of this LoginReturnDataDTO.

        DID of messagebroker which is the DID identifier corresponding to env.PRIVATE_KEY  # noqa: E501

        :param did: The did of this LoginReturnDataDTO.  # noqa: E501
        :type: str
        """
        if did is None:
            raise ValueError("Invalid value for `did`, must not be `None`")  # noqa: E501

        self._did = did

    @property
    def address(self):
        """Gets the address of this LoginReturnDataDTO.  # noqa: E501

        address of the env.PRIVATE_KEY for signature recovery purposes  # noqa: E501

        :return: The address of this LoginReturnDataDTO.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this LoginReturnDataDTO.

        address of the env.PRIVATE_KEY for signature recovery purposes  # noqa: E501

        :param address: The address of this LoginReturnDataDTO.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def signature(self):
        """Gets the signature of this LoginReturnDataDTO.  # noqa: E501

        the compact hex signature which is ECDSA hash(address of privatekey+messagebrokerDID+userDID)  # noqa: E501

        :return: The signature of this LoginReturnDataDTO.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this LoginReturnDataDTO.

        the compact hex signature which is ECDSA hash(address of privatekey+messagebrokerDID+userDID)  # noqa: E501

        :param signature: The signature of this LoginReturnDataDTO.  # noqa: E501
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
        if issubclass(LoginReturnDataDTO, dict):
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
        if not isinstance(other, LoginReturnDataDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
