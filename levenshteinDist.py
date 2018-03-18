
def nextState(previousState, increment, source_char, destination_char):
    modifications = previousState['modifications'] + increment
    aligned_source = previousState['source'] + source_char
    aligned_destination = previousState['destination'] + destination_char
    return {'modifications': modifications, 
        'source': aligned_source, 'destination': aligned_destination}


def removeChar(previousState, source_char):
    return nextState(previousState, 1, source_char, '_')

def addChar(previousState, destination_char):
    return nextState(previousState, 1, '_', destination_char)

def replaceChar(previousState, source_char, destination_char):
    return nextState(previousState, 
        (1 if source_char != destination_char else 0), 
        source_char, 
        destination_char)

def levenshteinDist(source, destination):
    source = ' ' + source
    destination = ' ' + destination
    dist_matrix = [ [{'modifications': 0, 
        'source': '', 
        'destination': ''} for i in range(len(source))] for j in range(len(destination))]

    for source_index in range(1, len(source)):
        dist_matrix[0][source_index] = removeChar(dist_matrix[0][source_index - 1], source[source_index])

    for destination_index in range(1, len(destination)):
        dist_matrix[destination_index][0] = addChar(dist_matrix[destination_index - 1][0], destination[destination_index])
    
    for source_index in range(1, len(source)):
        for destination_index in range(1, len(destination)):
            diagonalMovement = replaceChar(dist_matrix[destination_index-1][source_index - 1], 
                source[source_index], 
                destination[destination_index])
            leftMovement = addChar(dist_matrix[destination_index - 1][source_index], 
                destination[destination_index])
            upMovement = removeChar(dist_matrix[destination_index][source_index - 1], 
                source[source_index])
            dist_matrix[destination_index][source_index] = min([diagonalMovement, leftMovement, upMovement], 
                key = lambda p : p['modifications'])
    print(dist_matrix[len(destination) - 1][len(source) - 1])
    return dist_matrix[len(destination) - 1][len(source) - 1]