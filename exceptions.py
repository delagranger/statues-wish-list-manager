class ApplicationError(Exception):
    pass


class HTMLLoaderError(ApplicationError):
    def __init__(self, message: str):
        super().__init__(f"Unable to load HTML\n{message}")

