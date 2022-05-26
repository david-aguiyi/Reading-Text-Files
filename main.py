import string

def read_file_content(filename):
    file = open(filename, "r")
    file = file.readlines()
    return file


def count_words():
    text = read_file_content("./story.txt")
    dictionary = {}
    for line in text:
        line = line.lower()
        line = line.strip()
        line = line.translate(line.maketrans('','', string.punctuation))
        line = line.split()

        words = line

        for word in words:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    for key in list(dictionary.keys()):
        print(f"{{\"{key}\": {dictionary[key]}}},", end=" ")
count_words()