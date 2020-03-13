
f = open('text.txt',encoding = 'utf-8')
  # 1.методами строк очистить текст от знаков препинания

a = f.read()
# print(a)
c = "".join(c for c in a if c not in ('!','.',':',',','?',';','»','—','«',')','('))
# print(len(c))

  # 2.сформировать list со словами (split)

d = c.lower() # 3. привести все слова к нижнему регистру
a_list = d.split() # list со словами
print(a_list)
# print(len(a.split()))


  # 4.получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

word_dic = {}
for word in a_list:
    try:
        word_dic[word] = word_dic[word]+1
    except KeyError:
        word_dic[word] = 1
print (word_dic)

  # 5.вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)

a_list.sort()
print (sorted([(value, key ) for (key,value) in word_dic.items()])[-5:]) # 5 наиболее часто встречающихся слов (sort)
w = set(a_list)
print(len(w)) # количество разных слов в тексте (set)
print(w)
