from gensim.models import Word2Vec

Words=["The black-throated loon (Gavia arctica),", "also known as the Arctic loon and the black-throated diver,", "is a migratory aquatic bird found in the northern hemisphere,"]

clean_data=[word.lower().split() for word in Words]

model=Word2Vec(sentences=clean_data,vector_size=4,window=4,min_count=1,epochs=10,workers=2,min_alpha=0.5,compute_loss=True)



def loop():
    wordlist=[i.lower().split() for i in Words]
    for t in wordlist:
        b=model.wv[t]
        return b
        
        #b=model.wv[i]
        #return b

word=model.wv["the"]



print(word, model.get_latest_training_loss())
loop()


#

#https://radimrehurek.com/gensim/models/word2vec.html
#https://medium.com/@manansuri/a-dummys-guide-to-word2vec-456444f3c673
