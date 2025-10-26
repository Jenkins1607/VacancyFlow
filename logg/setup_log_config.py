import json
import logging.config
from pathlib import Path

from paths import PathsCustom

with open(PathsCustom.logging_config_json, 'r', encoding='utf-8') as f:
    config = json.load(f)
    print("\nКонфиг успешно загружен\n")

logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
