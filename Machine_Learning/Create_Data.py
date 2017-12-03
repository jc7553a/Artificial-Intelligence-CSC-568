import nltk
import os
from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer
import re
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
import string
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from nltk import bigrams
from nltk.corpus import PlaintextCorpusReader
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

os.chdir('C:/Artificial_Intelligence')

fiveHundredWords = ['come',
'good',
'let',
'would',
'well',
'hath',
'know',
'sir',
'make',
'love',
'one',
'like',
'say',
'go',
'yet',
'must',
'may',
'see',
'night',
'take',
'time',
'eye',
'upon',
'haue',
'heart',
'give',
'hand',
'much',
'mine',
'speak',
'life',
'day',
'doth',
'tell',
'loue',
'look',
'thing',
'death',
'art',
'god',
'men',
'friend',
'word',
'true',
'call',
'made',
'away',
'stand',
'think',
'thus',
'pray',
'sweet',
'two',
'nothing',
'could',
'part',
'great',
'dead',
'fear',
'hear',
'heaven',
'doe',
'world',
'play',
'master',
'till',
'name',
'though',
'son',
'thought',
'lie',
'daughter',
'therefore',
'better',
'head',
'enter',
'way',
'done',
'poor',
'never',
'nature',
'gone',
'hast',
'whose',
'hold',
'put',
'still',
'many',
'find',
'stay',
'place',
'show',
'noble',
'blood',
'mean',
'bear',
'nay',
'keep',
'house',
'leave',
'bed',
'fortune',
'boy',
'fair',
'within',
'grace',
'might',
'none',
'best',
'little',
'face',
'heere',
'set',
'woman',
'wife',
'rest',
'light',
'bid',
'tongue',
'follow',
'madam',
'bring',
'fall',
'young',
'hence',
'long',
'dear',
'spirit',
'since',
'answer',
'even',
'die',
'sword',
'kill',
'else',
'hor',
'ever',
'gentle',
'letter',
'without',
'live',
'three',
'full',
'reason',
'neuer',
'forth',
'faire',
'every',
'fellow',
'came',
'ring',
'end',
'ile',
'faith',
'turn',
'welcome',
'matter',
'hour',
'get',
'peace',
'dost',
'honour',
'sleep',
'wilt',
'heard',
'thine',
'youth',
'power',
'another',
'desire',
'enough',
'arm',
'strange',
'back',
'marry',
'moone',
'said',
'wit',
'giue',
'hamlet',
'lysander',
'rather',
'indeed',
'mind',
'pol',
'cause',
'morrow',
'please',
'sister',
'soul',
'earth',
'villain',
'sight',
'farewell',
'run',
'body',
'shalt',
'fire',
'mark',
'right',
'goe',
'hope',
'cry',
'citizen',
'ear',
'meet',
'new',
'seen',
'draw',
'speake',
'hither',
'need',
'child',
'saw',
'prince',
'together',
'dem',
'court',
'wrong',
'mad',
'sure',
'fly',
'tear',
'friar',
'use',
'seek',
'honest',
'grief',
'husband',
'looke',
'purpose',
'home',
'roman',
'sound',
'help',
'alone',
'mistress',
'hard',
'last',
'ill',
'something',
'truth',
'lay',
'fit',
'horse',
'left',
'false',
'pardon',
'heare',
'breath',
'casca',
'fairy',
'hate',
'thousand',
'found',
'state',
'dare',
'far',
'bond',
'law',
'wish',
'present',
'air',
'enemy',
'truly',
'read',
'ground',
'ben',
'cut',
'laer',
'deed',
'told',
'fell',
'bloody',
'thank',
'return',
'kind',
'mer',
'hang',
'year',
'shame',
'remember',
'late',
'seem',
'note',
'oph',
'send',
'bound',
'wind',
'wood',
'lost',
'prithee',
'voice',
'dog',
'worthy',
'sea',
'high',
'leaue',
'almost',
'fault',
'cold',
'either',
'age',
'question',
'selfe',
'patience',
'witch',
'beseech',
'haste',
'news',
'yes',
'neither',
'break',
'virtue',
'lip',
'speech',
'side',
'sun',
'gold',
'unto',
'mar',
'flesh',
'thinke',
'service',
'lion',
'flower',
'near',
'pleasure',
'watch',
'duty',
'rich',
'soldier',
'hell',
'beard',
'known',
'rome',
'servant',
'holy',
'wear',
'pale',
'sing',
'begin',
'arviragus',
'red',
'wise',
'happy',
'maid',
'comfort',
'content',
'feare',
'foot',
'point',
'company',
'crown',
'worse',
'land',
'sit',
'report',
'foul',
'vile',
'doctor',
'sorrow',
'married',
'grave',
'doubt',
'worth',
'strike',
'sport',
'talk',
'believe',
'change',
'ready',
'woe',
'lead',
'spoke',
'swear',
'business',
'touch',
'fare',
'joy',
'shine',
'morning',
'gave',
'juliet',
'poison',
'ask',
'pity',
'dream',
'beg',
'kiss',
'grow',
'wonder',
'wherefore',
'traitor',
'oath',
'given',
'care',
'tender',
'aside',
'ha',
'choose',
'hide',
'act',
'louers',
'cousin',
'sick',
'respect',
'honor',
'sent',
'work',
'oft',
'passion',
'weep',
'fiend',
'didst',
'strong',
'murther',
'thanks',
'thisby',
'walk',
'againe',
'next',
'trust',
'met',
'country',
'lover',
'drink',
'common',
'born',
'pretty',
'course',
'mouth',
'knave',
'free',
'euery',
'brain',
'command',
'often',
'beauty',
'athens',
'lose',
'murtherer',
'stone',
'hee',
'straight',
'ghost',
'finde',
'wake',
'ross',
'lov',
'manner',
'twenty',
'took',
'chamber',
'promise',
'beast',
'pay',
'yea',
'sake',
'sleepe',
'canst',
'slain',
'owne',
'wherein',
'sad',
'fight',
'fetch',
'move',
'thyself',
'coming',
'past',
'low',
'black',
'tree',
'bad',
'sometime',
'chance',
'smile',
'wing',
'me',
'want',
'water',
'majesty',
'whether',
'door',
'slave',
'sense',
'suit',
'prove',
'tyrant',
'alack',
'half',
'fast',
'cast',
'toward',
'general',
'shake',
'lyon',
'finger',
'war']



comedy_names = {'orlando', 'oliver', 'adam', 'charles' 'celia', 'rosalind',
                    'touchstone', 'le', 'beau', 'frederick','duke', 'senior',
                    'amiens', 'first', 'lord', 'second', 'adam', 'corin',
                    'silvius', 'jaques', 'corin', 'celia', 'martext', 'phebe',
                    'audrey', 'william', 'page', 'd', 's', 'll', 'u' ,'t', 'st',
                    'gentleman', 'queen', 'posthumus', 'imogen', 'cymbeline',
                    'pisanio','cloten', 'frenchman', 'iachimo', 'philario',
                    'messenger', 'belarius', 'guiderius', 'aviragus', 'senator',
                    'tribune', 'lucius', 'soothsayer', 'captain', 'gaoler',
                    'sicilius', 'brother', 'mother', 'father', 'women', 'lady',
                    'sal', 'anthonio', 'salar', 'anth', 'sola', 'ant', 'sala' ,
                    'bass', 'grati', 'lor', 'gra', 'an', 'bas', 'portia', 'ner',
                    'por', 'shy', 'iew', 'mor', 'clo', 'glaub', 'laun', 'lan',
                    'leon', 'ies', 'mes', 'tub', 'iessi', 'lorens', 'clown',
                    'clow', 'iessica', 'du', 'theseus', 'hip', 'the', 'ege',
                    'her', 'lys', 'egeus', 'hel', 'hele', 'quin', 'qui', 'bot',
                    'quince', 'flu', 'flut', 'star', 'snowt', 'snug', 'all',
                    'bottome', 'fai', 'rob', 'ob', 'qu', 'ober', 'puc', 'pucke',
                    'puck', 'pu', 'lis', 'de', 'snout', 'sn', 'pir', 'pet', 'tyta',
                    'tita', 'mus', 'peas', 'clow', 'thres', 'lis', 'pro', 'prol',
                    'wall', 'pir', 'deme', 'archidamus', 'camillo', 'polixenes',
                    'leontes', 'hermione', 'mamillius', 'antigonus', 'paulina',
                    'attendant', 'cleomenes','dion', 'mariner', 'clown', 'shepherd',
                    'autolycus', 'florizel', 'perdita', 'mopsa' ,'mopsa', 'dorcas',
                    'third', 'thou', 'thy', 'shall', 'octavius', 'helena', 'tybalt',
                'v', 'demetrius', 'messala', 'bassanio', 'malcolm', 'vp', 'ro', 'ay', 'a', 'i',
                'ere', 'o', 'er', 'euer', 'en', 'ye', 'ala', 'is', 'cap', 'piramus', 'hermia', 'ho', 'n', 'vpon', 'to', 'th',
                'thee', 'peter'
                    }
                    


                    
names = {'rom', 'jul', 'romeo', 'macduff', 'banquo', 'macbeth','Rom', 'Jul',
             'Ben', 'Mer', 'nurse', 'Cap', 'lord', 'macbeth', 'DUNCAN',
             'MACDUFF', 'MURTHERER', 'MURTHERERS', 'BOTH', 'lady',
             'MALCOLM', 'DONALBAIN', 'BANQUO', 'FLEANCE', 'LENNOX',
             'ROSS', 'SON', 'DOCTOR', 'GENTLEWOMEN', 'MENTEITH',
             'ANGUS', 'CAITHNESS', 'SIWARD', 'YOUNG', 'SEYTON',
             'HECATE', 'first', 'fourth', 'all', 'second', 'third',
             'WITCH', 'MESSENGER', 'Ber', 'Fran','Mar', 'Hor', 'King',
             'Laer', 'Pol', 'Ham', 'Queen', 'Oph', 'Ghost', 'Rey',
             'Volt', 'Ros', 'Guil', 'Play', 'Pro', 'Both', 'Mess',
             'Sailor', 'Clown', 'Osr', 'Fort', 'Ambassador', 'ham',
             'queen', 'king', 's', 'd', 'll', 't', 'u', 'FLAVIUS',
             'COMMONER', 'MARULLUS', 'caesar', 'CASCA', 'CALPURNIA',
             'antony', 'SOOTHSAYER', 'cassius', 'brutus', 'CICERO',
             'CINNA','LUCIUS', 'DECIUS', 'METELLUS', 'TREBONIUS',
             'PORTIA', 'LIGARIUS', 'SERVENT', 'CALPURNIA',
             'PUBLIUS','POPILIUS', 'ARTEMIDORUS', 'CITIZEN', 'OCTAVIUS',
             'LUCILIUS', 'POET', 'MESSALA', 'TITINIUS', 'VARRAO',
             'CLAUDIO', 'CATO', 'CLITUS', 'VOLUMNIUS', 'kent', 'glou', 'edm',
             'lear', 'gon', 'cor', 'alb', 'bur', 'france', 'reg', 'edg', 'osw',
             'knight', 'fool', 'cur', 'corn', 'gent', 'serv', 'old', 'man',
             'doct', 'mess', 'thou', 'thy', 'shall', 'octavius', 'helena', 'tybalt',
                'v', 'demetrius', 'messala', 'vp', 'ay', 'a', 'i',
                'ere', 'o', 'er', 'euer', 'en', 'ye', 'ala', 'is', 'cap', 'piramus', 'hermia', 'ho', 'n', 'vpon', 'to', 'th',
         'thee', 'peter'}

def getRidOfNames(wordsPassed):
    global names, comedy_names
    listOfWords = re.sub("[^\w]", " ",  wordsPassed).split()
    #listOfWords = wordsPassed
    new_list = []
    for i in range(len(listOfWords)):
        if listOfWords[i] in names or listOfWords[i] in comedy_names or listOfWords[i] == ' ':
            pass
        else:
            new_list.append(listOfWords[i])
    return new_list
    

def getTragedies():
    os.chdir('C:/Artificial_Intelligence/Tragedies')
    with open('Romeo_Juliet.txt', 'r') as myFile:
        passage1 = myFile.read().replace('\n', ' ')
    passage1 = re.sub(r'\d+', '', passage1)

    with open('Macbeth.txt', 'r') as myFile:
        passage2 = myFile.read().replace('\n', ' ')
    passage2 = re.sub(r'\d+', '', passage2)

    with open('Hamlet.txt', 'r') as myFile:
        passage3 = myFile.read().replace('\n', ' ')
    passage3 = re.sub(r'\d+', '', passage3)

    with open('Julius_Ceaser.txt', 'r') as myFile:
        passage4 = myFile.read().replace('\n', ' ')
    passage4 = re.sub(r'\d+', '', passage4)

    with open('King_Lear.txt', 'r') as myFile:
        passage5 = myFile.read().replace('\n', ' ')
    passage5 = re.sub(r'\d+', '', passage5)
    
    return passage1 + ' ' + passage2 + ' ' + passage3 + ' ' + passage4 + ' ' + passage5

def getComedies():
    os.chdir('C:/Artificial_Intelligence/Comedies')
    with open('All_Is_Well.txt', 'r') as myFile:
        passage1 = myFile.read().replace('\n', ' ')
    passage1 = re.sub(r'\d+', '', passage1)

    with open('Cymbeline.txt', 'r') as myFile:
        passage2 = myFile.read().replace('\n', ' ')
    passage2 = re.sub(r'\d+', '', passage2)

    with open('Merchant_Of_Venice.txt', 'r') as myFile:
        passage3 = myFile.read().replace('\n', ' ')
    passage3 = re.sub(r'\d+', '', passage3)

    with open('MidSummer_Nights_Dream.txt', 'r') as myFile:
        passage4 = myFile.read().replace('\n', ' ')
    passage4 = re.sub(r'\d+', '', passage4)

    with open('Winters_Tale.txt', 'r') as myFile:
        passage5 = myFile.read().replace('\n', ' ')
    passage5 = re.sub(r'\d+', '', passage4)
    
    return passage1 + ' ' + passage2 + ' ' + passage3 + ' ' + passage4 + ' ' + passage5

def computeTragedies(passage):
    global names
    wordnet = nltk.WordNetLemmatizer()
    stop = stopwords.words('english') + list(string.punctuation)                    
    passage = [i for i in word_tokenize(passage.lower()) if i not in stop]
    passage = ' '.join(passage)
    tagged_sentence = pos_tag(passage.split())
    edited_Passage = [word for word,tag in tagged_sentence if tag != 'NNP' and tag != 'NNPS']
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(passage)
    new_tokens = []
    for i in range(len(tokens)):
        if tokens[i] in names:
            pass
        else:
            new_tokens.append(tokens[i])
    for i in range(len(new_tokens)):
        new_tokens[i] = wordnet.lemmatize(new_tokens[i])
    return getRidOfNames(' '.join(new_tokens))

def computeComedies(passage):
    global comedy_names
    wordnet = nltk.WordNetLemmatizer()
    stop = stopwords.words('english') + list(string.punctuation)
    passage = [i for i in word_tokenize(passage.lower()) if i not in stop]
    passage = ' '.join(passage)
    tagged_sentence = pos_tag(passage.split())
    edited_Passage = [word for word,tag in tagged_sentence if tag != 'NNP' and tag != 'NNPS']
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(passage)
    new_tokens = []
    for i in range(len(tokens)):
        if tokens[i] in comedy_names:
            pass
        else:
            new_tokens.append(tokens[i])
    for i in range(len(new_tokens)):
        new_tokens[i] = wordnet.lemmatize(new_tokens[i])
    return getRidOfNames(' '.join(new_tokens))

def getFirst500(listPassed):
    fdist = FreqDist(listPassed)
    return fdist.most_common(500)



def computeAct(actGiven, classification):
    global fiveHundredWords
    values = np.zeros((1,501))
    values[0][500] = classification
    for i in range (len(actGiven)):
        word = actGiven[i].lower()
        for j in range(len(fiveHundredWords)):
            if word == fiveHundredWords[j]:
                values[0][j] +=1
                
    return values.tolist()


def computeIDF(allActs):
    idfCalc = np.zeros((1, 500))
    global fiveHundredWords
    for i in range(len(fiveHundredWords)):
        word = fiveHundredWords[i]
        for j in range(len(allActs)):
            myAct = allActs[j]
            found = 0
            for k in range(len(myAct)):
                if myAct[k] == word:
                    found = 1
            idfCalc[0][i] += found
    for i in range(500):
        idfCalc[0][i] = np.log10(len(allActs)/(idfCalc[0][i]))
    return idfCalc
    

def computeTF(actGiven, classification):
    global fiveHundredWords
    values = np.zeros((1,501))
    values[0][500] = classification
    for i in range(len(fiveHundredWords)):
        word = fiveHundredWords[i]
        amount = 0
        for j in range(len(actGiven)):
            if word == actGiven[j]:
                amount +=1
        if amount != 0:
            values[0][i] = amount/(len(actGiven)*1.0)
    return values.tolist()

def getComedyActs():
    os.chdir('C:/Artificial_Intelligence/Acts_Comedies')
    
    with open('MidSummer_Nights_Dream_Act.txt', 'r') as myFile:
        passage1 = myFile.read().replace('\n', ' ')
    passage1 = re.sub(r'\d+', '', passage1)
    passage1 = passage1.split("JASPIN")

    with open('Cymbeline_Act.txt', 'r') as myFile:
        passage2 = myFile.read().replace('\n', ' ')
    passage2 = re.sub(r'\d+', '', passage2)
    passage2 = passage2.split("JASPIN")

    with open('Merchant_Of_Venice_Act.txt', 'r') as myFile:
        passage3 = myFile.read().replace('\n', ' ')
    passage3 = re.sub(r'\d+', '', passage3)
    passage3 = passage3.split("JASPIN")

    with open('As_You_Like_Act.txt', 'r') as myFile:
        passage4 = myFile.read().replace('\n', ' ')
    passage4 = re.sub(r'\d+', '', passage4)
    passage4 = passage4.split("JASPIN")

    with open('Winters_Tale_Act.txt', 'r') as myFile:
        passage5 = myFile.read().replace('\n', ' ')
    passage5 = re.sub(r'\d+', '', passage5)
    passage5 = passage5.split("JASPIN")

    return passage1 + passage2 + passage3 + passage4 + passage5

def getTragedyActs():
    os.chdir('C:/Artificial_Intelligence/Acts_Tragedies')
    
    with open('Hamlet_Act.txt', 'r') as myFile:
        passage1 = myFile.read().replace('\n', ' ')
    passage1 = re.sub(r'\d+', '', passage1)
    passage1 = passage1.split("JASPIN")

    with open('Julius_Ceaser_Act.txt', 'r') as myFile:
        passage2 = myFile.read().replace('\n', ' ')
    passage2 = re.sub(r'\d+', '', passage2)
    passage2 = passage2.split("JASPIN")

    with open('King_Lear_Act.txt', 'r') as myFile:
        passage3 = myFile.read().replace('\n', ' ')
    passage3 = re.sub(r'\d+', '', passage3)
    passage3 = passage3.split("JASPIN")

    with open('Macbeth_Act.txt', 'r') as myFile:
        passage4 = myFile.read().replace('\n', ' ')
    passage4 = re.sub(r'\d+', '', passage4)
    passage4 = passage4.split("JASPIN")

    with open('Romeo_Juliet_Act.txt', 'r') as myFile:
        passage5 = myFile.read().replace('\n', ' ')
    passage5 = re.sub(r'\d+', '', passage5)
    passage5 = passage5.split("JASPIN")

    return passage1 + passage2 + passage3 + passage4 + passage5

def BagOfWords():
    comedyActs = getComedyActs()
    new_passage = computeComedies(comedyActs[0])
    
    for i in range(len(comedyActs)):
        new_passage = computeComedies(comedyActs[i])
        values.append(computeAct(new_passage, 1))
    print(np.shape(values))
    
    for i in range(len(values)):
        newvals.append(values[i][0])
    print(np.shape(newvals))
    
    tragedyActs = getTragedyActs()
    values2 = []
    for i in range(len(tragedyActs)):
        new_passage = computeTragedies(tragedyActs[i])
        values2.append(computeAct(new_passage, 0))
    print(np.shape(values2))

    for i in range(len(values2)):
        newvals.append(values2[i][0])

    print(np.shape(newvals))
    os.chdir('C:/Artificial_Intelligence')
    np.savetxt('shakespeare.csv', newvals, delimiter = ",")
    

if __name__ == '__main__':
    '''
    comedies = computeComedies(getComedies())
    tragedies = computeTragedies(getTragedies())
    totalWords = comedies + tragedies
    fiveHundred = getFirst500(totalWords)
    for i in range(len(fiveHundred)):
        print("'" + str(fiveHundred[i][0]) + "',")
    '''
    #TFIDF()
    comedy = getComedyActs()
    comedyActs = []
    values = []
    for i in range(len(comedy)):
        comedyActs.append(computeComedies(comedy[i]))
        values.append(computeTF(comedyActs[i], 1))
    tragedy = getTragedyActs()
    tragedyActs = []
    values2 = []
    for i in range(len(tragedy)):
        tragedyActs.append(computeTragedies(tragedy[i]))
        values2.append(computeTF(tragedyActs[i], 0))
    thing = computeIDF(comedyActs+tragedyActs)
    newvals = []
    for i in range(len(values)):
        newvals.append(values[i][0])

    for i in range(len(values2)):
        newvals.append(values2[i][0])
    print(np.shape(newvals))

    for i in range(len(newvals)):
        for j in range(500):
            newvals[i][j] = newvals[i][j]*thing[0][j]
    
    os.chdir('C:/Artificial_Intelligence')
    np.savetxt('shakespeareTFIDF.csv', newvals, delimiter = ",")
