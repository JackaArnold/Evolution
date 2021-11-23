import random
mutationChance = 100
lifeTimeMax = 100
breedablityMax = 1

def cellCombiner(x, y):
    isMutiant = random.randint(0,mutationChance)
    if isMutiant = 1:
        lifeTime = random.randint(0,lifeTimeMax*1.1)
        if lifeTime > lifeTimeMax:
            lifeTimeMax = lifeTime

def createCell(parentCell1, parentCell2):
    location = parentCell1.location
    lifeTime = 100
    breedablity = cellCombiner(parentCell1,parentCell2,)


