from skeletonGenerator import SkeletonGenerator
from grassDecorator import GrassDecorator
from riverSkeletonGenerator import RiverSkeletonGenerator
from riverDecorator import RiverDecorator
from groundDecorator import GroundDecorator
from waterExtraDecorator import WaterExtraDecorator
from grassExtraDecorator import GrassExtraDecorator
from groundExtraDecorator import GroundExtraDecorator
from copy import deepcopy

GROUND_SPRITE_INDEX = 2363
GRASS_SPRITE_INDEX = 2420
WATER_SPRITE_INDEX = 2717


#up,down,left,right,upperCornerLeft, upperCornerRight, lowerCornerRight, lowerCornerLeft
#edge cases sprites:  upperCornerLeft, upperCornerRight, lowerCornerRight, lowerCornerLeft
GRASS_SPRITE_MAP = [2361, 2479, 2419, 2421, 2480, 2478, 2362, 2360, 2422, 2423,2482,2481]

#up,down,left,right,upperCornerLeft, upperCornerRight, lowerCornerRight, lowerCornerLeft
#edge cases sprites:  upperCornerLeft, upperCornerRight, lowerCornerRight, lowerCornerLeft
WATER_SPRITE_MAP = [2715, 2833, 2773, 2775, 2834, 2832, 2716, 2714,2776,2777,2836,2835]

GROUND_SPRITE_MAP = [GROUND_SPRITE_INDEX,2483,2484,2485]

WATER_EXTRA_SPRITE_MAP = [ 2896, 2897, 2898, 2899 ]

GRASS_EXTRA_SPRITE_MAP = [ 2609, 2610, 2611]

GRASS_EXTRA_SPRITE_MAP2 = [2186,2187, 2306,2307,2308,2309,2310]

GROUND_EXTRA_SPRITE_MAP = [2491,2550]

skeleton = SkeletonGenerator(GROUND_SPRITE_INDEX, GRASS_SPRITE_INDEX)
createdPath = skeleton.createdPath
groundArea = skeleton.ground
matrix = skeleton.matrix
matrix = GrassDecorator().updateCells(matrix,GRASS_SPRITE_MAP,skeleton.createdPath,skeleton.ground, GRASS_SPRITE_INDEX, GROUND_SPRITE_INDEX)
skeleton = RiverSkeletonGenerator(matrix,WATER_SPRITE_INDEX, GROUND_SPRITE_INDEX)

if len( skeleton.waterSpot ) > 0:
    matrix = RiverDecorator().updateCells(matrix,WATER_SPRITE_INDEX,skeleton.waterSpot, GROUND_SPRITE_INDEX, WATER_SPRITE_MAP)
    WaterExtraDecorator(matrix, skeleton.waterSpot, WATER_EXTRA_SPRITE_MAP)

GroundDecorator(matrix,GROUND_SPRITE_MAP)

secondLayer = deepcopy(matrix)

GrassExtraDecorator(secondLayer,GRASS_EXTRA_SPRITE_MAP, GRASS_EXTRA_SPRITE_MAP2, createdPath, GRASS_SPRITE_INDEX)
GroundExtraDecorator(secondLayer, GROUND_EXTRA_SPRITE_MAP, groundArea, GROUND_SPRITE_MAP )

with open("../src/JS/matrixInfo.js", 'w') as F:
    F.write("let matrix = [" )

    for i in range(len(matrix)):
        line = "["  
        for j in range(len(matrix[i])):
            line += str(matrix[i][j])
            if j < len(matrix[i]) - 1:
                line += ","
        line += "]"
        if i < len(matrix) - 1:
            line += ","
        line += "\n"
        F.write(line)

    F.write("];\n export default matrix;")


with open("../src/JS/secondInfo.js", 'w') as F:
    F.write("let secondLayer = [" )

    for i in range(len(secondLayer)):
        line = "["  
        for j in range(len(secondLayer[i])):
            line += str(secondLayer[i][j])
            if j < len(secondLayer[i]) - 1:
                line += ","
        line += "]"
        if i < len(secondLayer) - 1:
            line += ","
        line += "\n"
        F.write(line)

    F.write("];\n export default secondLayer;")
