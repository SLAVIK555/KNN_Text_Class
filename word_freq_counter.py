import os

def string_norm(str1):
	string = str(str1.lower())

	if string.find('.'):
		string = string.replace('.', '')

	if string.find(','):
		string = string.replace(',', '')

	if string.find(':'):
		string = string.replace(':', '')

	if string.find(';'):
		string = string.replace(';', '')

	if string.find('-'):
		string = string.replace('-', '')

	if string.find('_'):
		string = string.replace('_', '')

	if string.find('!'):
		string = string.replace('!', '')

	if string.find('?'):
		string = string.replace('?', '')

	return string

def word_freq_counter(source_path, stoppath, word):
	filelist = []
	for root, dirs, files in os.walk(source_path + "/" + word): 
		for file in files: 
			#append the file name to the list 
			filelist.append(file)

	#print all the file names 
	for name in filelist: 
		print(name)

	with open(stoppath) as stopfile:
		stoplist = stopfile.read().split()
	#print (stoplist)

	main_word_filelist = []
	main_freq_filelist = []

	print("-----------------")

	for name in filelist: 
		print(name)
		#input()

		with open(source_path + "/" + word + "/" + name) as inputfile:
			list_data = inputfile.read().split() # читаем с файла разбиваем по пробелам
			#print(list_data)
			for item in list_data:
				litem = string_norm(item)
				if litem not in stoplist:
					#print(litem)
					#input()
					if litem in main_word_filelist:
						litem_index = main_word_filelist.index(litem)
						litem_freq = main_freq_filelist[litem_index]
						new_litem_freq = litem_freq + 1
						main_freq_filelist[litem_index] = new_litem_freq
					else:
						main_word_filelist.append(litem)
						main_freq_filelist.append(1)

	outfile = open(word + ".txt", 'w')

	for i in range(2000):
		max_item_freq = max(main_freq_filelist)
		max_index = main_freq_filelist.index(max_item_freq)
		max_item_word = main_word_filelist[max_index]

		outstring = str(max_item_freq) + ": " + str(max_item_word) + "\n"

		outfile.write(outstring)

		main_word_filelist.pop(max_index)
		main_freq_filelist.pop(max_index)

	outfile.close()

def main():
	source_path = "/home/slava/Source/KNN_Text_Class/Dataset"
	stoppath = "/home/slava/Source/KNN_Text_Class/stopwords.txt"
	#word = "Detective"
	word = "Space_fiction"

	word_freq_counter(source_path, stoppath, word)

if __name__ == "__main__":
	main()