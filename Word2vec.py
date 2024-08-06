from gensim.models import Word2Vec

sentences=["A Rubens tube, also known as a standing wave", "flame tube, or simply flame tube, is a physics apparatus", "for demonstrating acoustic standing waves in a tube.", "Invented by German physicist Heinrich Rubens in 1905," ,"it graphically shows the relationship between sound waves and sound pressure,", "as a primitive oscilloscope. Today, it is used only occasionally,", "typically as a demonstration in physics education."]

sentenceprocess=[words.lower().split() for words in sentences]

model=Word2Vec(sentences=sentenceprocess,vector_size=5,window=1,min_count=1,workers=2)

word=model.wv["rubens"]

print(word)
