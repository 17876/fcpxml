from fcpxml import AppSpecificData, QTCodec, Data
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('super')

qtc = QTCodec()
dt = Data(qtc)
dt_node = dt.make_node()

asd = AppSpecificData(data=dt)
asd_node = asd.make_node()

root.append(asd_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()








