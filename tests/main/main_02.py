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

# file 1 parameters
file_path_1 = 'file://localhost/Volumes/work_01/PROJECTS/Poem%2045176/Videos/VHS/Chayki.mp4'
file_dur_1 = 534
file_w_1 = 750
file_h_1 = 576
file_id_1 = 'chaiki_file'
file_name_1 = 'Chayki.mp4'

# file 2 parameters
file_path_2 = 'file://localhost/Volumes/work_01/PROJECTS/Poem%2045176/Videos/VHS/Alisa.mp4'
file_dur_2 = 493
file_w_2 = 750
file_h_2 = 576
file_id_2 = 'alisa_file'
file_name_2 = 'Alisa.mp4'


# video clip 1 parameters
clip_start_1 = 0
clip_end_1 = 534
clip_dur_1 = 534
clip_in_1 = 0
clip_out_1 = 534
video_clipitem_id_1 = 'v_clipitem_chaiki'
clipitem_name_1 = 'Chayki.mp4'

# video clip 2 parameters
clip_start_2 = 620
clip_end_2 = 1113
clip_dur_2 = 493
clip_in_2 = 0
clip_out_2 = 493
video_clipitem_id_2 = 'v_clipitem_alisa'
clipitem_name_2 = 'Alisa.mp4'

# audio media
file_bit_depth = 16
file_audio_sample_rate = 48000

# 1
audio_clipitem_L_id_1 = 'a_clipitem_chaiki_L'
audio_clipitem_R_id_1 = 'a_clipitem_chaiki_R'

# 2
audio_clipitem_L_id_2 = 'a_clipitem_alisa_L'
audio_clipitem_R_id_2 = 'a_clipitem_alisa_R'

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

#### VIDEO CLIPITEM 1 ####

# sequence.media.video.track.clipitem.file.media.video.samplecharacteristics
sample_characteristics_ = SampleCharacteristics(rate=rate_, width=file_w_1, height=file_h_1, anamorphic='FALSE',
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
kv = [['id', file_id_1]]
file_ = File(keysnvalues=kv, name=file_name_1, pathurl=file_path_1,
             rate=rate_, duration=file_dur_1, media=media_)

link1 = Link(linkclipref=video_clipitem_id_1, mediatype='video', trackindex=1, clipindex=1)
link2 = Link(linkclipref=audio_clipitem_L_id_1, mediatype='audio', trackindex=1, clipindex=1, groupindex=1)
link3 = Link(linkclipref=audio_clipitem_R_id_1, mediatype='audio', trackindex=2, clipindex=1, groupindex=1)

# sequence.media.video.track.clipitem
kv = [['id', video_clipitem_id_1]]
v_clip_item_1 = ClipItem(keysnvalues=kv, name=clipitem_name_1, enabled='TRUE', duration=clip_dur_1, rate=rate_,
                       start=clip_start_1, end=clip_end_1, in_=clip_in_1, out=clip_out_1, pixelaspectratio='square',
                       anamorphic='FALSE', file=file_, link1=link1, link2=link2, link3=link3)

#### VIDEO CLIPITEM 2 ####

# sequence.media.video.track.clipitem.file.media.video.samplecharacteristics
sample_characteristics_ = SampleCharacteristics(rate=rate_, width=file_w_2, height=file_h_2, anamorphic='FALSE',
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
kv = [['id', file_id_2]]
file_ = File(keysnvalues=kv, name=file_name_2, pathurl=file_path_2,
             rate=rate_, duration=file_dur_2, media=media_)

link1 = Link(linkclipref=video_clipitem_id_2, mediatype='video', trackindex=1, clipindex=2)
link2 = Link(linkclipref=audio_clipitem_L_id_2, mediatype='audio', trackindex=1, clipindex=2, groupindex=1)
link3 = Link(linkclipref=audio_clipitem_R_id_2, mediatype='audio', trackindex=2, clipindex=2, groupindex=1)


# sequence.media.video.track.clipitem
kv = [['id', video_clipitem_id_2]]
v_clip_item_2 = ClipItem(keysnvalues=kv, name=clipitem_name_2, enabled='TRUE', duration=clip_dur_2, rate=rate_,
                       start=clip_start_2, end=clip_end_2, in_=clip_in_2, out=clip_out_2, pixelaspectratio='square',
                       anamorphic='FALSE', file=file_, link1=link1, link2=link2, link3=link3)


# sequence.media.video.track
clipitems_ = {video_clipitem_id_1: v_clip_item_1, video_clipitem_id_2: v_clip_item_2}
media_video_track = Track(clipitems=clipitems_, enabled='TRUE', locked='FALSE')

# sequence.media.video
media_video = Video(format=media_video_format, track=media_video_track)


#### AUDIO ####

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


#### TRACK 1 AUDIO CLIPITEM 1 ####

link1 = Link(linkclipref=video_clipitem_id_1, mediatype='video', trackindex=1, clipindex=1)
link2 = Link(linkclipref=audio_clipitem_L_id_1, mediatype='audio', trackindex=1, clipindex=1, groupindex=1)
link3 = Link(linkclipref=audio_clipitem_R_id_1, mediatype='audio', trackindex=2, clipindex=1, groupindex=1)

# sequence.media.audio.track.clipitem.file
kv = [['id', file_id_1]]
file_ = File(keysnvalues=kv)

# sequence.media.audio.track.clipitem.sourcetrack
sourcetrack_ = SourceTrack(mediatype='audio', trackindex=1)

# sequence.media.audio.track.clipitem
kv = [['id', audio_clipitem_L_id_1], ['premiereChannelType', 'stereo']]
a_clip_item_1 = ClipItem(keysnvalues=kv,  name=clipitem_name_1, enabled='TRUE', duration=clip_dur_1, rate=rate_,
                       start=clip_start_1, end=clip_end_1, in_=clip_in_1, out=clip_out_1, file=file_,
                       sourcetrack=sourcetrack_, link1=link1, link2=link2, link3=link3)

#### TRACK 1 AUDIO CLIPITEM 2 ####

link1 = Link(linkclipref=video_clipitem_id_2, mediatype='video', trackindex=1, clipindex=2)
link2 = Link(linkclipref=audio_clipitem_L_id_2, mediatype='audio', trackindex=1, clipindex=2, groupindex=1)
link3 = Link(linkclipref=audio_clipitem_R_id_2, mediatype='audio', trackindex=2, clipindex=2, groupindex=1)

# sequence.media.audio.track.clipitem.file
kv = [['id', file_id_2]]
file_ = File(keysnvalues=kv)

# sequence.media.audio.track.clipitem.sourcetrack
sourcetrack_ = SourceTrack(mediatype='audio', trackindex=1)

# sequence.media.audio.track.clipitem
kv = [['id', audio_clipitem_L_id_2], ['premiereChannelType', 'stereo']]
a_clip_item_2 = ClipItem(keysnvalues=kv,  name=clipitem_name_2, enabled='TRUE', duration=clip_dur_2, rate=rate_,
                       start=clip_start_2, end=clip_end_2, in_=clip_in_2, out=clip_out_2, file=file_,
                       sourcetrack=sourcetrack_, link1=link1, link2=link2, link3=link3)


# sequence.media.audio.track
clipitems_ = {audio_clipitem_L_id_1: a_clip_item_1, audio_clipitem_L_id_2: a_clip_item_2}
kv = [['PannerCurrentValue', '0.5'], ['PannerIsInverted','true'], ['PannerName', 'Balance'],
['currentExplodedTrackIndex', '0'], ['totalExplodedTrackCount', '2'], ['premiereTrackType', 'Stereo']]
audio_track_1 = Track(keysnvalues=kv, clipitems=clipitems_, enabled='TRUE', locked='FALSE', outputchannelindex=1)




#### TRACK 2 AUDIO CLIPITEM 1 ####

link1 = Link(linkclipref=video_clipitem_id_1, mediatype='video', trackindex=1, clipindex=1)
link2 = Link(linkclipref=audio_clipitem_L_id_1, mediatype='audio', trackindex=1, clipindex=1, groupindex=1)
link3 = Link(linkclipref=audio_clipitem_R_id_1, mediatype='audio', trackindex=2, clipindex=1, groupindex=1)


# sequence.media.audio.track.clipitem.file
kv = [['id', file_id_1]]
file_ = File(keysnvalues=kv)

# sequence.media.audio.track.clipitem.sourcetrack
sourcetrack_ = SourceTrack(mediatype='audio', trackindex=2)

# sequence.media.audio.track.clipitem
kv = [['id', audio_clipitem_R_id_1], ['premiereChannelType', 'stereo']]
a_clipitem_1 = ClipItem(keysnvalues=kv,  name=clipitem_name_1, enabled='TRUE', duration=clip_dur_1, rate=rate_,
                     start=clip_start_1, end=clip_end_1, in_=clip_in_1, out=clip_out_1, file=file_, sourcetrack=sourcetrack_,
                     link1=link1, link2=link2, link3=link3)


#### TRACK 2 AUDIO CLIPITEM 2 ####

link1 = Link(linkclipref=video_clipitem_id_2, mediatype='video', trackindex=1, clipindex=2)
link2 = Link(linkclipref=audio_clipitem_L_id_2, mediatype='audio', trackindex=1, clipindex=2, groupindex=1)
link3 = Link(linkclipref=audio_clipitem_R_id_2, mediatype='audio', trackindex=2, clipindex=2, groupindex=1)


# sequence.media.audio.track.clipitem.file
kv = [['id', file_id_2]]
file_ = File(keysnvalues=kv)

# sequence.media.audio.track.clipitem.sourcetrack
sourcetrack_ = SourceTrack(mediatype='audio', trackindex=2)

# sequence.media.audio.track.clipitem
kv = [['id', audio_clipitem_R_id_2], ['premiereChannelType', 'stereo']]
a_clipitem_2 = ClipItem(keysnvalues=kv,  name=clipitem_name_2, enabled='TRUE', duration=clip_dur_2, rate=rate_,
                     start=clip_start_2, end=clip_end_2, in_=clip_in_2, out=clip_out_2, file=file_, sourcetrack=sourcetrack_,
                     link1=link1, link2=link2, link3=link3)


# sequence.media.audio.track
clipitems_ = {audio_clipitem_R_id_1: a_clipitem_1, audio_clipitem_R_id_2: a_clipitem_2}
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

text_file = open("output_main_02.xml", "w")
text_file.write(line)
text_file.close()

















