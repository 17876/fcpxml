from fcpxml import AppSpecificData, QTCodec, Data, Codec, SampleCharacteristics, Rate, Format
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('super')

qtc = QTCodec()
dt = Data(qtc)
asd = AppSpecificData(data=dt)
cdc = Codec(appspecificdata=asd)
r = Rate(timebase=33, ntsc='FALSE')
sc = SampleCharacteristics(rate=r, codec=cdc, width=1920, height=1080)
frmt = Format(sc)

frmt_node = frmt.make_node()

root.append(frmt_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()








