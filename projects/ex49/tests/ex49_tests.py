from nose.tools import *
from ex49 import parser

def test_peek():
    tuple = [('direction','north')]
    result = parser.peek(tuple)
    assert_equal(result,'direction')
    tuple = []
    result = parser.peek(tuple)
    assert_equal(result,None)
 
def test_match():
    tuple = [('direction','north')]
    result = parser.match(tuple,'direction')
    assert_equal(result,('direction','north'))
    tuple = [('direction','north')]
    result = parser.match(tuple,'verb')
    assert_equal(result,None)
    tuple = []
    result = parser.match(tuple,'direction')
    assert_equal(result,None)


def test_skip():
    tuple = [('direction','north')]
    parser.skip(tuple,'direction')
    assert_equal(tuple,[])
    tuple = [('direction','north')]
    parser.skip(tuple,'verb')
    assert_equal(tuple,[('direction','north')])
    tuple = []
    parser.match(tuple,'direction')
    assert_equal(tuple,[])


def test_parse_verb():
    pass

def test_parse_object():
    pass

def test_parse_subject():
    pass

def test_parse_sentence():
    pass

