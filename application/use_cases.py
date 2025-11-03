from application.interfaces import VacancyRepository
from domain.models import Vacancy
from typing import List

class FetchVacanciesUseCase:
    """Use Case: получить и обработать вакансии"""
    def __init__(self, repo: VacancyRepository):
        self.repo = repo
    
    def execute(self, query_params: dict):
        raw_data: dict = self.repo.fetch_raw_data(query_params=query_params)
        return self._parse_vacancies(raw_data)

    def _parse_vacancies(self, raw_data: dict) -> List[Vacancy]:
        items = raw_data.get('items', [])
        N = len(items)
        vacancies = []

        for idx in range(N):
                url = items[idx].get('alternate_url', ' ')
                vac_name = items[idx].get('name', ' ')
                salary = items[idx].get('salary', ' ')
                schedule = items[idx].get('schedule', {}).get('name', ' ')

                vacancy = Vacancy(
                        name=vac_name,                
                        url=url,
                        salary=salary,
                        schedule=schedule,
                    ) 
                
                vacancies.append(vacancy)
                
        return vacancies