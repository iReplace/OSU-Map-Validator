from utils import *

# TODO:
#	- Implémenter la récupération des évènements
#	-
#	-
#	-

class Map:
	def __init__(self, mapArray):
		## Définition de tous les attributs
		# Version de OSU
		self.osuVersion = 0
		
		# Tous les marqueurs
		self.generalMarker = 0
		self.editorMarker = 0
		self.metadataMarker = 0
		self.difficultyMarker = 0
		self.eventsMarker = 0
		self.timingPointsMarker = 0
		self.coloursMarker = 0
		self.hitObjectsMarker = 0
		
		# Général
		self.audioFilename = ''
		self.audioLeadIn = 0
		self.previewTime = 0
		self.countdown = 0
		self.sampleSet = ''
		self.stackLeniency = 0.0
		self.mode = 0
		self.letterboxInBreaks = 0
		self.widescreenStoryboard = 0
		
		# Editor
		self.bookmarks = []
		self.distanceSpacing = 0.0
		self.beatDivisor = 0
		self.gridSize = 0
		self.timelineZoom = 0.0
		
		#Metadata
		self.title = ''
		self.titleUnicode = ''
		self.artist = ''
		self.artistUnicode = ''
		self.creator = ''
		self.version = ''
		self.source = ''
		self.tags = []
		self.beatmapID = 0
		self.beatmapSetID = 0
		
		# Difficulty
		self.hpDrainRate = 0
		self.circleSize = 0
		self.overallDifficulty = 0.0
		self.approachRate = 0.0
		self.sliderMultiplier = 0.0
		self.distanceSnap = 0.0
		self.sliderTickRate = 0.0
		
		#Events (liste de lignes)
		self.backgroundAndVideoEvents = []
		self.breakPeriods = []
		self.storyboardLayer0 = []
		self.storyboardLayer1 = []
		self.storyboardLayer2 = []
		self.storyboardLayer3 = []
		self.storyboardSoundSamples = []
		self.backgroundColourTransformations = []
		
		# TimingPoints (liste de lignes)
		self.timingPoints = []
		
		# Colours (liste de lignes)
		self.colours = []
		
		# HitObjects (liste de lignes)
		self.hitObjects = []
		
		## Remplissage à partir de tableau issu de la lecture du fichier
		# Version de OSU
		line = mapArray[0]
		self.osuVersion = int(line.split('v')[1])
		
		# Marqueurs (On vérifie au passage que chacun est bien indiqué dans la map
		self.generalMarker = search('[General]\n', mapArray)
		if self.generalMarker < 0:
			raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[General]"')
		self.editorMarker = search('[Editor]\n', mapArray)
		if self.editorMarker < 0:
			raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[Editor]"')
		self.metadataMarker = search('[Metadata]\n', mapArray)
		if self.metadataMarker < 0:
			raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[Metadata]"')
		self.difficultyMarker = search('[Difficulty]\n', mapArray)
		if self.difficultyMarker < 0:
			raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[Difficulty]"')
		self.eventsMarker = search('[Events]\n', mapArray)
		if self.eventsMarker < 0:
			raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[Events]"')
		self.timingPointsMarker = search('[TimingPoints]\n', mapArray)
		if self.timingPointsMarker < 0:
			raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[TimingPoints]"')
		self.coloursMarker = search('[Colours]\n', mapArray)
		# Pas de vérification car les couleurs ne sont pas obligatoires
		self.hitObjectsMarker = search('[HitObjects]\n', mapArray)
		if self.hitObjectsMarker < 0:
			raise InvalidMapFileException('Votre map est invalide, il manque le marqueur "[HitObjects]"')
		
		# Général
		self.audioFilename = mapArray[self.generalMarker+1].split(': ')[1].replace('\n', '')
		self.audioLeadIn = int(mapArray[self.generalMarker+2].split(': ')[1])
		self.previewTime = int(mapArray[self.generalMarker+3].split(': ')[1])
		self.countdown = int(mapArray[self.generalMarker+4].split(': ')[1])
		self.sampleSet = mapArray[self.generalMarker+5].split(': ')[1].replace('\n', '')
		self.stackLeniency = float(mapArray[self.generalMarker+6].split(': ')[1])
		self.mode = int(mapArray[self.generalMarker+7].split(': ')[1])
		self.letterboxInBreaks = int(mapArray[self.generalMarker+8].split(': ')[1])
		self.widescreenStoryboard = int(mapArray[self.generalMarker+9].split(': ')[1])
		
		# Erreur si ce n'est pas une map en mode OSU "normal" on lève une erreur
		if (self.mode != 0):
			raise InvalidMapFileException('Ce programme ne prend en charge que les maps OSU normal...')
		
		# Editor
		bArray = mapArray[self.editorMarker+1].split(': ')
		b = 0
		if (bArray[0] == 'Bookmarks'):
			for el in bArray[1].split(','):
				self.bookmarks.append(int(el))
			b = 1;
		
		self.distanceSpacing = float(mapArray[self.editorMarker+1+b].split(': ')[1])
		self.beatDivisor = int(mapArray[self.editorMarker+2+b].split(': ')[1])
		self.gridSize = int(mapArray[self.editorMarker+3+b].split(': ')[1])
		self.timelineZoom = float(mapArray[self.editorMarker+4+b].split(': ')[1])
	
		#Metadata
		self.title = mapArray[self.metadataMarker+1].split(':')[1].replace('\n', '')
		self.titleUnicode = mapArray[self.metadataMarker+2].split(':')[1].replace('\n', '')
		self.artist = mapArray[self.metadataMarker+3].split(':')[1].replace('\n', '')
		self.artistUnicode = mapArray[self.metadataMarker+4].split(':')[1].replace('\n', '')
		self.creator = mapArray[self.metadataMarker+5].split(':')[1].replace('\n', '')
		self.version = mapArray[self.metadataMarker+6].split(':')[1].replace('\n', '')
		self.source = mapArray[self.metadataMarker+7].split(':')[1].replace('\n', '')
		self.tags = mapArray[self.metadataMarker+8].split(':')[1].replace('\n', '').split(' ')
		self.beatmapID = int(mapArray[self.metadataMarker+9].split(':')[1])
		self.beatmapSetID = int(mapArray[self.metadataMarker+10].split(':')[1])
		
		# Difficulty
		self.hpDrainRate = float(mapArray[self.difficultyMarker+1].split(':')[1])
		self.circleSize = float(mapArray[self.difficultyMarker+2].split(':')[1])
		self.overallDifficulty = float(mapArray[self.difficultyMarker+3].split(':')[1])
		self.approachRate = float(mapArray[self.difficultyMarker+4].split(':')[1])
		self.sliderMultiplier = float(mapArray[self.difficultyMarker+5].split(':')[1])
		self.distanceSnap = self.sliderMultiplier * 100
		self.sliderTickRate = float(mapArray[self.difficultyMarker+6].split(':')[1])
		
		#Events (liste de lignes)
		self.backgroundAndVideoEvents = []
		self.breakPeriods = []
		self.storyboardLayer0 = []
		self.storyboardLayer1 = []
		self.storyboardLayer2 = []
		self.storyboardLayer3 = []
		self.storyboardSoundSamples = []
		self.backgroundColourTransformations = []
		
		# TimingPoints (liste de lignes)
		# On récupère l'index de la dernière ligne délimitant [TimingPoints]
		timingPointsEndMarker = -1
		for i in range(self.timingPointsMarker, len(mapArray)):
			if (mapArray[i] == '\n'):
				timingPointsEndMarker = i
			if timingPointsEndMarker > 0 : break
		if timingPointsEndMarker < 0:
			raise InvalidMapFileException('Un problème à eu lieu lors de la récupération de la section [TimingPoints]')
		# On place toutes ligne correspondante dans notre attribut timingPoints
		for i in range(self.timingPointsMarker+1, timingPointsEndMarker):
			self.timingPoints.append(mapArray[i].replace('\n', ''))
				
		# Colours (liste de lignes)
		# On récupère l'index de la dernière ligne délimitant [Colours] (que si il y'a un marqueur couleur)
		if (self.coloursMarker > 0):
			coloursEndMarker = -1
			for i in range(self.coloursMarker, len(mapArray)):
				if (mapArray[i] == '\n'):
					coloursEndMarker = i
				if coloursEndMarker > 0 : break
			if coloursEndMarker < 0:
				raise InvalidMapFileException('Un problème à eu lieu lors de la récupération de la section [Colours]')
			# On place toutes ligne correspondante dans notre attribut timingPoints
			for i in range(self.coloursMarker+1, coloursEndMarker):
				self.colours.append(mapArray[i].replace('\n', ''))
		
		# HitObjects (liste de lignes)
		# On récupère l'index de la dernière ligne délimitant [HitObjects]
		hitObjectsEndMarker = -1
		for i in range(self.hitObjectsMarker, len(mapArray)):
			if (mapArray[i] == '\n'):
				hitObjectsEndMarker = i
			# Il est possible que la section aille jusqu'à la fin du fichier on ajoute donc une exception et on ajoute 1 à i
			elif (i == len(mapArray)-1):
				hitObjectsEndMarker = i + 1
			if hitObjectsEndMarker > 0 : break
		if hitObjectsEndMarker < 0:
			raise InvalidMapFileException('Un problème à eu lieu lors de la récupération de la section [HitObjects]')
		# On place toutes ligne correspondante dans notre attribut timingPoints
		for i in range(self.hitObjectsMarker+1, hitObjectsEndMarker):
			self.hitObjects.append(mapArray[i].replace('\n', ''))
			
	# print des sections
	def printGeneral(self):
		print('AudioFilename :', self.audioFilename)
		print('AudioLeadIn :', self.audioLeadIn)
		print('PreviewTime :', self.previewTime)
		print('Countdown :', self.countdown)
		print('SampleSet :', self.sampleSet)
		print('StackLeniency :', self.stackLeniency)
		print('Mode :', self.mode)
		print('LetterboxInBreaks', self.letterboxInBreaks)
		print('WidescreenStoryboard :', self.widescreenStoryboard)
		
	def printEditor(self):
		if (len(self.bookmarks) > 0):
			print('Bookmarks :', self.bookmarks)
		print('DistanceSpacing :', self.distanceSpacing)
		print('BeatDivisor :', self.beatDivisor)
		print('GridSize :', self.gridSize)
		print('TimelineZone :', self.timelineZoom)
	
	def printMetadata(self):
		print('Title :', self.title)
		print('TitleUnicode :', self.titleUnicode)
		print('Artist :', self.artist)
		print('ArtistUnicode :', self.artistUnicode)
		print('Creator :', self.creator)
		print('Version :', self.version)
		print('Source :', self.source)
		print('tags :', self.tags)
		print('BeatmapID :', self.beatmapID)
		print('BeatmapSetID :', self.beatmapSetID)
		
	def printDifficulty(self):
		print('HPDrainRate :', self.hpDrainRate)
		print('CircleSize :', self.circleSize)
		print('OverallDifficulty :', self.overallDifficulty)
		print('ApproachRate :', self.approachRate)
		print('SliderMultiplier :', self.sliderMultiplier)
		print('*DistanceSnap :', self.distanceSnap)
		print('SliderTickRate :', self.sliderTickRate)
			
	# Exploitations des données
			
	def extractTimingPoints(self):
		timingPoints = []
		for i, el in enumerate(self.timingPoints):
			timingPoint = TimingPoint(el)
			timingPoints.append(timingPoint)
		
		return timingPoints
			
	def extractHitObjects(self):
		hitObjects = []
		for i, el in enumerate(self.hitObjects):
			object = self.guessHitObject(el)
			hitObjects.append(object)
			
		return hitObjects
			
		
	def guessHitObject(self, hitObject):
		array = hitObject.split(',')
		typeHitObject = int(array[3])
		if (typeHitObject == 12 or typeHitObject == 16):
			return Spinner(hitObject)
		elif (typeHitObject == 1 or typeHitObject == 5):
			return HitCircle(hitObject)
		else:
			return Slider(hitObject)
	
class TimingPoint:
	def __init__(self, data):
		# Définition
		self.offset = 0
		self.millisecondsPerBeat = 0.0
		self.bpm = 0.0
		self.multiplier = 0.0
		self.meter = 0
		self.sampleType = 0
		self.sampleSet = 0
		self.volume = 0
		self.inherited = 0
		self.kiaiMode = 0
		
		# Hydratation
		array = data.split(',')
		self.offset = int(array[0])
		self.millisecondsPerBeat = float(array[1])
		if (self.millisecondsPerBeat < 0):
			self.multiplier = self.millisecondsPerBeat / -100
		else:
			self.bpm = 60000/self.millisecondsPerBeat
		self.meter = int(array[2])
		self.sampleType = int(array[3])
		self.sampleSet = int(array[4])
		self.volume = int(array[5])
		self.inherited = int(array[6])
		self.kiaiMode = int(array[7])
		
class Slider:
	def __init__(self, data):
		# Définition
		self.x = 0
		self.y = 0
		self.time = 0
		self.type = 0
		self.hitSound = 0
		self.sliderType = ''
		self.curves = ''
		self.repeat = 0
		self.pixelLength = 0.0
		self.edgeHitsound = ''
		self.edgeAddition = ''
		self.addition = ''
		
		# Hydratation
		array = data.split(',')
		self.x = int(array[0])
		self.y = int(array[1])
		self.time = int(array[2])
		self.type = int(array[3])
		self.hitSound = int(array[4])
		self.sliderType = array[5].split('|')[0]
		self.curves = array[5].replace(self.sliderType+'|', '')
		self.repeat = int(array[6])
		self.pixelLength = float(array[7])
		if (len(array) > 8):
			self.edgeHitsound = array[8]
			if (len(array) > 9):
				self.edgeAddition = array[9]
				if (len(array) > 10):
					self.addition = array[10]
					
	def __str__(self):
		return str(self.x) + ' ' + str(self.y) + ' ' + str(self.time) + ' ' + str(self.type) + ' ' + str(self.hitSound) + ' ' + str(self.sliderType) + ' ' + str(self.curves) + ' ' + str(self.repeat) + ' ' + str(self.pixelLength) + ' ' + str(self.edgeHitsound) + ' ' + str(self.edgeAddition) + ' ' + str(self.addition)

		

class HitCircle:
	def __init__(self, data):
		# Définition
		self.x = 0
		self.y = 0
		self.time = 0
		self.type = 0
		self.hitSound = 0
		self.addition = ''
		
		# Hydratation
		array = data.split(',')
		self.x = int(array[0])
		self.y = int(array[1])
		self.time = int(array[2])
		self.type = int(array[3])
		self.hitSound = int(array[4])
		if (len(array) > 5):
			self.addition = array[5]
	
	def __str__(self):
		return str(self.x) + ' ' + str(self.y) + ' ' + str(self.time) + ' ' + str(self.type) + ' ' + str(self.hitSound) + ' ' + str(self.addition)
		
		
class Spinner:
	def __init__(self, data):
		# Définition
		self.x = 0
		self.y = 0
		self.time = 0
		self.type = 0
		self.hitSound = 0
		self.endTime = 0
		self.addition = ''
		
		# Hydratation
		array = data.split(',')
		self.x = int(array[0])
		self.y = int(array[1])
		self.time = int(array[2])
		self.type = int(array[3])
		self.hitSound = int(array[4])
		self.endTime = int(array[5])
		if (len(array) > 6):
			self.addition = array[6]
	
	def __str__(self):
		return str(self.x) + ' ' + str(self.y) + ' ' + str(self.time) + ' ' + str(self.type) + ' ' + str(self.hitSound) + ' ' + str(self.endTime) + ' ' + str(self.addition)
				
				
class InvalidMapFileException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		