import datetime
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
    res = _verify_payload(payload)
    if 0 == len(res):
        return (200, headers, json.dumps({'status': 1, 'request': TEST_REQUEST_ID}))
    else:
        return (400, headers, json.dumps({"bad_parameters": res}))
    
def _verify_payload(payload):
    """Verify that the passed-in payload meets Pushover's requirements

    :param payload: the payload to be verified
    :type payload: dict
    :returns: a list of the parameters with erroneous values
    :rtype: list
    """
    params_to_check = {
        'token': {
            'optional': False,
            'valid_values': {TEST_TOKEN}
        },
        'user': {
            'optional': False,
            'valid_values': {TEST_USER}
        },
        'title': {
            'optional': True
        },
        'message': {
            'optional': False
        },
        'device': {
            'optional': True
        },
        'url': {
            'optional': True
        },
        'url_title': {
            'optional': True
        },
        'priority': {
            'optional': True,
            'valid_values': {'-2', '-1', '0', '1', '2'}
        },
        'timestamp': {
            'optional': True
        },
        'sound': {
            'optional': True
        }
    }
    malformed_params = []
    
    for param, requirements in params_to_check.items():
        if param not in payload:
            if not requirements['optional']:
                malformed_params.append((param, 'missing'))
        elif 'valid_values' in requirements and payload[param][-1] not in requirements['valid_values']:
            malformed_params.append((param, 'invalid_value'))
        elif param == 'timestamp':
            try:
                datetime.datetime.fromtimestamp(int(payload[param][-1]))
            except:
                malformed_params.append((param, 'invalid_timestamp_value'))
                
    return malformed_params
