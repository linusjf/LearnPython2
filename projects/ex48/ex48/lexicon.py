import re

directions = {
        'north':'direction',
        'south':'direction',
         'east':'direction',
         'west':'direction',
         'down':'direction',
         'up':'direction',
         'back':'direction',
         'left':'direction',
         'right':'direction'
}

verbs = {
        'go':'verb',
         'stop':'verb',
         'kill':'verb',
         'eat':'verb'
}

stops = {
        'the':'stop',
         'in':'stop',
         'of':'stop',
         'from':'stop',
         'at':'stop',
         'it':'stop'
}

nouns = {
        'door':'noun',
         'bear':'noun',
         'princess':'noun',
         'cabinet':'noun'
}

def scan(stuff):
    words = stuff.split()
    tuples = []
    for word in words:
        if word.lower() in directions:
            tuples.append((directions[word.lower()],word))
        elif word.lower() in verbs:
            tuples.append((verbs[word.lower()],word))
        elif word.lower() in stops:
            tuples.append((stops[word.lower()],word))
        elif word.lower() in nouns:
            tuples.append((nouns[word.lower()],word))
        else:
            num = scan_num(word)
            if num <> None:
                tuples.append(('number',num))
            else:
                tuples.append(('<error>',word))
    
    return tuples

def scan_num(word):

    isnum = re.search("^[0-9]+$",word)
    if isnum:
        return int(word)
    else:
        return None


