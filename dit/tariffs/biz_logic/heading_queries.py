from ..models import Heading


class HeadingQueries:

    def __init__(self, heading: str):
        self.heading = heading

    def is_in_database(self) -> bool:
        return Heading.objects.filter(heading_digits=self.heading).exists()
