import argparse
from config import API_Key
import requests

parser = argparse.ArgumentParser(description='If you run this script with a petition url as argument, will return the id associated with this petition. If no url is provided will make a request to the following link : https://www.change.org/p/etiquetage-nutritionnel-alimentaire-les-consommateurs-fran%C3%A7ais-veulent-le-code-5-couleurs')
parser.add_argument('url', nargs = '?', default = 'https://www.change.org/p/etiquetage-nutritionnel-alimentaire-les-consommateurs-fran%C3%A7ais-veulent-le-code-5-couleurs' ,
                    help = 'The url we want to fetch the id from')
args = parser.parse_args()

request_url = 'https://api.change.org/v1/petitions/get_id'

def get_id(url_request):
    data =  {'api_key' : API_Key,
            'petition_url' : url_request}
    request = requests.get(request_url,params = data)
    return request.json()['petition_id']

if __name__ == '__main__' :
    res = get_id(args.url)
    print(res)