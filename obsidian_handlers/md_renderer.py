from textwrap import dedent

class MarkdownRenderer:
    def __init__(self):
        pass

    def render(self, statue) -> str:
        statue_md = dedent(f"""
            # {statue.title}

            - Status: {statue.status}
            - Studio: {statue.studio}
            - Media type: {statue.media_type}
            - Franchise: {statue.franchise}
            - Character: {statue.character}
            - Dimensions: {statue.dimensions}
            - Release date: {statue.release_date}
        """)

        return statue_md