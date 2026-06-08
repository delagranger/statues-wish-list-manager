import logging

import config
from parsers.html_loader import HTMLLoader
from parsers.orzgk_parser import ORZGKParser
from exceptions import HTMLLoaderError
from models.statue import Statue
from obsidian_handlers.md_renderer import MarkdownRenderer
from obsidian_handlers.md_saver import MarkDownSaver

config.logging_setup()
log = logging.getLogger(__name__)

if __name__ == "__main__":
    try:    
        html_loader = HTMLLoader()
        url = "https://www.orzgk.com/product/iron-studio-statue-voldemort-and-nagini-harry-potter-legacy-replica-1-4/"
        html = html_loader.load(url)
        log.info("Load HTML: SUCCESS; HTML length = %s", len(html))
    except HTMLLoaderError as e:
        log.error("Load HTML: FAILED\nERROR: %s", e)

    parser = ORZGKParser()
    statue_data = parser.parse(html)
    statue = Statue(url, statue_data)

    md_renderer = MarkdownRenderer()
    statue_md = md_renderer.render(statue)
    print(statue_md)

    obsidian_path = config.get_obsidian_path()
    print(obsidian_path)
    md_saver = MarkDownSaver(obsidian_path)
    md_saver.save(statue, statue_md)

