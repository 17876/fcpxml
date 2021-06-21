from fcpxml import AppSpecificData, QTCodec, Data, Codec
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('super')

qtc = QTCodec()
dt = Data(qtc)
asd = AppSpecificData(data=dt)
cdc = Codec(appspecificdata=asd)
cdc_node = cdc.make_node()

root.append(cdc_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()








