import httpx
import json
from paths import PathsCustom
from services.vacancy_service import VacancyService


class Response:
    """Получает ответ от API и сохраняет параметры запроса."""
    def __init__(self, method: str, url: str, params: dict):
        self.method = method
        self.url = url
        self.params = params # сохраняем параметры для дальнейшего использования
        self.data = self.__get_response()

    def __get_response(self) -> dict:

        data = VacancyService.fetch_vacancies(
            method=self.method,
            url=self.url,
            params=self.params
            )
        
        return data

class Dumper:
    """Dump ответа от функции Response._get_response"""
    def __init__(self, response: Response):
        self.response = response
        self.__dump()

    def __dump(self, filename=PathsCustom.response_json):
        VacancyService.save_raw_response(filename, self.response)
        return

class SaveVacanciesLinks:
    """Запись вакансий в vacancies.json"""
    def __init__(self, response: Response):
        self.response = response
        self.__write()                     

    def __write(self):
        VacancyService.save_filtered_vacancies(self.response.data)

