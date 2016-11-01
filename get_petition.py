# -*- coding: utf-8 -*-
import requests, argparse, random
from config import API_Key
from util import chunksamples
from time import sleep

request_url = 'https://api.change.org/v1/petitions'
parser = argparse.ArgumentParser(description='Running this script with an id as argument wil return the petition associated with that id')
parser.add_argument('petition_id', nargs = '?', default = [i for i in range(5000000,5005000)]  )
args = parser.parse_args()


def get_petitions_from_ids (ids, random_sample = False, key = API_Key):
    ids = [str(id) for id in ids]
    if len(ids) > 500: #We need to make multiple requests as the max size of a response is 500 petitions
        if random_sample :
            random.shuffle(ids)
        list_ids = chunksamples(ids, 500)
    else: list_ids = [ids]
    for chunk in list_ids:
        except_counter = 0
        while True :
            try :
                params = {'api_key' : key,
                        'petition_ids' : ','.join(chunk)}
                request = requests.get(request_url,params=params)
                print(request)
                yield request.json()['petitions'], chunk
                break
            except Exception as e:
                except_counter += 1
                if except_counter < 10:
                    print('An exception occured, trying again in 6 seconds')
                    sleep(6)
                else :
                    print(request.text)
                    raise e

def get_single_petition(id) :
    """from a single id, get the petition"""
    return get_petitions_from_ids([id])

if __name__ == '__main__' :
    out_res = []
    res = get_petitions_from_ids(args.petition_id)
    for i in res :
        print(i['petitions'])
        out_res.append(i)