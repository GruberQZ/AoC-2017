import os
import os.path
import re

regex = re.compile(r'(\d+):\s(\d+)')

class Firewall():
    def __init__(self):
        self.layers = {}
    def addLayer(self, number, layer):
        self.layers[number] = layer
    def advanceAllScanners(self):
        for name, layer in self.layers.items():
            layer.advanceScanner()
    def existsLayer(self, layerNumber):
        return layerNumber in self.layers
    def getLayer(self, layerNumber):
        return self.layers[layerNumber]

class Layer():
    def __init__(self, depth):
        self.depth = depth
        self.scanner = 1
        self.direction = 1
    def advanceScanner(self):
        # Flip direction if necessary
        if self.direction == 1 and self.scanner == self.depth:
            self.direction = -1
        elif self.direction == -1 and self.scanner == 1:
            self.direction = 1
        # Advance    
        self.scanner += self.direction
    def getScannerPosition(self):
        return self.scanner
    def getLength(self):
        return self.depth

firewall = Firewall()

# Get input
# Figure out what the last layer is
maxLayerNumber = 0
with open(os.path.join(os.getcwd(), 'Day13', 'input.txt'), 'r') as input:
    for line in input:
        match = regex.match(line.rstrip())
        layerNumber = int(match.group(1))
        layerLength = int(match.group(2))
        firewall.addLayer(layerNumber, Layer(layerLength))
        if layerNumber > maxLayerNumber:
            maxLayerNumber = layerNumber

# Make steps and figure out where we get caught
caughtTotal = 0
for step in range(maxLayerNumber + 1):
    # See if the scanner is in the first position
    if firewall.existsLayer(step) and \
        firewall.getLayer(step).getScannerPosition() == 1:
        caughtTotal += step * firewall.getLayer(step).getLength()
    # Advance the security scanners
    firewall.advanceAllScanners()

print(str(caughtTotal))
