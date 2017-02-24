import requests
import json


def make_request(method, api_key, param=None):
    header = {'X-Api-App-Id': api_key}
    return requests.get('https://api.superjob.ru/2.0/%s' % method,
                        headers=header, params=param)


def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_from_json(input_file):
    with open(input_file, 'r') as file:
        return json.load(file)
