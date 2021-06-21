from fcpxml import Rate
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('super')

r = Rate(timebase=33, ntsc='TRUE')
r_node = r.make_node()


root.append(r_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()







