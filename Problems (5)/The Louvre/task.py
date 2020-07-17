class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def full_title(self):
        return f"\"{self.title}\" by {self.artist} ({self.year}) hangs in the Louvre."


input_title = input()
input_artist = input()
input_year = input()

painting = Painting(input_title, input_artist, input_year)

print(painting.full_title())
