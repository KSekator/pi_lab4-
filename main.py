import pymorphy2
import re

total_words = 0
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
            if f_word != '':
                total_words += 1
            if 'VERB' in p.tag or 'INFN' in p.tag:
                verb_count += 1
            elif 'ADVB' in p.tag:
                adv_count += 1
            elif 'ADJF' in p.tag or 'ADJS' in p.tag:
                adj_count += 1

print("Всего слов:", total_words)
print("Количество глаголов:", verb_count, '—', round(verb_count/total_words*100, 2), '%')
print("Количество наречий:", adv_count, '—', round(adv_count/total_words*100, 2), '%')
print("Количество прилагательных:", adj_count, '—', round(adj_count/total_words*100, 2), '%')
