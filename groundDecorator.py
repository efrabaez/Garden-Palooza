import random

class GroundDecorator:
    def __init__(self,matrix,GROUND_SPRITE_MAP):
        for row in range(len(matrix)):
            for column in range(len(matrix)):
                if matrix[row][column] == GROUND_SPRITE_MAP[0]:
                    if random.randint(0,100) <= 40:
                        matrix[row][column] = GROUND_SPRITE_MAP[ random.randint(0,len(GROUND_SPRITE_MAP) - 1)]