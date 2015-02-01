zipcodes = [11105,11102,11103,11104,11377,11373,11372,11368]

def get_neighbors(zip, zipcodes):
    x = zipcodes.index(zip)
    neighbors = zipcodes[x-1:x+2]
    return neighbors
