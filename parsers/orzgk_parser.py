import bs4
from parsers.normalize_data import normalize_media_type

class ORZGKParser:
    def __init__(self):
        pass


    def parse(self, html: str) -> dict:
        _soup = bs4.BeautifulSoup(html, "html.parser")
        statue_data = {}

        title_tag = _soup.select_one(".product-title")
        title_str = title_tag.get_text(strip=True)
        statue_data["title"] = title_str

        meta_blocks = _soup.select(".product_meta_r")
        for block in meta_blocks:
            text = block.get_text(strip=True)

            if text.startswith("Brand:"):
                pref = "Brand:"
                statue_data["studio"] = text[len(pref):]
            elif text.startswith("From:"):
                pref = "From:"
                media_type, franchise = text[len(pref):].split('-')
                statue_data["media_type"] = normalize_media_type(media_type)
                statue_data["franchise"] = franchise
            elif text.startswith("Character:"):
                pref = "Character:"
                statue_data["character"] = text[len(pref):]
            elif text.startswith("Height Range:"):
                pref = "Height Range:"
                statue_data["dimensions"] = text[len(pref):]
            elif text.startswith("Est Released Time:"):
                pref = "Est Released Time:"
                statue_data["release_date"] = text[len(pref):]
            
        
        return statue_data
        

