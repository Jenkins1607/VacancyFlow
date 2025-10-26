import httpx
import json
import logg.setup_log_config
import logging
from paths import PathsCustom

logger = logging.getLogger(__name__)


class Response:
    """Получает ответ от API и сохраняет параметры запроса."""
    def __init__(self, method: str, url: str, params: dict):
        self.method = method
        self.url = url
        self.params = params          # сохраняем параметры для дальнейшего использования
        self.data = self.__get_response()

    def __get_response(self):
        try:
            resp = httpx.request(method=self.method, url=self.url, params=self.params)
            logger.info(f"Статус ответа при запросе к {self.url}: {resp.raise_for_status()}")
            data = resp.json()
            return data            # уже Python‑объект (dict)
        except httpx.HTTPError as exc:
            logger.warning(f"HTTP Exception: {exc}")
            


class Dumper:
    """Dump ответа от функции Response._get_response"""
    def __init__(self, response: Response):
        self.response = response
        self.__dump()

    def __dump(self, filename=PathsCustom.response_json):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.response.data, f, indent=4, ensure_ascii=False)
        except TypeError as exc:
            logging.debug(f"Ошибка сериализации: {exc}")

        except IOError as exc:
            logger.info(f"Ошибка ввода-вывода при записи файла response.json: {exc}")
    logger.info("Dump response.json успешно завершен")

class VacanciesLinks:
    """Собирает ссылки вакансий"""
    def __init__(self, response: Response):
        self.response = response
        self.__write()                     

    def __write(self):
        items = self.response.data.get('items', [])
        N = len(items)
        vacancies = []

        
        with open(PathsCustom.vacancies_json, 'w', encoding='utf-8') as f:
            for idx in range(N):

                url = items[idx].get('alternate_url', ' ')
                vac_name = items[idx].get('name', ' ')
                salary = items[idx].get('salary', ' ')
                schedule = items[idx].get('schedule', {}).get('name', ' ')

                line = {
                        'name': vac_name,                
                        'url': url,
                        'salary': salary,
                        'schedule': schedule
                        } # формируем json-строку
                
                vacancies.append(line)
            json.dump(vacancies, f, indent=4, ensure_ascii=False)


def main():
    per_page = int(input("Укажите кол‑во вакансий на одной странице:\n- "))
    page = int(input(f"\nСколько страниц с {per_page} вакансий вы хотите получить?\n- "))
    text = input("\nКакую работу ищете?\n- ")

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
        VacanciesLinks(resp_obj)

if __name__ == '__main__':
    main()
