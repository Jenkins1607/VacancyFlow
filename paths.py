from pathlib import Path

class PathsCustom():
    response_json = Path(__file__).parent /"data"/"response.json"
    vacancies_json = Path(__file__).parent /"data"/"vacancies.json"
    logging_config_json = Path(__file__).parent /"logg"/"logging_config.json"

