from fcpxml import Node
import xml.etree.ElementTree as ET
from xml.dom import minidom

n1 = Node('Test', codecname='Apple ProRes 422', codectypename='Apple ProRes 422XXX')
n1_node = n1.make_node()
line = minidom.parseString(ET.tostring(n1_node)).toprettyxml(indent = "   ")
print(line)

n2 = Node('Nested', codecname='Apple ProRes 422', codectypename='Apple ProRes 422XXX', object=n1)
n2_node = n2.make_node()
line = minidom.parseString(ET.tostring(n2_node)).toprettyxml(indent = "   ")
print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()







