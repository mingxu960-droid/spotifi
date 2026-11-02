class cancion:
    def __init__(self, id: str, titulo: str, artista: str, duracion: int):
        self.id= id
        self.titulo= titulo
        self.artista= artista
        self.duracion= duracion

    def __str__(self):
        return f"{self.id}.{self.titulo}, nombre artista: {self.artista}, duracion de la cancion: {self.duracion}"

print(cancion(1, "cagar", "marc", "3:49"))


        
