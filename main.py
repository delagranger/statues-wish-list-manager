import os
import logging
from dotenv import load_dotenv

from parsers.html_loader import HTMLLoader

def _logging_setup():
    load_dotenv()
    log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level_str)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        handlers=[logging.StreamHandler()]
    )

    return log_level_str

if __name__ == "__main__":
    log_level = _logging_setup()
    log = logging.getLogger(__name__)
    log.info("Logging is started with level %s", log_level)

    html_loader = HTMLLoader()
    url = "https://www.orzgk.com/product/hundian-studio-bloodborne-serieslady-maria-of-the-astral-clocktower/" 
    html = html_loader.load(url)
    log.info("Load HTML: SUCCESS; HTML length = %s", len(html))

