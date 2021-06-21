from fcpxml import SampleCharacteristics, Rate, Video, Audio, Media, File, ClipItem, Link
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

link1 = Link(linkclipref='clipitem-1', mediatype='video', trackindex=1, clipindex=1)
link2 = Link(linkclipref='clipitem-2', mediatype='audio', trackindex=1, clipindex=1, groupindex=1)
link3 = Link(linkclipref='clipitem-3', mediatype='audio', trackindex=2, clipindex=1, groupindex=1)

kv = [['id', 'clipitem-1']]
clpitm = ClipItem(keysnvalues=kv, name='Chayki.mp4', enabled='TRUE', duration=534, rate=r_vd,
                  start=0, end=534, in_=0, out=534, pixelaspectratio='square', anamorphic='FALSE', file=f,
                  link1=link1, link2=link2, link3=link3)
clpitm_node = clpitm.make_node()

root.append(clpitm_node)
line = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()








