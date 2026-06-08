NORMALIZATION_MAP = {
    "Video Game Figure" : "Games",

    "Anime Figure" : "Anime",

    "Movie" : "Movies",
    "Movie / TV Show Figure" : "Movies", 
}

def normalize_media_type(media_type: str) -> str:
    return NORMALIZATION_MAP[media_type]