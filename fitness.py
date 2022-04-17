def fitness(individual, dictionaryGraph):
    for i in range(len(individual) - 1):
        key = str(individual[i]) + ", " + str([individual[i + 1]])
        if key in dictionaryGraph:
            if dictionaryGraph[key] == 0:
                return -100000
        result = result - dictionaryGraph[key]
    return result
