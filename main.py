import os
from osumap import *
from utils import *

print('You\'re Welcome !')

#path = input('Entrez le chemin de votre map : ')
path = '/Users/jeanbaptistecaplan/Documents/py/osu/map_valide.osu'
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
		

map = Map(mapLinesArray)

timingPoints = map.extractTimingPoints()
hitObjects = map.extractHitObjects()

print(len(timingPoints))
print(len(hitObjects))

#print('Cette map est réalise pour la version', map.osuVersion, 'de OSU')
#print('Le nom de la map est', map.title)
#print('Le créateur de la map est', map.creator)
#print('Le fichier audio associé est', map.audioFilename)
#print('beatmapID :', map.beatmapID)
#print('circleSize :', map.circleSize)
#print('tags :', map.tags)