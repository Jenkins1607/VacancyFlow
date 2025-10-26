import httpx
import json
from paths import PathsCustom
import logging
import logg.setup_log_config

logger = logging.getLogger(__name__)

class VacancyService:
    def fetch_vacancies(method: str, url: str, params: dict) -> dict:
        try:
            resp = httpx.request(method=method, url=url, params=params)
            resp.raise_for_status()
            data = resp.json()

            logger.info(f"Успешный ответ от {url}")

            return data    
             
        except httpx.HTTPError as exc: 
            logger.warning(f"HTTP Exception: {exc}")


    def save_raw_response(filename, response) -> None:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(response.data, f, indent=4, ensure_ascii=False)
        except TypeError as exc:
            logging.debug(f"Ошибка сериализации: {exc}")

        except IOError as exc:
            logger.debug(f"Ошибка ввода-вывода при записи файла response.json: {exc}")
        logger.info("Dump response.json успешно завершен")

    def save_filtered_vacancies(response: dict):
        items = response.get('items', [])
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