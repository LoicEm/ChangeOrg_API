import random,csv
from get_petition import get_petitions_from_ids
import time
from threading import Thread
import queue
from config import API_keys
from util import chunkit

class fetcheur(Thread) :
    def __init__(self, api_key,out_queue, number):
        Thread.__init__(self)
        self.part = chunk_queue.get()
        self.api_key = api_key
        self.out_queue = out_queue
        self.number = number

    def run(self):
        fetch_part = get_petitions_from_ids(self.part, key = self.api_key)
        for response in fetch_part :
            try  :
                self.out_queue.put(response)
            except :
                continue
        print('Thread %s finished'%self.number)
        self.out_queue.put((None,None))


class writer(Thread) :
    """From the queue given by the fetchers, write to the file the responses and in another file the ids already fetched"""
    def __init__(self, in_queue, out_file, requested_file):
        Thread.__init__(self)
        self.in_queue = in_queue
        self.out_file = out_file
        self.requested_file = requested_file

    def run(self):
        none_counter = 0
        while True:
            batch, requested_ids = self.in_queue.get()
            if batch is None:
                none_counter +=1
                print(none_counter)
                if none_counter == nb_chunks:
                    break
                continue
            for petition in batch :
                self.out_file.write(str(petition) + '\n')
            for id in requested_ids :
                self.requested_file.write(str(id) + '\n')
            self.in_queue.task_done()
        print('writing finished')

with open('data/requested.txt') as rfile :
    lines =  [i.strip() for i in rfile.readlines()]

ids = [str(i) for i in range(256960, 8350000)]
len_ids = len(ids)
print('Removing already requested ids')
ids = list(set(ids) - set(lines))
print('%s out of %s ids have been kept'%(len(ids), len_ids))
del lines

random.shuffle(ids)

nb_chunks = len(API_keys)
chunks = chunkit(ids, nb_chunks)

print('Starting queue')
q = queue.Queue()
chunk_queue = queue.Queue()

for chunk in chunks :
    chunk_queue.put(chunk)

requested_path = 'data/requested.txt'
petitions_path = 'data/petitions.csv'

for i in range(nb_chunks) :
    t = fetcheur(API_keys[i], q, i)
    t.setDaemon(True)
    t.start()

with open(petitions_path, 'a', encoding='utf8') as petitions_file, open(requested_path, 'a') as requested_file :
    t = writer(q, petitions_file,requested_file)
    t.start()
    chunk_queue.join()
    q.join()