from nose.tools import *
import re
import requests

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):

    assert status in resp.status, "Expected response %r not in %r" % (status, resp.status)

    if status == "200":
        assert resp.data, "Response data is empty."

    if contains:
        assert contains in resp.data, "Response does not contain %r" % contains

    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.data), "Response does not match %r" % matches

    if headers:
        assert_equal(resp.headers, headers)

def assertResponse(resp, contains=None, matches=None, headers=None, status=200):

    assert status == resp.status_code, "Expected response %r not %r" % (status, resp.status_code)

    if status == 200:
        assert resp.text, "Response data is empty."

    if contains:
        assert contains in resp.text, "Response does not contain %r" % contains

    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.text), "Response does not match %r" % matches

    if headers:
        assert_equal(resp.headers, headers)

def get_session_id(resp):
    cookies_str = resp.headers['Set-Cookie']
    if cookies_str:
        for kv in cookies_str.split(';'):
            if 'webpy_session_id=' in kv:
                return kv

def get_location(resp):
    location = resp.headers['Location']
    return location


