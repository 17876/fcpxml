from fcpxml import *
import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('xmeml')

# sequence.rate
rate_ = Rate(timebase=25, ntsc='FALSE')

# sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec
qt_codec_ = QTCodec()

# sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data
data_ = Data(qt_codec_)

# sequence.media.video.format.samplecharacteristics.codec.appspecificdata
app_specific_data_ = AppSpecificData(data=data_)

# sequence.media.video.format.samplecharacteristics.codec
codec_ = Codec(appspecificdata=app_specific_data_)

# sequence.media.video.format.samplecharacteristics
sample_characteristics_ = SampleCharacteristics(rate=rate_, codec=codec_, width=1920, height=1080)

# sequence.media.video.format
media_video_format = Format(sample_characteristics_)

# sequence.media.video.track.clipitem.file.media.video.samplecharacteristics
sample_characteristics_ = SampleCharacteristics(rate=rate_, width=1920, height=1080, anamorphic='FALSE', pixelaspectratio='square',
                           fielddominance='none')

# sequence.media.video.track.clipitem.file.media.video
video_ = Video(samplecharacteristics=sample_characteristics_)

# sequence.media.video.track.clipitem.file.media.audio.samplecharacteristics
sample_characteristics_ = SampleCharacteristics(depth=16, samplerate=48000)

# sequence.media.video.track.clipitem.file.media.audio
audio_ = Audio(samplecharacteristics=sample_characteristics_)

# sequence.media.video.track.clipitem.file.media
media_ = Media(video=video_, audio=audio_)

# sequence.media.video.track.clipitem.file
kv = [['id', 'file-1']]
file_ = File(keysnvalues=kv, name='Chayki.mp4',
         pathurl='file://localhost/Volumes/work_01/PROJECTS/Poem%2045176/Videos/VHS/Chayki.mp4',
         rate=rate_, duration=534, media=media_)

link1 = Link(linkclipref='clipitem-1', mediatype='video', trackindex=1, clipindex=1)
link2 = Link(linkclipref='clipitem-2', mediatype='audio', trackindex=1, clipindex=1, groupindex=1)
link3 = Link(linkclipref='clipitem-3', mediatype='audio', trackindex=2, clipindex=1, groupindex=1)

# sequence.media.video.track.clipitem
kv = [['id', 'clipitem-1']]
clip_item_1 = ClipItem(keysnvalues=kv, name='Chayki.mp4', enabled='TRUE', duration=534, rate=rate_,
                  start=0, end=534, in_=0, out=534, pixelaspectratio='square', anamorphic='FALSE', file=file_,
                  link1=link1, link2=link2, link3=link3)

# sequence.media.video.track
clipitems_ = {'clipitem-1': clip_item_1}
media_video_track = Track(clipitems=clipitems_, enabled='TRUE', locked='FALSE')

# sequence.media.video
media_video = Video(format=media_video_format, track=media_video_track)

# sequence.media.audio.format.samplecharacteristics
samplecharacteristics_ = SampleCharacteristics(depth=16, samplerate=48000)

# sequence.media.audio.format
format_ = Format(samplecharacteristics=samplecharacteristics_)

# sequence.media.audio.outputs.group
channel1 = Channel(index=1)
channel2 = Channel(index=3)
group1 = Group(index=1, numchannels=1, downmix=0, channel=channel1)
group2 = Group(index=1, numchannels=1, downmix=0, channel=channel2)

# sequence.media.audio.outputs
outputs_ = Outputs(group1=group1, group2=group2)

# sequence.media.audio.track.clipitem.file
kv = [['id', 'file-1']]
file_ = File(keysnvalues=kv)

# sequence.media.audio.track.clipitem.sourcetrack
sourcetrack_ = SourceTrack(mediatype='audio', trackindex=1)

# sequence.media.audio.track.clipitem
kv = [['id', 'clipitem-2'], ['premiereChannelType', 'stereo']]
clip_item_2 = ClipItem(keysnvalues=kv,  name='Chayki.mp4', enabled='TRUE', duration=534, rate=rate_,
                     start=0, end=534, in_=0, out=534, file=file_, sourcetrack=sourcetrack_,
                     link1=link1, link2=link2, link3=link3)


# sequence.media.audio.track
clipitems_ = {'clipitem-2': clip_item_2}
kv = [['PannerCurrentValue', '0.5'], ['PannerIsInverted','true'], ['PannerName', 'Balance'],
['currentExplodedTrackIndex', '0'], ['totalExplodedTrackCount', '2'], ['premiereTrackType', 'Stereo']]
audio_track_1 = Track(keysnvalues=kv, clipitems=clipitems_, enabled='TRUE', locked='FALSE', outputchannelindex=1)


# sequence.media.audio.track.clipitem.file
kv = [['id', 'file-1']]
file_ = File(keysnvalues=kv)

# sequence.media.audio.track.clipitem.sourcetrack
sourcetrack_ = SourceTrack(mediatype='audio', trackindex=2)

# sequence.media.audio.track.clipitem
kv = [['id', 'clipitem-3'], ['premiereChannelType', 'stereo']]
clipitem_3 = ClipItem(keysnvalues=kv,  name='Chayki.mp4', enabled='TRUE', duration=534, rate=rate_,
                     start=0, end=534, in_=0, out=534, file=file_, sourcetrack=sourcetrack_,
                     link1=link1, link2=link2, link3=link3)

# sequence.media.audio.track
clipitems_ = {'clipitem-3': clipitem_3}
kv = [['PannerCurrentValue', '0.5'], ['PannerIsInverted','true'], ['PannerName', 'Balance'],
['currentExplodedTrackIndex', '1'], ['totalExplodedTrackCount', '2'], ['premiereTrackType', 'Stereo']]
audio_track_2 = Track(keysnvalues=kv, clipitems=clipitems_, enabled='TRUE', locked='FALSE', outputchannelindex=2)

# sequence.media.audio
media_audio = Audio(samplecharacteristics=None, channelcount=None, numOutputChannels=2, format=format_,
                 outputs=outputs_, track1=audio_track_1, track2=audio_track_2)

media_ = Media(video=media_video, audio=media_audio)

# sequence.timecode
timecode_ = Timecode(rate=rate_, string='00:00:00:00', frame=0, displayformat='NDF')

# sequence
kv = [['id', 'sequence-1']]
sequence_ = Sequence(keysnvalues=kv, duration=534, rate=rate_, name='Chayki', media=media_, timecode=timecode_)

sequence_node = sequence_.make_node()
root.append(sequence_node)

kv = [['version', '4']]
xmeml_ = XMEML(keysnvalues=kv, sequence=sequence_)
xmeml_node = xmeml_.make_node()
line = minidom.parseString(ET.tostring(xmeml_node)).toprettyxml(indent = "   ")
print(line)

text_file = open("output.xml", "w")
text_file.write(line)
text_file.close()








