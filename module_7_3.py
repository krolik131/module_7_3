class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for file_name in file_names:
            self.file_names.append(file_name)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break

                    line = line.lower()
                    if ',' or '.' or '=' or '!' or '?' or ';' or ':' or  ' - ' in line:
                        line = line.replace(',', '')
                        line = line.replace('.', '')
                        line = line.replace('=', '')
                        line = line.replace('!', '')
                        line = line.replace('?', '')
                        line = line.replace(';', '')
                        line = line.replace(':', '')
                        line = line.replace(' - ', '')
                        line = line.split()
                        if all_words == {}:
                            all_words[file_name] = line
                        else:
                            all_words[file_name] += line
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words().items()
        word = word.lower()
        for file_name, words in all_words:
            if word in words:
                result[file_name] = words.index(word) + 1
                return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words().items()
        word = word.lower()
        for file_name, words in all_words:
            if word in words:
                result[file_name] = words.count(word)
        return result

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))