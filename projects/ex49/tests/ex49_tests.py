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
    check = tuple[0]
    result = parser.match(tuple,'direction')
    assert_equal(result,check)
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
    tuple =  [('verb','go')]
    check = tuple[0]
    result = parser.parse_verb(tuple)
    assert_equal(result,check)
    tuple = [('stop','in'),('verb','go')]
    check = tuple[1]
    result = parser.parse_verb(tuple)
    assert_equal(result,check)
    tuple = [('stop','in')]
    assert_raises(parser.ParserError,parser.parse_verb,tuple)
 

def test_parse_object():
    tuple =  [('direction','west')]
    check = tuple[0]
    result = parser.parse_object(tuple)
    assert_equal(result,check)
    tuple = [('stop','in'),('direction','east')]
    check = tuple[1]
    result = parser.parse_object(tuple)
    assert_equal(result,check)
    tuple = [('stop','at'),('noun','princess')]
    check = tuple[1]
    result = parser.parse_object(tuple)
    assert_equal(result,check)
    tuple = [('stop','in')]
    assert_raises(parser.ParserError,parser.parse_object,tuple)

def test_parse_subject():
    word_list = [('verb','go'),('direction','west')]
    subject = ('noun','player')
    verb = word_list[0]
    obj = word_list[1]
    result = parser.parse_subject(word_list,subject)
    assert_equal(result,parser.Sentence(subject,verb,obj))
    word_list = [('verb','punch'),('noun','bear')]
    subject = ('noun','player')
    verb = word_list[0]
    obj = word_list[1]
    result = parser.parse_subject(word_list,subject)
    assert_equal(result,parser.Sentence(subject,verb,obj))
    word_list = [('direction','west'),('verb','go')]
    subject = ('noun','player')
    verb = word_list[1]
    obj = word_list[0]
    assert_raises(parser.ParserError,parser.parse_subject,word_list,subject)
    
    
def test_parse_sentence():
    word_list = [('noun','player'),('verb','go'),('direction','west')]
    subject = word_list[0]
    verb = word_list[1]
    obj = word_list[2]
    result = parser.parse_sentence(word_list)
    assert_equal(result,parser.Sentence(subject,verb,obj))

    word_list = [('noun','player'),('verb','open'),('noun','door')]
    subject = word_list[0]
    verb = word_list[1]
    obj = word_list[2]
    result = parser.parse_sentence(word_list)
    assert_equal(result,parser.Sentence(subject,verb,obj))

    word_list = [('noun','player'),('verb','open'),('stop','the'),('noun','door')]
    subject = word_list[0]
    verb = word_list[1]
    obj = word_list[3]
    result = parser.parse_sentence(word_list)
    assert_equal(result,parser.Sentence(subject,verb,obj))

    word_list = [('verb','go'),('stop','through'),('stop','the'),('noun','door')]
    subject = ('noun','player')
    verb = word_list[0]
    obj = word_list[3]
    result = parser.parse_sentence(word_list)
    assert_equal(result,parser.Sentence(subject,verb,obj))

    word_list = [('verb','punch'),('noun','bear'),('stop','in'),('stop','the'),('noun','face')]
    subject = ('noun','player')
    verb = word_list[0]
    obj = word_list[1]
    result = parser.parse_sentence(word_list)
    assert_equal(result,parser.Sentence(subject,verb,obj))

    word_list = [('verb','punch'),('noun','bear')]
    subject = ('noun','player')
    verb = word_list[0]
    obj = word_list[1]
    result = parser.parse_sentence(word_list)
    assert_equal(result,parser.Sentence(subject,verb,obj))

    word_list = [('noun','bear'),('verb','punch')]
    subject = ('noun','player')
    verb = word_list[1]
    obj = word_list[0]
    assert_raises(parser.ParserError,parser.parse_sentence,word_list)


