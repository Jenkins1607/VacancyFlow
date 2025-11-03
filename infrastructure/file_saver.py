from domain.models import Vacancy
from pathlib import Path
import json


class JsonFileSaver:
    """Адаптер: сохраняет вакансии в json"""
    def __init__ (self, file_path: Path):
        self.file_path = file_path

    def save_vacancies(self, vacancies: Vacancy) -> None:
        data = [{
            "name": v.name,
            "url": v.url,
            "salary": v.salary,
            "schedule": v.schedule,
            }
        for v in vacancies
        ]

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

