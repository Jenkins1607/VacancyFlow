from application.use_cases import FetchVacanciesUseCase
from infrastructure.file_saver import JsonFileSaver

class VacancyController:
    def __init__(self, use_case: FetchVacanciesUseCase, saver: JsonFileSaver):
        self.use_case = use_case
        self.saver = saver

    def handle_fetch_request(self, query_params: dict):
        vacancies = self.use_case.execute(query_params=query_params)
        self.saver.save_vacancies(vacancies)
        return {"count": len(vacancies), "saved_to": self.saver.file_path}