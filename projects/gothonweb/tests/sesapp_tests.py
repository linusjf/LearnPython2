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
       
def invokeGetGame(relPath=''):
    global url
    return session.get(url+relPath)

def invokePostGame(data={}):
    global url
    return session.post(url=url+'/game',data=data)

def invokeLaserWeaponArmory():
    invokeGetGame('')
    return invokePostGame(
            data={'action':'tell a joke'})

def invokeTheBridge():
    invokeLaserWeaponArmory()
    return invokePostGame(data={'action':'0132'})

def invokeEscapePod():
    resp = invokeTheBridge()
    return invokePostGame(
            data={'action':'slowly place the bomb'})

def invokeEndWinner():
    invokeEscapePod()
    return invokePostGame(data={'action':'2'})

def testSessionID():
    # check that a session id is created
    resp = session.get(url)
    session_id = get_session_id(resp)
    assert_true(session_id)

def testShoot():
    resp1 = invokeGetGame('/game')
    assertResponse(resp1, status=200,
            contains='Central Corridor')
    resp1 = invokePostGame(
            data={'action':'shoot!'})
    assertResponse(resp1,
            status=200,
            contains=map.generic_death.name)

def testDodge():
    resp1 = invokeGetGame()
    assertResponse(resp1,
            status=200,
            contains='Central Corridor')
    resp1 = invokePostGame(data={'action':'dodge!'})
    assertResponse(resp1,
            status=200,
            contains=map.generic_death.name)

def testTellAJoke():
    resp1 = invokeGetGame()
    assertResponse(resp1,
            status=200,
            contains='Central Corridor')
    resp1 = invokePostGame(
            data={'action':'tell a joke'})
    assertResponse(resp1,
            status=200,
            contains=map.laser_weapon_armory.name)

def testCentralCorridorError():
    resp1 = invokeGetGame()
    assertResponse(resp1,
            status=200,
            contains='Central Corridor')
    resp1 = invokePostGame(
            data={'action':'*'})
    assertResponse(resp1,
            status=200,
            contains='The End')

def testInputCode():
    resp = invokeLaserWeaponArmory()
    resp1 = invokePostGame(data={'action':'0132'})
    assertResponse(resp1,
            status=200,
            contains=map.the_bridge.name)

def testInputCodeError():
    resp = invokeLaserWeaponArmory()
    resp1 = invokePostGame(data={'action':'*'})
    assertResponse(resp1,
            status=200,
            contains=map.generic_death.name)


def testTheBridge():
    resp = invokeTheBridge()
    resp = invokePostGame(
            data={'action':'slowly place the bomb'})
    assertResponse(resp,
            status=200,
            contains=map.escape_pod.name)

def testTheBridgeError():
    resp = invokeTheBridge()
    resp = invokePostGame(data=
            {'action':'throw the bomb'})
    assertResponse(resp,
            status=200,
            contains=map.generic_death.name)


def testEscapePod():
    resp = invokeEscapePod()
    resp = invokePostGame(data={'action':'2'})
    assertResponse(resp,
            status=200,
            contains=map.the_end_winner.name)

def testEscapePodError():
    resp = invokeEscapePod()                    
    resp = invokePostGame(data={'action':'5'})
    assertResponse(resp,status=200,
            contains=map.the_end_loser.name)   

