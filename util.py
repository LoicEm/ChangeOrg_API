def chunksamples(l, size_chunks) :
    """Divides a list into chunks of the size given. The last chunk is the rest"""
    relative_size = len(l)//size_chunks
    samples = [ l[i*size_chunks : (i+1)*size_chunks] for i in range(relative_size-1)]
    samples.append(l[size_chunks*relative_size:])
    return samples

def chunkit (l, nb_chunks):
    """divides a list into N roughly equal-sized chunks. The last chunk is always the longest"""
    listoflists = []
    newn = int(len(l) / nb_chunks)
    for i in range(0, nb_chunks-1):
        listoflists.append(l[i*newn:i*newn+newn])
    listoflists.append(l[nb_chunks*newn-newn:])
    return listoflists