Flamock
==========
[![Build Status](https://travis-ci.org/Travix-International/flamock.svg?branch=master)](https://travis-ci.org/Travix-International/flamock)

# Overview
Inspired by mock-server and wiremock. Implementation of mock server in Python + Flask.
All incoming requests are validated according saved expectations.
One expectation can describe following behavior:
* Send prepared response
* Forward request to particular host

# Functions
* Add expectation
* Remove expectation
* Remove all expectations

* Forward request
* Send response to request

# Examples
Add a response with http code 503 for all requests with tag label 
POST /flamock/add_expectation
Body:
{
  "key": "503",
  "request": {
    "body": ".*<label>*"
  },
  "response": {
    "httpcode": 503,
    "body": "Answer from mock"
  },
  "unlimited": true,
  "priority": 1
}

# License
MIT © Travix International
