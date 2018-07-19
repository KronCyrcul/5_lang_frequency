import re
import sys
from collections import Counter


def load_data(filepath):
    with open(filepath) as file:
        text_string = file.read()
    return text_string


<<<<<<< HEAD
def get_most_frequent_words(text, top_n):
=======
def get_most_frequent_words(text):
    top_n = 10
>>>>>>> d907c61383f15c8a0cc581e9f8869007a7e35a03
    pattern = r"[A-z]+"
    changed_text = re.sub(pattern, " ", text_string).casefold()
    words_frequencies = Counter(changed_text.split())
    most_common_words = words_frequencies.most_common(top_n)
<<<<<<< HEAD
    return most_common_words
=======
    print("10 часто используемых слов:")
    for word, frequency in most_common_words:
        print("{} - {}".format(word, frequency))
>>>>>>> d907c61383f15c8a0cc581e9f8869007a7e35a03


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
        text_string = load_data(filepath)
        most_common_words = get_most_frequent_words(text_string, 10)
        print("10 часто используемых слов:")
        for word, frequency in most_common_words:
            print("{} - {}".format(word, frequency))
    except IndexError:
        sys.exit("Введите путь до файла")
    except FileNotFoundError:
        sys.exit("Файл не найден")
