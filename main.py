import pymorphy2
import re

verb_count = 0
adv_count = 0
adj_count = 0
morph = pymorphy2.MorphAnalyzer()
reg = re.compile('[^-а-яА-я]')
with open("text.txt", 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.split()
        for word in parts:
            f_word = reg.sub('', word)
            p = morph.parse(f_word)[0]
            print(p)
            if 'VERB' in p.tag:
                verb_count += 1
            elif 'ADVB' in p.tag:
                adv_count += 1
            elif 'ADJF' in p.tag:
                adj_count += 1

print("Количество глаголов:", verb_count)
print("Количество наречий:", adv_count)
print("Количество прилагательных:", adj_count)
