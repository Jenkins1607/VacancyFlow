import logging
import logg.setup_log_config
import logging

logger = logging.getLogger(__name__)

def tests_colorlog():
    print("ПРОВЕРКА РАБОТЫ ЛОГГЕРОВ\n")

    logger.debug("Отладка")
    logger.info("Информация")
    logger.warning("Предупреждение")
    logger.error("Ошибка")
    logger.critical("Критическая ошибка")

    print("\nПРОВЕРКИ ЗАКОНЧЕНЫ\n")

tests_colorlog()