import numpy as np
import MultiLayerPerceptron as MLP
import random as ra


'''----------------------------------------'''
'''IMORTANT FOR DATA IMPORT!!!!!!!!'''
'''YOU SHOULD HAVE 501 VALUES IN EACH ROW'''
'''YOUR FIRST 500 VALUES SHOULD BE FREQUENCYS OF WORDS OR BOW/TFIDF'''
'''THE LAST VALUE IN EACH ROW MUST BE THE CLASSIFICATION VALUE'''
'''------------------------------------------'''


'''Import Saved Data'''
def getData():
    '''You Need to Put in the Correct File Name Below'''
    '''IT SHOULD BE A CSV'''
    data = np.genfromtxt('shakespeareTFIDF.csv', delimiter = ',')
    '''I'm Deleteing The First Row Because that was all Column Names'''
    data = np.delete(data, 0,0)
    return data


'''Trains Using 500 Epochs'''
def train(dataPassed):
    shape = np.shape(dataPassed)

    '''Creates Neural Network, Num Features should stay same'''
    '''You can Change Number of hidden units if you want'''
    '''I'm just using 3/4 Size of Input'''
    network = MLP.MLP(shape[1]-1, int(shape[1]*.75))
    np.random.shuffle(dataPassed)

    '''Number of Epochs is 500'''
    '''You can Train for Longer If You Want'''
    for i in range(500):
        for j in range(len(dataPassed)):
            random = ra.randint(0, shape[0]-1)
            network.train([dataPassed[random][0:500]], [[dataPassed[random][500]]])
    return network


'''Tests Network and Produces Accuracy'''
def test(testingData, network, classes):
    predictedValues = []
    for i in range(len(testingData)):
        predictedValues.append(network.calc_total_cost([testingData[i][0:500]], [[testingData[i][500]]]))

    for i in range(len(predictedValues)):
        if predictedValues[i] < .5:
            predictedValues[i] = 0
        else:
            predictedValues[i] = 1

    correct = 0
    false = 0
    for i in range(len(predictedValues)):
        if predictedValues[i] == classes[i]:
            correct +=1
        else:
            false +=1
    accuracy = correct/len(classes)
    print("Accuracy ", correct/len(classes))
    return accuracy


'''Keeps Class Values of the Testing Data to Compare To Predicted'''
def getClassValues(dataPassed):
    classes = []
    for i in range(len(dataPassed)):
        classes.append(dataPassed[i][500])
    return classes

def tenFoldCrossValidation():
    totalData = getData()
    startFold = 0
    endFold = .1
    accuracy = 0
    np.random.shuffle(totalData)
    for i in range(10):
        print("Performing Fold " + str(i+1))
        beginFold = int(startFold*len(totalData))
        endingFold = int(endFold*len(totalData))
        if i == 0:
            testingData = totalData[beginFold:endingFold][:]
            trainingData = totalData[endingFold:len(totalData)][:]
        elif i == 9:
            trainingData = totalData[0:beginFold][:]
            testingData = totalData[beginFold:len(totalData)][:]
        else:
            trainingData1 = totalData[0:beginFold][:]
            trainingData2 = totalData[endingFold:len(totalData)][:]
            trainingData = np.concatenate((trainingData1, trainingData2),axis =  0)
            testingData = totalData[beginFold:endingFold][:]
        
        classes = getClassValues(testingData)
        neuralNet= train(trainingData)
        accuracy += test(testingData, neuralNet, classes)
        startFold += .1
        endFold +=.1
    totalAccuracy = accuracy*.1
    print("Total Accuracy of MLP " + str(totalAccuracy))
        

if __name__ == '__main__':
    tenFoldCrossValidation()
