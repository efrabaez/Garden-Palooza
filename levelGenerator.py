import random
from copy import deepcopy
from collections import deque

class LevelGenerator(): 
    def __init__(self):
        self.manhattanDistance = lambda pointA, pointB: abs((pointA[0] - pointB[0])) + abs((pointA[1] - pointB[1]))
        self.between = lambda point, matrix: 0 <= point[0] < len(matrix) and 0 <= point[1] < len(matrix[0])

    def GenerateMatrix(self):
        rows = 40
        cols = 80
        matrix = [[3 for x in range(cols)] for y in range(rows)]
        
        start = [rows - 1,random.randint(0,cols -1)]
        end = [0,random.randint(0,cols - 1)]
        self.GenerateLevel(matrix,deepcopy(start), deepcopy(end))
        return matrix

    def GenerateLevel(self,matrix,wanderer,seeker):
        createdPath = []

        while seeker not in createdPath:
            
            matrix[ wanderer[0] ][ wanderer[1] ] = 11;
            matrix[ seeker[0] ][ seeker[1] ] = 11;

            createdPath.append( wanderer )
            createdPath.append( seeker )

            wanderer = self.getWandererNextMove(matrix,createdPath, wanderer)
            seeker = self.getSeekerNextMove(matrix, createdPath, wanderer,seeker)

    def getMoveDirections(self,point):
        up = [point[0] - 1, point[1]]
        down = [point[0] + 1, point[1]]
        left = [point[0], point[1] - 1]
        right = [point[0], point[1] + 1]
        return [up,down,left,right]

    def getSeekerNextMove(self,matrix, createdPath, wanderer, seeker):
        
        moves = self.getMoveDirections(seeker)

        originalDistance = self.manhattanDistance(wanderer,seeker)
        upDistance = self.manhattanDistance(wanderer,moves[0])
        downDistance = self.manhattanDistance(wanderer,moves[1])
        leftDistance = self.manhattanDistance(wanderer,moves[2])
        rightDistance = self.manhattanDistance(wanderer,moves[3])

        distances = [originalDistance,upDistance,downDistance,leftDistance,rightDistance]
        
        return self.createSeekerNextMove(distances,moves,matrix,createdPath)
        
    def createSeekerNextMove(self,distances,moves,matrix,createdPath):
        validMoves = []
        for i in range(4):
            if  self.between(moves[i],matrix) and moves[i] not in createdPath and distances[0] > distances[i + 1]:
                validMoves.append(moves[i])
        
        if len(validMoves) > 0:
            return validMoves[random.randint(0,len(validMoves) - 1)]

        return [random.randint(0,len(matrix) - 1),random.randint(0,len(matrix[0]) - 1)]

    def getWandererNextMove(self,matrix,createdPath,wanderer):
        moves = self.getMoveDirections(wanderer)
        validMoves = []
        for move in moves:
            if self.between(move,matrix):
                validMoves.append(move)
        
        if len(validMoves) > 0:

            return validMoves[random.randint(0,len(validMoves) - 1)]

        return self.checkWandererPossibleMoves(matrix,wanderer,createdPath)

    def checkWandererPossibleMoves(self,matrix,wanderer,createdPath):
        pathExploration = deque()
        walkablePath = []

        while len(pathExploration) > 0:
            point = pathExploration.pop()
            self.checkWandererPathOptions(walkablePath, pathExploration,matrix, point)

        return walkablePath[random.randint(0,len(walkablePath) - 1)]

    def checkWandererPathOptions(self,walkablePath, pathExploration,matrix,point):
        moves = self.getMoveDirections(point)
        for move in moves:
            if self.between(move,matrix) and matrix[move[0]][move[1]] == 0:
                pathExploration.append(move)
                walkablePath.append(move)