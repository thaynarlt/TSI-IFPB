
class VideoGame:
	contador = 0

	def __init__(self, marca="Sony", modelo="PS5", data_fabricacao=None):
		self.marca: str = marca
		self.modelo: str = modelo
		self.data_fabricacao: str = data_fabricacao if data_fabricacao else "25/08/2023"
		VideoGame.contador += 1
		self.numero_serie: int = VideoGame.contador
		self.capacidade: int = 1024 # MB
		self.jogos_instalados = ["Overwatch", "Fifa", "Fortnite", "GTA"]



v1 = VideoGame()
v2 = VideoGame("10/07/2020")
v3 = VideoGame(marca="Micro$oft", modelo="XBox Peba", data_fabricacao="01/04/1980")