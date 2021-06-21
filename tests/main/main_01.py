from fcpxml import *
import xml.etree.ElementTree as ET
from xml.dom import minidom

# input data to build sequence from 1 clip

# sequence parameters
timebase = 25
seq_w = 750
seq_h = 576
seq_audio_bit_depth = 16
seq_audio_sample_rate = 48000
seq_dur = 534
seq_name = 'Chayki'
seq_id = 'sequence-1'

# file parameters
file_path = 'file://localhost/Volumes/work_01/PROJECTS/Poem%2045176/Videos/VHS/Chayki.mp4'
file_dur = 534
file_w = 750
file_h = 576
file_id = 'chaiki_file'
file_name = 'Chayki.mp4'

# video clip parameters
clip_start = 0
clip_end = 534
clip_dur = 534
clip_in = 0
clip_out = 534
video_clipitem_id = 'v_clipitem_chaiki'
clipitem_name = 'Chayki.mp4'

# audio media
file_bit_depth = 16
file_audio_sample_rate = 48000
audio_clipitem_L_id = 'a_clipitem_chaiki_L'
audio_clipitem_R_id = 'a_clipitem_chaiki_R'

root = ET.Element('xmeml')

# sequence.rate
rate_ = Rate(timebase=timebase, ntsc='FALSE')

# sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec
qt_codec_ = QTCodec()

# sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data
data_ = Data(qt_codec_)

# sequence.media.video.format.samplecharacteristics.codec.appspecificdata
app_specific_data_ = AppSpecificData(data=data_)

# sequence.media.video.format.samplecharacteristics.codec
codec_ = Codec(appspecificdata=app_specific_data_)

# sequence.media.video.format.samplecharacteristics
sample_characteristics_ = SampleCharacteristics(rate=rate_, codec=codec_, width=seq_w, height=seq_h, anamorphic='FALSE',
                                                pixelaspectratio='square', fielddominance='none', colordepth=24)

# sequence.media.video.format
media_video_format = Format(sample_characteristics_)

# sequence.media.video.track.clipitem.file.media.video.samplecharacteristics
sample_characteristics_ = SampleCharacteristics(rate=rate_, width=file_w, height=file_h, anamorphic='FALSE',
                                                pixelaspectratio='square', fielddominance='none')

# sequence.media.video.track.clipitem.file.media.video
video_ = Video(samplecharacteristics=sample_characteristics_)

# sequence.media.video.track.clipitem.file.media.audio.samplecharacteristics
sample_characteristics_ = SampleCharacteristics(depth=seq_audio_bit_depth, samplerate=seq_audio_sample_rate)

# sequence.media.video.track.clipitem.file.media.audio
audio_ = Audio(samplecharacteristics=sample_characteristics_, channelcount=2)

# sequence.media.video.track.clipitem.file.media
media_ = Media(video=video_, audio=audio_)

# sequence.media.video.track.clipitem.file
kv = [['id', file_id]]
file_ = File(keysnvalues=kv, name=file_name,
         pathurl=file_path,
         rate=rate_, duration=file_dur, media=media_)

link1 = Link(linkclipref=video_clipitem_id, mediatype='video', trackindex=1, clipindex=1)
link2 = Link(linkclipref=audio_clipitem_L_id, mediatype='audio', trackindex=1, clipindex=1, groupindex=1)
link3 = Link(linkclipref=audio_clipitem_R_id, mediatype='audio', trackindex=2, clipindex=1, groupindex=1)

# sequence.media.video.track.clipitem
kv = [['id', video_clipitem_id]]
clip_item_1 = ClipItem(keysnvalues=kv, name=clipitem_name, enabled='TRUE', duration=clip_dur, rate=rate_,
                       start=clip_start, end=clip_end, in_=clip_in, out=clip_out, pixelaspectratio='square',
                       anamorphic='FALSE', file=file_, link1=link1, link2=link2, link3=link3)

# sequence.media.video.track
clipitems_ = {video_clipitem_id: clip_item_1}
media_video_track = Track(clipitems=clipitems_, enabled='TRUE', locked='FALSE')

# sequence.media.video
media_video = Video(format=media_video_format, track=media_video_track)

# sequence.media.audio.format.samplecharacteristics
samplecharacteristics_ = SampleCharacteristics(depth=file_bit_depth, samplerate=file_audio_sample_rate)

# sequence.media.audio.format
format_ = Format(samplecharacteristics=samplecharacteristics_)

# sequence.media.audio.outputs.group
channel1 = Channel(index=1)
channel2 = Channel(index=2)
group1 = Group(index=1, numchannels=1, downmix=0, channel=channel1)
group2 = Group(index=2, numchannels=1, downmix=0, channel=channel2)

# sequence.media.audio.outputs
outputs_ = Outputs(group1=group1, group2=group2)

# sequence.media.audio.track.clipitem.file
kv = [['id', file_id]]
file_ = File(keysnvalues=kv)

# sequence.media.audio.track.clipitem.sourcetrack
sourcetrack_ = SourceTrack(mediatype='audio', trackindex=1)

# sequence.media.audio.track.clipitem
kv = [['id', audio_clipitem_L_id], ['premiereChannelType', 'stereo']]
clip_item_2 = ClipItem(keysnvalues=kv,  name=clipitem_name, enabled='TRUE', duration=clip_dur, rate=rate_,
                     start=clip_start, end=clip_end, in_=clip_in, out=clip_out, file=file_, sourcetrack=sourcetrack_,
                     link1=link1, link2=link2, link3=link3)


# sequence.media.audio.track
clipitems_ = {audio_clipitem_L_id: clip_item_2}
kv = [['PannerCurrentValue', '0.5'], ['PannerIsInverted','true'], ['PannerName', 'Balance'],
['currentExplodedTrackIndex', '0'], ['totalExplodedTrackCount', '2'], ['premiereTrackType', 'Stereo']]
audio_track_1 = Track(keysnvalues=kv, clipitems=clipitems_, enabled='TRUE', locked='FALSE', outputchannelindex=1)


# sequence.media.audio.track.clipitem.file
kv = [['id', file_id]]
file_ = File(keysnvalues=kv)

# sequence.media.audio.track.clipitem.sourcetrack
sourcetrack_ = SourceTrack(mediatype='audio', trackindex=2)

# sequence.media.audio.track.clipitem
kv = [['id', audio_clipitem_R_id], ['premiereChannelType', 'stereo']]
clipitem_3 = ClipItem(keysnvalues=kv,  name=clipitem_name, enabled='TRUE', duration=clip_dur, rate=rate_,
                     start=clip_start, end=clip_end, in_=clip_in, out=clip_out, file=file_, sourcetrack=sourcetrack_,
                     link1=link1, link2=link2, link3=link3)

# sequence.media.audio.track
clipitems_ = {audio_clipitem_R_id: clipitem_3}
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
sequence_ = Sequence(keysnvalues=kv, duration=seq_dur, rate=rate_, name=seq_name, media=media_, timecode=timecode_)

sequence_node = sequence_.make_node()
root.append(sequence_node)

kv = [['version', '4']]
xmeml_ = XMEML(keysnvalues=kv, sequence=sequence_)
xmeml_node = xmeml_.make_node()
line = minidom.parseString(ET.tostring(xmeml_node)).toprettyxml(indent = "   ")
print(line)

text_file = open("output_main_01.xml", "w")
text_file.write(line)
text_file.close()

















