from pathlib import Path

class PathsCustom():
    response_json = Path(__file__).parent /"vacancies"/"response.json"
    vacancies_json = Path(__file__).parent /"vacancies"/"vacancies.json"
    logging_config_json = Path(__file__).parent /"logg"/"logging_config.json"

