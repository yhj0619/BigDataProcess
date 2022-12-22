import sys
import numpy as np
import operator
from os import listdir

def createDataSet(dataDir):
	labels = []
	trainingDigits = listdir(dataDir)
	m = len(trainingDigits)
	trainingMat = np.zeros((m,1024))

	for i in range(m):
		fileName = trainingDigits[i]
		classNum = int(fileName.split('_')[0])
		labels.append(classNum)
		trainingMat[i, :] = vectors(dataDir + '/' + fileName)
	return labels, trainingMat

def vectors(fileName):
	vector = np.zeros((1,1024))
	with open(fileName) as fp:
		for i in range(32):
			line = fp.readline()
			for j in range(32):
				vector[0, 32*i+j] = int(line[j])
		return vector

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

trainingFileDirName = sys.argv[1]
testFileDirName = sys.argv[2]

testFiles = listdir(testFileDirName)
m = len(testFiles)

labels, matrix = createDataSet(trainingFileDirName)

for k in range(1, 21): 
    error = 0
    count = 0

    for i in range(m):
        classes = int(testFiles[i].split('_')[0])
        data = vectors(testFileDirName + '/' + testFiles[i])
        result = classify0(data, matrix, labels, k)
        
        count += 1
        if classes != result:
            error += 1
    
    print(int(error / count * 100))
