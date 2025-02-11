class Game:
    def __init__(self, id, name, genre, jaar, uitgever):
        self.id = id
        self.name = name
        self.genre = genre
        self.jaar = jaar
        self.uitgever = uitgever

    def __str__(self):
        return f"{self.id} - {self.name} - {self.genre} - {self.jaar} - {self.uitgever}"