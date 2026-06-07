class Statue:
    def __init__(self, ):
        character: str
        title: str 
        franchise: str 
        studio: str 
        media_type: str # Allowed values ["Anime", "Games", "Movies", "Series", "Other"]
        url: str 
        price: str | None
        release_date: str | None
        dimensions: str | None
        images: list[str]
        selected_images: list[str]
        status: str = "Not Purchased"