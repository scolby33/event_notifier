import json
import urllib

import responses
import requests

from tests.constants import *

class MockPushoverServer(object):
    """A mock Pushover server using the responses package"""
    def __init__(self):
        responses.add_callback(
            responses.POST,
            'https://api.pushover.net:443/1/messages.json',
            callback = self._request_callback
        )
        
    @classmethod
    def _request_callback(cls, request):
        payload = urllib.parse.parse_qs(request.body)
        headers = {'Content-Type': 'application/json; charset=utf-8', 'X-Request-Id': TEST_REQUEST_ID}
        if cls._verify_parameters(payload):
            return (200, headers, json.dumps({'status': 1, 'request': TEST_REQUEST_ID}))
        # TODO: deal with bad requests in a real way
        return (400, headers, json.dumps('fail'))
    
    @staticmethod
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
        for k, v in params_to_check.items():
            if not payload[k] and not v['optional']:
                return k
            if not isinstance(payload[k], v['type']):
                return k
            if v['valid_values']:
                if not payload[k] in v['valid_values']:
                    return k
        return True
