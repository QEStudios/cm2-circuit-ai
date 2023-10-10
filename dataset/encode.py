import cm2py as cm2

inputFilename = "raw_dataset.txt"
outputFilename = "encoded_dataset.txt"

input = open(inputFilename, "r")
output = open(outputFilename, "w")

def encode(saveString):
    encoded = ""

    blockNames = [NOR, AND, OR, XOR, BUTTON, FLIPFLOP, LED, SOUND, CONDUCTOR, CUSTOM, NAND, XNOR, RANDOM, TEXT, TILE]

    save = cm2.importSave(saveString)

    for block in save.blocks.values():
        encoded += blockNames[block.blockId] + " "

        if block.uuid in save.connections:
            for connection in save.connections[block.uuid]:
                # TODO
                pass

for line in input:
    output.write(encode(line))