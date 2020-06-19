words_count={}
fh=open('words.txt')
for lines in fh:
    words=lines.split()
    for word in words:
        words_count[word]=words_count.get(word,0)+1
print(words_count.items())
