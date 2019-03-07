from nose.tools import *
from gothonweb.sesapp import app
from tests.tools import assert_response
from tests.tools import get_session_id

session_id = None

def setup_module():
    setUpSession()

def setUpSession():
# check that we get a 303 on the / URL
    global session_id
    resp = app.request("/")
    assert_response(resp, status="303 See Other")

# check that a session id is created
    session_id = get_session_id(resp)
    assert_true(session_id)

def testGame():
# make next request to /game setting session id
# in cookies
    resp1 = app.request('/game', headers={'Cookie':session_id})
    assert_response(resp1, status='200', contains='Central Corridor')

def teardown_module():
    pass

