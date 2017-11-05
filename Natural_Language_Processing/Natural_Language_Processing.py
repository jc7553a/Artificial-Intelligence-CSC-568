import nltk
import os
from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer
import re
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
                    'third'
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
             'doct', 'mess'}

def getToBeOrNotToBe():
    with open('to_be_or_not.txt', 'r') as myFile:
        passage1 = myFile.read().replace('\n', ' ')
    return passage1

def getDumbledoreSpeech():
    with open('dumbledore.txt', 'r') as myFile:
        passage1 = myFile.read().replace('\n', ' ')
    return passage1

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
    passage = getTragedies()
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

    return new_tokens

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
    return new_tokens



def getFirst50():
    fdist = FreqDist(computeComedies(getComedies()))
    print(fdist.most_common(50))
    
    fidst = FreqDist(computeTragedies(getTragedies()))
    print(fdist.most_common(50))

def createParseTree():
    with open('to_be_3.txt', 'r') as myFile:
         train_text = myFile.read().replace('\n', ' ')
    sample_text = train_text

    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

    tokenized = custom_sent_tokenizer.tokenize(sample_text)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()     

    except Exception as e:
        print(str(e))


def generateWordCloud():
    text = ' '.join(computeComedies(getComedies()))
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis("off")
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    text = ' '.join(computeTragedies(getTragedies()))
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis("off")
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    
    
if __name__ == '__main__':
    #getFirst50()
    '''
    stuff = list(getToBeOrNotToBe())
    sentances = 0
    for i in range(len(stuff)):
        if stuff[i] == '?' or stuff[i] == '.':
            sentances +=1
    print(sentances)
    '''
    generateWordCloud()
    
