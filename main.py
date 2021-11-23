import random
mutationChance = 100
lifeTimeMax = 100
breedablityMax = 1


def createCell(parentCell1, parentCell2):
    isMutiant = random.randint(0,mutationChance)
    location = parentCell1.location
    lifeTime = 100
    breedablity = parentCell1,parentCell2


def createVirus(parentVirus1, parentVirus2):
    isMutiant = random.randint(0,mutationChance)
    location = parentCell1.location
    lifeTime = 50
    breedablity = cellCombiner(parentVirus1,parentVirus2)

def createFood():
    x = random.randint (0,50)
    y = random.randint (0,50)


