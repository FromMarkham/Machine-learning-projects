def my_positional_encoding(sentence_length,vector_length,n=10000):
    positionalEncodingVector=np.zeros((sentence_length,vector_length))

    for kVectorposition in range(sentence_length):
        for i in np.arange(int(vector_length/2)):
            denominator=np.power(n,2*i/sentence_length)
            positionalEncodingVector[kVectorposition]=np.sin(kVectorposition/denominator)
            positionalEncodingVector[kVectorposition]=np.sin(kVectorposition/denominator)
           
    return positionalEncodingVector

positionvectors=my_positional_encoding(sentence_length=6,vector_length=6,n=10000)
print(positionvectors)
