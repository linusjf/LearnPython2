from nose.tools import *
from tests.tools import assertResponse
from tests.tools import get_session_id
import requests
from gothonweb import map

url = 'http://localhost:8080'
session = None

def setup_module():
    setUpSession()

def setUpSession():

    global session
    session = requests.session()
    session.allow_redirects = True
    resp = session.get(url)
    assertResponse(resp, status=200)

# check that a session id is created
    session_id = get_session_id(resp)
    assert_true(session_id)
    
def invokeGetGame(relPath=''):
    return session.get(url+relPath)

def invokePostGame(data={}):
    return session.post(url=url+'/game',data=data)

def testShoot():
    
    resp1 = invokeGetGame('/game')
    assertResponse(resp1, status=200, contains='Central Corridor')
    resp1 = invokePostGame(data={'action':'shoot!'})
    assertResponse(resp1, status=200, contains=map.generic_death.name)

def testDodge():
    
    resp1 = invokeGetGame()
    assertResponse(resp1, status=200, contains='Central Corridor')
    resp1 = invokePostGame(data={'action':'dodge!'})
    assertResponse(resp1, status=200, contains=map.generic_death.name)

def testTellAJoke():

    resp1 = invokeGetGame()
    assertResponse(resp1, status=200, contains='Central Corridor')
    resp1 = invokePostGame(data={'action':'tell a joke'})
    assertResponse(resp1, status=200, contains=map.laser_weapon_armory.name)



def teardown_module():
    pass

