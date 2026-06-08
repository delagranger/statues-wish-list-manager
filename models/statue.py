class Statue:
    def __init__(self, url, data):
        self.status = "Not purchased"
        self.title = data["title"]
        self.studio = data["studio"]
        self.url = url
        self.media_type = data["media_type"]
        self.franchise = data["franchise"]
        self.character = data["character"]
        self.dimensions = data["dimensions"]
        self.release_date = data["release_date"]

    def __str__(self):
        return "Status: %s\n" \
               "Title: %s\n" \
               "Studio: %s\n" \
               "URL: %s\n" \
               "Media type: %s\n" \
               "Franchise: %s\n" \
               "Character: %s\n" \
               "Dimensions: %s\n" \
               "Release date: %s\n" % (
                   self.status, 
                   self.title, 
                   self.studio, 
                   self.url,
                   self.media_type, 
                   self.franchise, 
                   self.character, 
                   self.dimensions, 
                   self.release_date)
    