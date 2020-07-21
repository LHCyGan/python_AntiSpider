from fontTools.ttLib import TTFont

font = TTFont("783e23d8-8799-11ea-a9e8-9c305b3c8000.wwof")
uni_list = font.getGlyphNames()[1:-1]
font.saveXML("./0.xml")
print(uni_list)