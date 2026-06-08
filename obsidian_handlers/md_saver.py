from pathlib import Path

class MarkDownSaver:
    def __init__(self, obsidian_path):
        self._obsidian_path = Path(obsidian_path)


    def save(self, statue, statue_md):
        dir_path = self._obsidian_path / statue.media_type.replace('/', '-') / statue.franchise.replace('/', '-') / statue.character.replace('/', '-')
        dir_path.mkdir(parents=True, exist_ok=True)

        file_path = dir_path / f"{statue.title.replace(':', '-')}.md"
        file_path.write_text(statue_md, encoding="utf-8")
    
