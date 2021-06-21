from fcpxml import QTCodec
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('super')

qtc = QTCodec()
qtc_node = qtc.make_node()
root.append(qtc_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()







