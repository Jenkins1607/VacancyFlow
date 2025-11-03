from application.use_cases import FetchVacanciesUseCase
from infrastructure.hh_api import HhVacancyRepository
from infrastructure.file_saver import JsonFileSaver
from presentation.api import VacancyController
from paths import PathsCustom
from ui import UI


if __name__ == "__main__":
    # настройка зависимостей
    repo = HhVacancyRepository()
    use_case = FetchVacanciesUseCase(repo)
    saver = JsonFileSaver(PathsCustom.vacancies_json)
    controller = VacancyController(use_case, saver)

    text : str = UI.text
    page : int = UI.page
    per_page : int = UI.per_page

    result = controller.handle_fetch_request(
        {
        "text": f"{text}", "page": page, "per_page": per_page
        }
    )

    print(result)