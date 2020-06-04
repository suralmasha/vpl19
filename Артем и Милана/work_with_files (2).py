import os
result = {}
inputt = {}
new_dict ={}
amount_frequency = {}
files_frequency = {}
files_paths = {}
list_of_files = []

#получение списка текстовых файлов
def get_list_of_files(list_of_files):
    directory = os.getcwd()
    local_list_files = [file for file in os.listdir(directory) if file.endswith(".txt") and file not in list_of_files]
    list_of_files += local_list_files
    return list_of_files

list_of_files = get_list_of_files(list_of_files)

print(list_of_files)
#словарь с названием файла и его путь
def get_files_paths(list_of_files, files_paths):
    files_paths.update({file: os.path.abspath(file) for file in list_of_files})
    return files_paths

get_files_paths(list_of_files, files_paths)

#вычисления частотности
def get_frequency(file_name: str) -> dict:
    with open(file_name) as data_file:
        info = data_file.read().lower().replace('\n', ' ')
        list_of_words = info.split(' ')

        # создаем сет с словами, чтобы потом для них найти частотность
        one_copy_of_word = set(list_of_words)

        #создаем список с частнотностью слов
        list_frequency = [list_of_words.count(word) for word in one_copy_of_word]

        frequency_of_words = {word: frequency for word, frequency in zip(one_copy_of_word, list_frequency)}
        return frequency_of_words


#частотность слова в тексте
def add_frequency_to_dict(list_of_files: list) -> dict:
    for file_name in list_of_files:
        files_frequency[file_name] = get_frequency(file_name)
    return files_frequency


add_frequency_to_dict(list_of_files)

user = input()

def top_frequency(user):
    user = user.lower()
    for k,v in files_frequency.items():
        amount_frequency[k] = files_frequency[k][str(user)]
    return amount_frequency

top_frequency(user)
print(amount_frequency)

def word_getting(list_of_files):
    for files_name in list_of_files:
        with open(files_name) as data_file:
            info = data_file.read().lower().replace('\n', ' ')
            list_of_words = info.split(' ')
            inputt[files_name] = list_of_words
            for k, v in inputt.items():
                if user in v:
                    index = int(list_of_words.index(user))
                    result[k] = v[index-5:index+5]      
                    print(result)
    return result

word_getting(list_of_files)

        
'''
index = int(list_of_words.index(user))
            for i in list_of_files:
                inputt[i] = list_of_words[index-2:index+2]
            print(inputt)
'''

