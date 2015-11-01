import json
import urllib

import pytest

import responses
import requests

from tests.constants import *

@pytest.fixture
def mock_pushover_server(request):
    """A fixture to mock requests to the Pushover API"""
    responses.add_callback(
        responses.POST,
        'https://api.pushover.net:443/1/messages.json',
        callback = _request_callback
    )
    def fin():
        responses.reset()
    request.addfinalizer(fin)
    
@pytest.fixture
def mock_bad_pushover_server(request):
    """A fixture that pretends the Pushover API isn't accepting even valid requests"""
    responses.add(
        responses.POST,
        'https://api.pushover.net:443/1/messages.json',
        body = json.dumps({'error': 'server failure'}),
        status = 500,
        content_type = 'application/json'
    )
    def fin():
        responses.reset()
    request.addfinalizer(fin)
    
def _request_callback(request):
    payload = urllib.parse.parse_qs(request.body)
    headers = {'Content-Type': 'application/json; charset=utf-8', 'X-Request-Id': TEST_REQUEST_ID}
    if _verify_payload(payload):
        return (200, headers, json.dumps({'status': 1, 'request': TEST_REQUEST_ID}))
    # TODO: deal with bad requests in a real way
    return (400, headers, json.dumps('fail'))
    
def _verify_payload(payload):
    """Verify that the passed-in payload meets Pushover's requirements

    :param payload: the payload to be verified
    :type payload: dict
    :returns: True if the payload is valid, a str containing the name of the invalid parameter otherwise
    :rtype: bool or str
    """
    params_to_check = {
        'token': {
            'optional': False,
            'type': str,
            'valid_values': [TEST_TOKEN]
        },
        'user': {
            'optional': False,
            'type': str,
            'valid_values': [TEST_USER]
        },
        'title': {
            'optional': True,
            'type': str
        },
        'message': {
            'optional': False,
            'type': str
        },
        'device': {
            'optional': True,
            'type': str
        },
        'url': {
            'optional': True,
            'type': str
        },
        'url_title': {
            'optional': True,
            'type': str
        },
        'priority': {
            'optional': True,
            'type': int,
            'valid_values': [-2, -1, 0, 1, 2]
        },
        'timestamp': {
            'optional': True,
            'type': int,
        },
        'sound': {
            'optional': True,
            'type': str
        }
    }
    for param, requirements in params_to_check.items():
        if param not in payload and not requirements['optional']:
            return param
        if not isinstance(payload[param], requirements['type']):
            return param
        if 'valid_values' in requirements and payload[param] not in requirements['valid_values']:
            return param
    return True
