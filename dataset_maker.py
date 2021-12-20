import os
import numpy as np
from word_freq_counter import string_norm

def repeat_deleter(vector_path, new_vector_path):
	with open(vector_path) as vectorfile:
		vectorlist = vectorfile.read().split()

		rd_vectorlist = list(set(vectorlist))

		ofile = open(new_vector_path, 'w')
		for item in rd_vectorlist:
			ofile.write(item + "\n")

		ofile.close()

def normalization_vector(vector):
	norm_vector = [0] * len(vector)#vectorsize
	minv = min(vector)
	maxv = max(vector)
	delta = maxv-minv

	for i in range(len(norm_vector)):
		norm_vector[i] = (vector[i]-minv)/delta

	return norm_vector

def dataset_maker(new_vector_path, source_path, word, dataset, number):
	with open(new_vector_path) as vectorfile:
		vectorlist = vectorfile.read().split()
		# print(vectorlist)
		# input()
	vectorsize = len(vectorlist)

	filelist = []
	for root, dirs, files in os.walk(source_path + "/" + word): 
		for file in files: 
			#append the file name to the list 
			filelist.append(file)

	#print all the file names 
	for name in filelist: 
		print(name)
		vector = [0] * vectorsize
		# print(vector)
		# input()

		with open(source_path + "/" + word + "/" + name) as inputfile:
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

		norm_vector.append(number)

		dataset.append(norm_vector)
		# print(norm_vector)
		# input()

	return dataset

def main():
	vector_path = "/home/slava/Source/KNN_Text_Class/Vector.txt"
	new_vector_path = "/home/slava/Source/KNN_Text_Class/NewVector.txt"
	source_path = "/home/slava/Source/KNN_Text_Class/Dataset"
	#word = "Detective"
	#word = "Space_fiction"

	#repeat_deleter(vector_path, new_vector_path)

	main_dataset = []

	det = dataset_maker(new_vector_path, source_path, "Detective", main_dataset, 0)
	print("----")
	sf = dataset_maker(new_vector_path, source_path, "Space_fiction", main_dataset, 1)

	#main_dataset = [det, sf]#det is 0, sf is 1
	print(len(main_dataset[0]))

	np.save("DSDataset.npy", main_dataset)

if __name__ == "__main__":
	main()