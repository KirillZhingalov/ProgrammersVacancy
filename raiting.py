from os.path import exists

from helpful_func import load_from_json


def make_dict_of_languages():
    languages = {'1C': {'synonyms': ['1C']},
                 'C/C++': {'synonyms': ['C', 'C++', 'C/C++']},
                 'Python': {'synonyms': ['python']}, 
                 'Perl': {'synonyms': ['Perl']}, 
                 'Ruby': {'synonyms': ['Ruby']},
                 'C#': {'synonyms': ['C#', '.Net']},
                 'Objective-C': {'synonyms': ['Swift', 'ios', 'Obj-c', 'Objective-C']},
                 'PHP': {'synonyms': ['PHP']},
                 'Delphi': {'synonyms': ['Delphi']},
                 'Java': {'synonyms': ['Java', 'Android']},
                 'Assembler': {'synonyms': ['Assembler']},
                 'R': {'synonyms': ['R']},
                 'JavaScript': {'synonyms': ['JS', 'JavaScript']},
                 'SQL': {'synonyms': {'SQL', 'MySQL', 'PostgreSQL'}}
    } 
    for language in languages.keys():
        languages[language].update({'vacancy_count': 0, 'average_payment': 0})
    return languages 


def is_lang_detected(languages, text):
    for language in languages.keys():
        for synonym in languages[language]['synonyms']:
            if synonym.lower() in text.lower():
                return language
    return False


def update_dict(language, payment, languages_dict):
    languages_dict[language]['vacancy_count'] += 1
    languages_dict[language]['average_payment'] += payment
    return languages_dict 


def get_average_payment(languages_dict):
    for language in languages_dict.keys():
        if languages_dict[language]['vacancy_count']:
            languages_dict[language]['average_payment'] /= languages_dict[language]['vacancy_count']
    return languages_dict

if __name__ == "__main__":
    input_file = input('Enter filename with vacancy data: ')
    if not exists(input_file):
        print('Ooops, file not found...')
        exit()
    languages_dict = make_dict_of_languages()
    vacancies = load_from_json(input_file)
    for vacancy in vacancies:
        language = is_lang_detected(languages_dict, vacancy['profession'])
        if not language:
            language = is_lang_detected(languages_dict, vacancy['candidat'])
            if not language:
                continue
        payment = (vacancy['payment to'] + vacancy['payment from']) / 2
        languages_dict = update_dict(language, payment, languages_dict)
    languages_dict = get_average_payment(languages_dict)
    for language in languages_dict.keys():
        if languages_dict[language]['vacancy_count']:
            print('%s. Count of vacancies: %d\nAverage_payment: %d' %
                  (language, languages_dict[language]['vacancy_count'],
                  languages_dict[language]['average_payment']))
