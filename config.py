from dotenv import load_dotenv
import os
import logging

def logging_setup():
    load_dotenv()
    _log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
    _log_level = getattr(logging, _log_level_str)

    logging.basicConfig(
        level=_log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        handlers=[logging.StreamHandler()]
    )

    log = logging.getLogger(__name__)
    log.info("Logging is started with level %s", _log_level_str)


def get_obsidian_path() -> str:
    load_dotenv()
    obsidian_path = os.getenv("OBSIDIAN_PATH")
    return obsidian_path