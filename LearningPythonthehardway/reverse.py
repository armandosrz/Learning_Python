def reverse_words(str):
  #go for it
  words = str.split(' ')
  for word in range(len(words)):
    words[word] = words[word][::-1]
    print words[word]
  return False

reverse_words('Hello Armando')
