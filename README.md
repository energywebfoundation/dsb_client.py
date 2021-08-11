# dsb_client

Python client for use with the Energy Web DSB Message Broker. Some understanding
of the DSB is required (DID-based authentication via Energy Web Switchboard) and
can be found in the documentation on https://github.com/energywebfoundation/dsb.

This client was generated from the DSB Message Broker's Swagger documentation.
An additional (thin) client was written to wrap the generated `swagger_client`
and provide a cleaner API (mostly in keeping with previous versions of this
client).

To get started with the client:
```sh
git clone {this_repo}
cd {this_repo}
python3 -m venv venv # substitute with your preferred method
source ./venv/bin/activate
python setup.py install
```

An example usage of the client has been provided in [examples](./examples). We
will be adding additional examples as we develop the DSB.

To run the example (while still in your virtual env):
```
python examples/login_and_get_messages.py
```

In the example, a private key is provided, which already has the user role. You
will need to substitute this for your own private key. See the DSB Message Broker
for more information about using your private key to obtain a Decentralized
Identifier (DID) and enrol as a user of the EW Distributed Service Bus.

The client will also be distributed via PyPI in the near future.

# swagger-client
Swagger documentation for the DSB Message Broker API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import dsb_client.swagger_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dsb_client.swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import dsb_client.swagger_client
from dsb_client.swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoginDataDTO() # LoginDataDTO |

try:
    api_response = api_instance.auth_controller_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_controller_login: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_controller_login**](docs/AuthApi.md#auth_controller_login) | **POST** /auth/login |
*ChannelApi* | [**channel_controller_create**](docs/ChannelApi.md#channel_controller_create) | **POST** /channel |
*HealthApi* | [**health_controller_check**](docs/HealthApi.md#health_controller_check) | **GET** /health |
*MessageApi* | [**message_controller_get_new_from_channel**](docs/MessageApi.md#message_controller_get_new_from_channel) | **GET** /message |
*MessageApi* | [**message_controller_publish**](docs/MessageApi.md#message_controller_publish) | **POST** /message |

## Documentation For Models

 - [CreateChannelDto](docs/CreateChannelDto.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse200Info](docs/InlineResponse200Info.md)
 - [InlineResponse503](docs/InlineResponse503.md)
 - [LoginDataDTO](docs/LoginDataDTO.md)
 - [LoginReturnDataDTO](docs/LoginReturnDataDTO.md)
 - [MessageDTO](docs/MessageDTO.md)
 - [PublishMessageDto](docs/PublishMessageDto.md)

## Documentation For Authorization


## access-token



## Author
