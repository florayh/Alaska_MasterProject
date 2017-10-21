# Copy the following goes into the pre-logic block
def level1(level2):
    if level2 in ['Meadow', 'Bog', 'Mowed']:
        return 'Herbaceous'
    elif level2 in ['Willow']:
        return 'Shrub'
    elif level2 in ['Alder', 'Spruce', 'Cottonwood', 'Mixed']:
        return 'Forest'
    elif level2 in ['Water']:
        return 'Water'
    elif level2 in ['Developed']:
        return 'Developed'
    else:
        return 'Error' 
# then, in the actual code, write: level1(!LEVEL2CLASS!)
