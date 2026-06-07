import os
import logging
from dotenv import load_dotenv

from parsers.html_loader import HTMLLoader
from parsers.orzgk_parser import ORZGKParser
from exceptions import HTMLLoaderError
from models.statue import Statue
from obsidian_handlers.md_renderer import MarkdownRenderer
from obsidian_handlers.md_saver import MarkDownSaver

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

    try:    
        html_loader = HTMLLoader()
        url = "https://www.orzgk.com/product/real-studio-jujutsu-kaisen-sukuna-flame-arrow/"
        html = html_loader.load(url)
        log.info("Load HTML: SUCCESS; HTML length = %s", len(html))
    except HTMLLoaderError as e:
        log.error("Load HTML: FAILED\nERROR: %s", e)

    parser = ORZGKParser()
    statue_data = parser.parse(html)
    statue = Statue(statue_data)
    print(str(statue))

    md_renderer = MarkdownRenderer()
    statue_md = md_renderer.render(statue)
    print(statue_md)

    md_saver = MarkDownSaver()
    md_saver.save(statue, statue_md)

