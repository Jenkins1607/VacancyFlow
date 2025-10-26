from ui.main_interface import UI
from hh_client import (
    Dumper,
    Response,
    SaveVacanciesLinks
    )

def main():

    per_page = UI.per_page
    page = UI.page
    text = UI.text

    params = {
        'per_page': per_page, 
        'page': page, 
        'text': text
        }
    
    url = 'https://api.hh.ru/vacancies'
    method = 'GET'


    resp_obj = Response(method, url, params)
    if resp_obj.data is not None:
        Dumper(resp_obj)
        SaveVacanciesLinks(resp_obj)

if __name__ == '__main__':
    main()