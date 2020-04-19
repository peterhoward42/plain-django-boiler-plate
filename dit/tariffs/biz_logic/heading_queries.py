from ..models import LastUpdated


class HeadingQueries:

    def __init__(self, heading: str):
        self.heading = heading

    def is_in_database(self) -> bool:
        return LastUpdated.objects.filter(heading=self.heading).exists()
