from gensim.models import Word2Vec

Words=["The black-throated loon (Gavia arctica),", "also known as the Arctic loon and the black-throated diver,", "is a migratory aquatic bird found in the northern hemisphere,"]

clean_data=[word.lower().split() for word in Words]

model=Word2Vec(sentences=clean_data,vector_size=4,window=4,min_count=1,epochs=10,workers=2)

word=model.wv["the"]

print(word)


#https://radimrehurek.com/gensim/models/word2vec.html
#https://medium.com/@manansuri/a-dummys-guide-to-word2vec-456444f3c673
