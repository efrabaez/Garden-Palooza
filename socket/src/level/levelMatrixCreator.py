from src.level.skeletonGenerator import SkeletonGenerator
from src.level.grassDecorator import GrassDecorator
from src.level.riverSkeletonGenerator import RiverSkeletonGenerator
from src.level.riverDecorator import RiverDecorator
from src.level.groundDecorator import GroundDecorator
from src.level.waterExtraDecorator import WaterExtraDecorator

def GenerateLevelMatrix():
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

    skeleton = SkeletonGenerator(GROUND_SPRITE_INDEX, GRASS_SPRITE_INDEX)
    matrix = skeleton.matrix
    matrix = GrassDecorator().updateCells(matrix,GRASS_SPRITE_MAP,skeleton.createdPath,skeleton.ground, GRASS_SPRITE_INDEX, GROUND_SPRITE_INDEX)
    skeleton = RiverSkeletonGenerator(matrix,WATER_SPRITE_INDEX, GROUND_SPRITE_INDEX)

    if len( skeleton.waterSpot ) > 0:
        matrix = RiverDecorator().updateCells(matrix,WATER_SPRITE_INDEX,skeleton.waterSpot, GROUND_SPRITE_INDEX, WATER_SPRITE_MAP)
        WaterExtraDecorator(matrix, skeleton.waterSpot, WATER_EXTRA_SPRITE_MAP)
    GroundDecorator(matrix,GROUND_SPRITE_MAP)

    return matrix