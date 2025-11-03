from abc import ABC, abstractmethod

class VacancyRepository(ABC):
    """Порт: как приложение получает вакансии"""
    @abstractmethod
    def fetch_raw_data(self, query_params: dict):
        pass


