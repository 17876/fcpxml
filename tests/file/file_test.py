from fcpxml import SampleCharacteristics, Rate, Video, Audio, Media, File
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('super')
r_vd = Rate(timebase=33, ntsc='FALSE')
scvd = SampleCharacteristics(rate=r_vd, width=1920, height=1080, anamorphic='FALSE', pixelaspectratio='square',
                           fielddominance='none')
vd = Video(samplecharacteristics=scvd)


sca = SampleCharacteristics(depth=16, samplerate=48000)
a = Audio(samplecharacteristics=sca)

m = Media(video=vd, audio=a)

r_f = Rate(timebase=25, ntsc='FALSE')
kv = [['id', 'file-1']]
f = File(keysnvalues=kv, name='Chayki.mp4',
         pathurl='file://localhost/Volumes/work_01/PROJECTS/Poem%2045176/Videos/VHS/Chayki.mp4',
         rate=r_f, duration=534, media=m)
f_node = f.make_node()

root.append(f_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()








