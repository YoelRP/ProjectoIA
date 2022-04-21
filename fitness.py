def fitness(individual, dictionaryGraph):
    result = 0
    for i in range(len(individual) - 1):
        key = str(individual[i]) + ", " + str([individual[i + 1]])
        if key in dictionaryGraph:
            return -100000
        result = result - dictionaryGraph[key]
    return result
