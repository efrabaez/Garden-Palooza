from levelGenerator import LevelGenerator
import numpy

matrix = LevelGenerator().GenerateMatrix()

with open("./src/JS/matrixInfo.js", 'w') as F:
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

