# Example of making predictions
from math import sqrt
import numpy as np
from dataset_maker import normalization_vector
from word_freq_counter import string_norm

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	# print(row1)
	# print(row2)
	# print(len(row1))
	# print(len(row2))
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)
# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors 
# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	#print(neighbors)
	output_values = [row[-1] for row in neighbors]
	#print(output_values)
	prediction = max(set(output_values), key=output_values.count)
	return prediction, output_values
# # Test distance function
# dataset = [[2.7810836,2.550537003,0],
# 	[1.465489372,2.362125076,0],
# 	[3.396561688,4.400293529,0],
# 	[1.38807019,1.850220317,0],
# 	[3.06407232,3.005305973,0],
# 	[7.627531214,2.759262235,1],
# 	[5.332441248,2.088626775,1],
# 	[6.922596716,1.77106367,1],
# 	[8.675418651,-0.242068655,1],
# 	[7.673756466,3.508563011,1]]
# prediction = predict_classification(dataset, dataset[0], 5)
# print('Expected %d, Got %d.' % (dataset[0][-1], prediction))

def text_fit(full_path_to_text, full_path_to_vector):
	with open(full_path_to_vector) as inputvec:
		vectorlist = inputvec.read().split() # читаем с файла разбиваем по пробелам

	vector = [0] * len(vectorlist)
	# print(vector)
	# input()

	with open(full_path_to_text) as inputfile:
		list_data = inputfile.read().split() # читаем с файла разбиваем по пробелам
		#print(list_data)
		for item in list_data:
			litem = string_norm(item)
			if litem in vectorlist:
				index = vectorlist.index(litem)
				v_item = vector[index]
				n_v_item = v_item + 1
				vector[index] = n_v_item

	norm_vector = normalization_vector(vector)

	return norm_vector

def main():
	test_path = "/home/slava/Source/KNN_Text_Class/Dataset/Test"
	vec_path = "/home/slava/Source/KNN_Text_Class/NewVector.txt"

	dataset = np.load("DSDataset.npy")
	#print(len(dataset[0]))
	#input()

	fitd1 = text_fit(test_path + "/" + "D1", vec_path)
	fitd2 = text_fit(test_path + "/" + "D2", vec_path)
	fits1 = text_fit(test_path + "/" + "S1", vec_path)
	fits2 = text_fit(test_path + "/" + "S2", vec_path)

	#print(len(fitd1))

	print("0 is Detective, 1 is Space Fiction")
	print("----------------------------------")

	print("Test text is D1")
	prediction, list_data = predict_classification(dataset, fitd1, 3)
	print('Expected %d, Got %d, K %d, List %s' % (0, prediction, 3, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fitd1, 5)
	print('Expected %d, Got %d, K %d, List %s' % (0, prediction, 5, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fitd1, 7)
	print('Expected %d, Got %d, K %d, List %s' % (0, prediction, 7, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fitd1, 9)
	print('Expected %d, Got %d, K %d, List %s' % (0, prediction, 9, list_data))
	print("----------------------------------------------------")
	print("----------------------------------------------------")
	print("----------------------------------------------------")

	print("Test text is D2")
	prediction, list_data = predict_classification(dataset, fitd2, 3)
	print('Expected %d, Got %d, K %d, List %s' % (0, prediction, 3, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fitd2, 5)
	print('Expected %d, Got %d, K %d, List %s' % (0, prediction, 5, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fitd2, 7)
	print('Expected %d, Got %d, K %d, List %s' % (0, prediction, 7, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fitd2, 9)
	print('Expected %d, Got %d, K %d, List %s' % (0, prediction, 9, list_data))
	print("----------------------------------------------------")
	print("----------------------------------------------------")
	print("----------------------------------------------------")

	print("Test text is S1")
	prediction, list_data = predict_classification(dataset, fits1, 3)
	print('Expected %d, Got %d, K %d, List %s' % (1, prediction, 3, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fits1, 5)
	print('Expected %d, Got %d, K %d, List %s' % (1, prediction, 5, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fits1, 7)
	print('Expected %d, Got %d, K %d, List %s' % (1, prediction, 7, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fits1, 9)
	print('Expected %d, Got %d, K %d, List %s' % (1, prediction, 9, list_data))
	print("----------------------------------------------------")
	print("----------------------------------------------------")
	print("----------------------------------------------------")

	print("Test text is S2")
	prediction, list_data = predict_classification(dataset, fits2, 3)
	print('Expected %d, Got %d, K %d, List %s' % (1, prediction, 3, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fits2, 5)
	print('Expected %d, Got %d, K %d, List %s' % (1, prediction, 5, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fits2, 7)
	print('Expected %d, Got %d, K %d, List %s' % (1, prediction, 7, list_data))
	print("----------------------------------------------------")
	prediction, list_data = predict_classification(dataset, fits2, 9)
	print('Expected %d, Got %d, K %d, List %s' % (1, prediction, 9, list_data))
	print("----------------------------------------------------")
	print("----------------------------------------------------")
	print("----------------------------------------------------")


if __name__ == "__main__":
	main()
