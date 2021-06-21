from fcpxml import AppSpecificData, QTCodec, Data, Codec, SampleCharacteristics, Rate, Format, Video, Audio
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('super')
sc = SampleCharacteristics(depth=16, samplerate=48000)
a = Audio(samplecharacteristics=sc)
a_node = a.make_node()

root.append(a_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()

