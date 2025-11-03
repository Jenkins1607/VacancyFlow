from application.interfaces import VacancyRepository
import httpx
import logging
import logg.setup_log_config

logger = logging.getLogger(__name__)

class HhVacancyRepository(VacancyRepository):
    """Адаптер: получает данные с hh api"""
    BASE_URL = 'https://api.hh.ru/vacancies'
    def fetch_raw_data(self, query_params: dict):
        try:
            resp = httpx.request(method='GET',url=self.BASE_URL, params=query_params)
            resp.raise_for_status()
            data = resp.json()

            logger.info(f"Успешный ответ от {self.BASE_URL}")

            return data    
            
        except httpx.HTTPError as exc: 
            logger.warning(f"HTTP Exception: {exc}")
