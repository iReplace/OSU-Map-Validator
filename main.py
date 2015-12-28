import os
from osumap import *
from utils import *
from math import *

#path = input('Entrez le chemin de votre map : ')
path = '/Users/jeanbaptistecaplan/Documents/py/osu/map_valide.osu'
path = '/Users/jeanbaptistecaplan/Documents/py/osu/S3RL - MTC (Different Heaven Remix) (-Genesis) [Aeon\'s Taiko Oni].osu'
#path = '/Users/jeanbaptistecaplan/Documents/py/osu/map_invalide.osu'

# On ouvre, on stocke toute les lignes puis on referme le fichier
mapFile = open(path, 'r')
mapLinesArray = mapFile.readlines()
mapFile.close()
	
# On cherche la position du marqueur "[HitObjects]"
HitObjectPosition = search("[HitObjects]\n", mapLinesArray)
if (HitObjectPosition < 0):
	raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[HitObjects]"')

# On cherche la position du marqueur "[TimingPoints]"
TimingPointsPosition = search("[TimingPoints]\n", mapLinesArray)
if (TimingPointsPosition < 0):
	raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[TimingPoints]"')
		

# Initialisation d'un objet Map à partir des données tirées du fichier
map = Map(mapLinesArray)

# Récupération des TimingPoints et HitObjects depuis l'objet map
timingPoints = map.extractTimingPoints()
hitObjects = map.extractHitObjects()

map.printEditor()

# Petite boucle de calcul de la distance entre les [HitObjects] consécutifs
#for i, el in enumerate(hitObjects):
#	if (type(el) is Spinner):
#		print(el.time)
#	if (i > 0):
#		x = hitObjects[i-1].x - el.x
#		y = hitObjects[i-1].y - el.y
#		distance = sqrt(x**2 + y**2)
#		print(distance)