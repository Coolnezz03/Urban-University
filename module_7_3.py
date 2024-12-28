class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = list(file_name)

    def get_all_words(self):
        all_words = {}
        punkt = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_name:
            with open(name, encoding= 'utf-8') as file:
                text = file.read().lower()
                for char in punkt:
                    text = text.replace(char, '')
                words = text.split()
                all_words[name] = words
        return all_words

    def find(self, word):
        finders = {}
        for name, item in self.get_all_words().items():
            for i in range(len(item)):
                 if word.lower() == item[i]:
                     finders[name] = i+1
                     break
        return finders

    def count(self, word):
        finders = {}
        for name, item in self.get_all_words().items():
            j = 0
            for i in range(len(item)):
                if word.lower() == item[i]:
                    j += 1
            finders[name] = j
        return finders



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
for i in finder1.get_all_words().items():
    print(i)
print(finder1.find('the'))
print(finder1.count('the'))