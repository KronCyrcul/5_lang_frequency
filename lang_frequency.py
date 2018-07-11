import re
import sys
from collections import Counter


def load_data(filepath):
    with open(filepath) as file:
        file_content = file.read()
    pattern = r"[,.:;@#?!&$()\-\u2026]"
    changed_text = re.sub(pattern, " ", file_content).casefold()
    return changed_text.split()


def get_most_frequent_words(text):
    all_words_counts = Counter(text)
    most_common_words = all_words_counts.most_common(10)
    print("10 часто используемых слов:")
    for pair in most_common_words:
        print("{} - {}".format(pair[0], pair[1]))


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        file_content = load_data(filepath)
        get_most_frequent_words(file_content)
    except IndexError:
        sys.exit("Введите путь до файла")
    except FileNotFoundError:
        sys.exit("Файл не найден")
