import os.path
from sys import exit
from helpful_func import make_request, save_to_json


def get_programmers(api_key):
    params = {'town': 'Moscow', 'catalogues': 48, 'count': 100, 
              'keyword': ['Программист', 'Разработчик']}
    return make_request('vacancies/', api_key, params).json()

if __name__ == "__main__":
    api_key = input('Input your api key: ')
    list_of_vacancies = get_programmers(api_key)
    list_of_vacancies = list_of_vacancies['objects']
    output_file = input('Enter output file name: ')
    if os.path.exists(output_file):
        answer = input("File exist. Would you like to rewrite him?(y/n) ")
        if answer.lower() == "n" or answer.lower() == "no":
            exit()
    save_to_json(list_of_vacancies, output_file)
    if os.path.exists(output_file):
        print("Done")
    else:
        print("Houston, we have a problem. File is not created")
