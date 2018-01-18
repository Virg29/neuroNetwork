import json
import math
WorkWith = "Boxing"
LayerLevels = ['InpL','InnL','OutL']
TempValues = {'Value','CalculatedWith'}
File = open('NeuroWebStandart.json','r')
Json = json.loads(File.read())
print(Json) 
File.close()
def activation(x):
	return sigmoid(x)

def weigtInitialization(from,to): 
	pass
def reset():
	for layer in LayerLevels:
		for neuron in Json['Type'][WorkWith][layer]:
			neuron['Neuron']['TempValues']['Value']=0
			neuron['Neuron']['TempValues']['CalculatedWith']=[]

def sigmoid(x):
    return (1 / (1 + math.exp(-x)))

def getErrorValue(massive):
	Error=0
	for i in range(len(Json['Type'][WorkWith][LayerLevels[3]])):  
		neuron=Json['Type'][WorkWith][LayerLevels[3]][i]
		Error+=math.pow(activation(neuron['Neuron']['TempValues']['Value'])-massive[i],2)
	return Error
reset()
def setValue(massive):
	if(len(massive)!=len(Json['Type'][WorkWith][LayerLevels[1]])):
		raise IndexError
	for i in range(len(Json['Type'][WorkWith][LayerLevels[1]]))
		neuron=Json['Type'][WorkWith][LayerLevels[1]][i]
		neuron['Neuron']['InputValue']=massive[i]
def run():
	for layer in LayerLevels:
			for neuron in Json['Type'][WorkWith][layer]:
				#print(layer)
				#print(neuron)
				if(layer==LayerLevels[0]):
					for i in range(len(neuron['Neuron']['SinapsConnects'])):
						for j in Json['Type'][WorkWith][neuron['Neuron']['ConnectParallelLayer'][i]]:
							if(j['Neuron']['Id']==neuron['Neuron']['SinapsConnects'][i]):
								j['Neuron']['TempValues']['Value']+=activation(neuron['Neuron']['InputValue'])*neuron['Neuron']['SinapsWeight'][i]
								j['Neuron']['TempValues']['CalculatedWith'].append(neuron['Neuron']['Id'])
				if(layer==LayerLevels[1]):
					for i in range(len(neuron['Neuron']['ConnectParallelLayer'])):
						for j in Json['Type'][WorkWith][neuron['Neuron']['ConnectParallelLayer'][i]]:
							if(neuron['Neuron']['ConnectParallelLayer'][i]!=layer):
								continue
							if(j['Neuron']['TempValues']['CalculatedWith'].count(neuron['Neuron']['Id'])==0):
								j['Neuron']['TempValues']['Value']+=activation(neuron['Neuron']['TempValues']['Value'])*neuron['Neuron']['SinapsWeight'][i]	
								j['Neuron']['TempValues']['CalculatedWith'].append(neuron['Neuron']['Id'])
							else:
								continue

					for i in range(len(neuron['Neuron']['ConnectParallelLayer'])):
						for j in Json['Type'][WorkWith][neuron['Neuron']['ConnectParallelLayer'][i]]:
							if(j['Neuron']['TempValues']['CalculatedWith'].count(neuron['Neuron']['Id'])==0):
								j['Neuron']['TempValues']['Value']+=activation(neuron['Neuron']['TempValues']['Value'])*neuron['Neuron']['SinapsWeight'][i]
								j['Neuron']['TempValues']['CalculatedWith'].append(neuron['Neuron']['Id'])
							else:
								continue
				if(layer==LayerLevels[2]):
					pass
run()
print(Json)