from fcpxml import SampleCharacteristics, Rate, Video, Audio, Media
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('super')
r = Rate(timebase=33, ntsc='FALSE')
scvd = SampleCharacteristics(rate=r, width=1920, height=1080, anamorphic='FALSE', pixelaspectratio='square',
                           fielddominance='none')
vd = Video(samplecharacteristics=scvd)


sca = SampleCharacteristics(depth=16, samplerate=48000)
a = Audio(samplecharacteristics=sca)

m = Media(video=vd, audio=a)
m_node = m.make_node()

root.append(m_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()








