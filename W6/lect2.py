song = '''
Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
All the king's horses and all the king's men
Couldn't put Humpty together again
Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
All the king's horses and all the king's men
Couldn't put Humpty together again
Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
All the king's horses and all the king's men
Couldn't put Humpty together again
'''

lista = song.lower().replace("\"","").replace("\'","").replace(",","").split()

#print(type(lista))

word_dict = {}

#for word in lista:
 # if word in word_dict:
 #   word_dict[word] += 1
 # else:
 #   word_dict[word]  = 1


for item in lista:
  word_dict[item] = word_dict.get(item,0) +1

print(dict(sorted(word_dict.items(), key = lambda x: x[1]))) 