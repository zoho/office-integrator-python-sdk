<a href="https://zoho.com/catalyst/">
    <img width="300" src="https://www.zohowebstatic.com/sites/zweb/images/productlogos/officeintegrator.svg">
</a>

# Python SDK
![PyPI](https://img.shields.io/pypi/v/office-integrator-sdk) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/office-integrator-sdk) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/office-integrator-sdk) ![PyPI - License](https://img.shields.io/pypi/l/office-integrator-sdk)
* [Getting Started](#Getting-Started)
* [Prerequisites](#prerequisites)
* [Registering a Zoho Office Integrator APIKey](#registering-a-zoho-office-integrator-apikey)
* [Including the SDK in your project](#including-the-sdk-in-your-project)
* [Sample Code](#sdk-sample-code)
* [Release Notes](#release-notes)
* [License](#license)

## Getting Started

Zoho Office Integrator Pythod SDK used to help you quickly integrator Zoho Office Integrator editors in side your web application.

* [Python SDK Source code](https://github.com/zoho/office-integrator-python-sdk)
* [API reference documentation](https://www.zoho.com/officeintegrator/api/v1)
* [SDK example code](https://github.com/zoho/office-integrator-python-sdk-examples)

## Prerequisites

- To start working with this SDK you need a an account in office integrator service. [Sign Up](https://officeintegrator.zoho.com)

- You need to install suitable version of [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installation/)


## Registering a Zoho Office Integrator APIKey

Since Zoho Office Integrator APIs are authenticated with apikey, you should register your with Zoho to get an apikey. To register your app:

- Follow the steps mentioned in this help [page](https://www.zoho.com/officeintegrator/api/v1/getting-started.html) ( Sign-up for a Zoho Account if you don't have one)

- Enter your company name and short discription about how you are going to using zoho office integrator with your application in apikey sign-up form. Choose the type of your application(commerial or non-commercial) and generate the apikey.

- After sign-up completed for Zoho Office Integrator service, copy the apikey from the dashboard.

## Including the SDK in your project

You can include the SDK to your project using:

- Install **Python SDK**
    - Navigate to the workspace of your client app.
    - Run the command below:

    ```sh
    pip install office-integrator-sdk
    ```

- Another method to install the SDK
    - Add following line in requirements.txt file of your application.
    
     ```sh
    office-integrator-sdk==1.0.0b2
    ```
    - Run the follwoing comment install the sdk files
     ```sh
    pip3 install -r requirements.txt
    ```

## SDK Sample code

Refer this **[repository](https://github.com/zoho/office-integrator-python-sdk-examples)** for example codes to all Office Integrator API endpoints.

## Release Notes

*Version 1.0.b2*

- Readme file and license details updated

*Version 1.0.b1*

- Initial sdk version release

## License

This SDK is distributed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0), see LICENSE.txt for more information.