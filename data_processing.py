import os.path

from helpful_func import load_from_json, save_to_json


def processing(input_file, output_file):
    vacancies = load_from_json(input_file)
    clear_vacancies = []
    for vacantion in vacancies:
        clear_vacancies.append({'profession': vacantion['profession'],
                                'payment from': vacantion['payment_from'], 
                                'payment to': vacantion['payment_to'],
                                'candidat': vacantion['candidat']})
    save_to_json(clear_vacancies, output_file)

if __name__ == "__main__":
    input_file = input('Enter file with catalog of vacancies: ')
    if not os.path.exists(input_file):
        print('Ooops, file not found...')
        exit()
    output_file = input('Where do you want to save new catalog? ')
    processing(input_file, output_file)
    if os.path.exists(output_file): print("Done")
    else: print("Error")  
