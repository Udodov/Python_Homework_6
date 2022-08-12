import os
import codecs


def read_from_file(path_file: str) -> str:
    with codecs.open(path_file, 'r', encoding='utf-8') as file:
        return file.readline()


path = os.path.join('documentation6', 'task_6.1.txt')

read_text = read_from_file(path).split()
print(f'There is text in the file:\n ', " ".join(read_text))
deleted_word = input('Enter the word you want to remove from the text as a string:')

del_some_words = [item for item in read_text if deleted_word not in item]

print()
print(f'The final text looks like this:\n ', " ".join(del_some_words))
