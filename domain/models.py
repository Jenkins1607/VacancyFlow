from dataclasses import dataclass
from typing import Optional

@dataclass
class Vacancy:
    name: str
    url: str
    salary: Optional[dict]
    schedule: str

