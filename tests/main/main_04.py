from fcpxml import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
import copy

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


path = 'file://localhost/Volumes/work_01/PROJECTS/Poem%2045176/Videos/VHS/'

clips = {
    'clip_1': {
        'file': {
            'name': 'Chayki.mp4',
            'dur': 534,
            'width': 750,
            'height': 576,
        },
        'clip': {
            'start': 0,
            'in': 0,
            'out': 534
        }
    },
    'clip_2': {
        'file': {
            'name': 'Alisa.mp4',
            'dur': 493,
            'width': 750,
            'height': 576,
        },
        'clip': {
            'start': 620,
            'in': 0,
            'out': 493
        }
    },
    'clip_3': {
        'file': {
            'name': 'Chayki.mp4',
            'dur': 534,
            'width': 750,
            'height': 576,
        },
        'clip': {
            'start': 2000,
            'in': 0,
            'out': 534
        }
    },
}

clips_for_func = copy.deepcopy(clips)
clipindex = 1
for cur_clip_key, cur_clip_dict in clips.items():

    clips_for_func[cur_clip_key]['clip']['index'] = clipindex

    # generation file_id
    cur_file_id = 'file_id_' + cur_clip_dict['file']['name'][:-4]
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['file']['id'] = cur_file_id

    # generation file path
    cur_file_path = path + cur_clip_dict['file']['name']
    # adding this to clips_for_func
    clips_for_func[cur_clip_key]['file']['path'] = cur_file_path

    # generation clipitem_id for video
    cur_video_clipitem_id = 'v_clipitem_id_{:s}_{:d}'.format(cur_clip_dict['file']['name'][:-4], clipindex)


    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['clip']['v_clipitem_id'] = cur_video_clipitem_id

    # generation clipitem name for video
    cur_video_clipitem_name = 'v_clipitem_name_' + cur_clip_dict['file']['name'][:-4]
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['clip']['clipitem_name'] = cur_video_clipitem_name

    # generation clipitem id for audio left
    cur_audio_clipitem_id = 'aL_clipitem_id_{:s}_{:d}'.format(cur_clip_dict['file']['name'][:-4], clipindex)
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['clip']['aL_clipitem_id'] = cur_audio_clipitem_id

    # generation clipitem id for audio left
    cur_audio_clipitem_id = 'aR_clipitem_id_{:s}_{:d}'.format(cur_clip_dict['file']['name'][:-4], clipindex)
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['clip']['aR_clipitem_id'] = cur_audio_clipitem_id

    clipindex = clipindex + 1

# audio media
file_bit_depth = 16
file_audio_sample_rate = 48000


def make_sequence(in_dict):
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

    #### VIDEO CLIPITEMS ####
    clipitems_ = {}
    for cur_clip_key, cur_clip_dict in in_dict.items():
        file_w = cur_clip_dict['file']['width']
        file_h = cur_clip_dict['file']['height']
        file_id = cur_clip_dict['file']['id']
        file_name = cur_clip_dict['file']['name']
        file_path = cur_clip_dict['file']['path']
        file_dur = cur_clip_dict['file']['dur']

        clipindex = cur_clip_dict['clip']['index']
        v_clipitem_id = cur_clip_dict['clip']['v_clipitem_id']

        aL_clipitem_id = cur_clip_dict['clip']['aL_clipitem_id']
        aR_clipitem_id = cur_clip_dict['clip']['aR_clipitem_id']

        clipitem_name = cur_clip_dict['clip']['clipitem_name']

        clip_start = cur_clip_dict['clip']['start']
        clip_in = cur_clip_dict['clip']['in']
        clip_out = cur_clip_dict['clip']['out']
        clip_dur = clip_out - clip_in
        clip_end = clip_start + clip_dur

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
        file_ = File(keysnvalues=kv, name=file_name, pathurl=file_path,
                     rate=rate_, duration=file_dur, media=media_)

        # link for first video clip with its audio
        link1 = Link(linkclipref=v_clipitem_id, mediatype='video', trackindex=1, clipindex=clipindex)
        link2 = Link(linkclipref=aL_clipitem_id, mediatype='audio', trackindex=1, clipindex=clipindex, groupindex=1)
        link3 = Link(linkclipref=aR_clipitem_id, mediatype='audio', trackindex=2, clipindex=clipindex, groupindex=1)

        # sequence.media.video.track.clipitem
        kv = [['id', v_clipitem_id]]
        v_clip_item = ClipItem(keysnvalues=kv, name=clipitem_name, enabled='TRUE', duration=clip_dur, rate=rate_,
                               start=clip_start, end=clip_end, in_=clip_in, out=clip_out, pixelaspectratio='square',
                               anamorphic='FALSE', file=file_, link1=link1, link2=link2, link3=link3)

        clipitems_[v_clipitem_id] = v_clip_item

    # sequence.media.video.track
    # clipitems_ = {video_clipitem_id_1: v_clip_item_1, video_clipitem_id_2: v_clip_item_2}
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

    #### TRACK 1 AUDIO CLIPITEMS ####
    clipitems_ = {}
    for cur_clip_key, cur_clip_dict in in_dict.items():
        file_id = cur_clip_dict['file']['id']
        aL_clipitem_id = cur_clip_dict['clip']['aL_clipitem_id']

        clipitem_name = cur_clip_dict['clip']['clipitem_name']

        clip_start = cur_clip_dict['clip']['start']
        clip_in = cur_clip_dict['clip']['in']
        clip_out = cur_clip_dict['clip']['out']
        clip_dur = clip_out - clip_in
        clip_end = clip_start + clip_dur

        # sequence.media.audio.track.clipitem.file
        kv = [['id', file_id]]
        file_ = File(keysnvalues=kv)

        # sequence.media.audio.track.clipitem.sourcetrack
        sourcetrack_ = SourceTrack(mediatype='audio', trackindex=1)

        # sequence.media.audio.track.clipitem
        kv = [['id', aL_clipitem_id], ['premiereChannelType', 'stereo']]
        a_clip_item = ClipItem(keysnvalues=kv,  name=clipitem_name, enabled='TRUE', duration=clip_dur, rate=rate_,
                               start=clip_start, end=clip_end, in_=clip_in, out=clip_out, file=file_,
                               sourcetrack=sourcetrack_)

        # sequence.media.audio.track
        clipitems_[aL_clipitem_id] = a_clip_item


    kv = [['PannerCurrentValue', '0.5'], ['PannerIsInverted','true'], ['PannerName', 'Balance'],
    ['currentExplodedTrackIndex', '0'], ['totalExplodedTrackCount', '2'], ['premiereTrackType', 'Stereo']]
    audio_track_1 = Track(keysnvalues=kv, clipitems=clipitems_, enabled='TRUE', locked='FALSE', outputchannelindex=1)


    #### TRACK 2 AUDIO CLIPITEMS ####
    clipitems_ = {}
    for cur_clip_key, cur_clip_dict in in_dict.items():
        file_id = cur_clip_dict['file']['id']

        aR_clipitem_id = cur_clip_dict['clip']['aR_clipitem_id']

        clipitem_name = cur_clip_dict['clip']['clipitem_name']

        clip_start = cur_clip_dict['clip']['start']
        clip_in = cur_clip_dict['clip']['in']
        clip_out = cur_clip_dict['clip']['out']
        clip_dur = clip_out - clip_in
        clip_end = clip_start + clip_dur

        # sequence.media.audio.track.clipitem.file
        kv = [['id', file_id]]
        file_ = File(keysnvalues=kv)

        # sequence.media.audio.track.clipitem.sourcetrack
        sourcetrack_ = SourceTrack(mediatype='audio', trackindex=2)

        # sequence.media.audio.track.clipitem
        kv = [['id', aR_clipitem_id], ['premiereChannelType', 'stereo']]
        a_clip_item = ClipItem(keysnvalues=kv,  name=clipitem_name, enabled='TRUE', duration=clip_dur, rate=rate_,
                             start=clip_start, end=clip_end, in_=clip_in, out=clip_out, file=file_,
                                sourcetrack=sourcetrack_)

        clipitems_[aR_clipitem_id] = a_clip_item



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

    text_file = open("output_main_04.xml", "w")
    text_file.write(line)
    text_file.close()

make_sequence(clips_for_func)















