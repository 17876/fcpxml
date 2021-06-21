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
            'end': 534,
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
            'end': 1113,
            'in': 0,
            'out': 493
        }
    }
}

clips_for_func = copy.deepcopy(clips)
clipindex = 1
for cur_clip_key, cur_clip_dict in clips.items():

    clips_for_func[cur_clip_key]['clip']['index'] = clipindex
    clipindex = clipindex + 1

    # generation file_id
    cur_file_id = 'file_id_' + cur_clip_dict['file']['name'][:-4]
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['file']['id'] = cur_file_id

    # generation file path
    cur_file_path = path + cur_clip_dict['file']['name']
    # adding this to clips_for_func
    clips_for_func[cur_clip_key]['file']['path'] = cur_file_path

    # generation clipitem_id for video
    cur_video_clipitem_id = 'v_clipitem_id_' + cur_clip_dict['file']['name'][:-4]
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['clip']['v_clipitem_id'] = cur_video_clipitem_id

    # generation clipitem name for video
    cur_video_clipitem_name = 'v_clipitem_name_' + cur_clip_dict['file']['name'][:-4]
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['clip']['clipitem_name'] = cur_video_clipitem_name

    # generation clipitem id for audio left
    cur_audio_clipitem_id = 'aL_clipitem_id_' + cur_clip_dict['file']['name'][:-4]
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['clip']['aL_clipitem_id'] = cur_audio_clipitem_id

    # generation clipitem id for audio left
    cur_audio_clipitem_id = 'aR_clipitem_id_' + cur_clip_dict['file']['name'][:-4]
    # adding this id to clips_for_func
    clips_for_func[cur_clip_key]['clip']['aR_clipitem_id'] = cur_audio_clipitem_id


#
# # file 1 parameters
# file_name_1 = 'Chayki.mp4'
# file_path_1 = path + file_name_1
# file_dur_1 = 534
# file_w_1 = 750
# file_h_1 = 576
# file_id_1 = 'chaiki_file'
#
#
# # file 2 parameters
# file_name_2 = 'Alisa.mp4'
# file_path_2 = path + file_name_2
# file_dur_2 = 493
# file_w_2 = 750
# file_h_2 = 576
# file_id_2 = 'alisa_file'
#
# # video clip 1 parameters
# clip_start_1 = 0
# clip_end_1 = 534
# clip_dur_1 = 534
# clip_in_1 = 0
# clip_out_1 = 534
# video_clipitem_id_1 = 'v_clipitem_chaiki'
# clipitem_name_1 = 'Chayki.mp4'
#
# # video clip 2 parameters
# clip_start_2 = 620
# clip_end_2 = 1113
# clip_dur_2 = 493
# clip_in_2 = 0
# clip_out_2 = 493
# video_clipitem_id_2 = 'v_clipitem_alisa'
# clipitem_name_2 = 'Alisa.mp4'

# audio media
file_bit_depth = 16
file_audio_sample_rate = 48000

# # 1
# audio_clipitem_L_id_1 = 'a_clipitem_chaiki_L'
# audio_clipitem_R_id_1 = 'a_clipitem_chaiki_R'
#
# # 2
# audio_clipitem_L_id_2 = 'a_clipitem_alisa_L'
# audio_clipitem_R_id_2 = 'a_clipitem_alisa_R'

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

    #### VIDEO CLIPITEM 1 ####

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
        clip_end = cur_clip_dict['clip']['end']
        clip_in = cur_clip_dict['clip']['in']
        clip_out = cur_clip_dict['clip']['out']

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

    # link for second video clip with its audio
    clipindex = 2
    link1 = Link(linkclipref=video_clipitem_id_2, mediatype='video', trackindex=1, clipindex=clipindex)
    link2 = Link(linkclipref=audio_clipitem_L_id_2, mediatype='audio', trackindex=1, clipindex=clipindex, groupindex=1)
    link3 = Link(linkclipref=audio_clipitem_R_id_2, mediatype='audio', trackindex=2, clipindex=clipindex, groupindex=1)


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


    # sequence.media.audio.track.clipitem.file
    kv = [['id', file_id_1]]
    file_ = File(keysnvalues=kv)

    # sequence.media.audio.track.clipitem.sourcetrack
    sourcetrack_ = SourceTrack(mediatype='audio', trackindex=1)

    # sequence.media.audio.track.clipitem
    kv = [['id', audio_clipitem_L_id_1], ['premiereChannelType', 'stereo']]
    a_clip_item_1 = ClipItem(keysnvalues=kv,  name=clipitem_name_1, enabled='TRUE', duration=clip_dur_1, rate=rate_,
                           start=clip_start_1, end=clip_end_1, in_=clip_in_1, out=clip_out_1, file=file_,
                           sourcetrack=sourcetrack_)

    #### TRACK 1 AUDIO CLIPITEM 2 ####

    # sequence.media.audio.track.clipitem.file
    kv = [['id', file_id_2]]
    file_ = File(keysnvalues=kv)

    # sequence.media.audio.track.clipitem.sourcetrack
    sourcetrack_ = SourceTrack(mediatype='audio', trackindex=1)

    # sequence.media.audio.track.clipitem
    kv = [['id', audio_clipitem_L_id_2], ['premiereChannelType', 'stereo']]
    a_clip_item_2 = ClipItem(keysnvalues=kv,  name=clipitem_name_2, enabled='TRUE', duration=clip_dur_2, rate=rate_,
                           start=clip_start_2, end=clip_end_2, in_=clip_in_2, out=clip_out_2, file=file_,
                           sourcetrack=sourcetrack_)


    # sequence.media.audio.track
    clipitems_ = {audio_clipitem_L_id_1: a_clip_item_1, audio_clipitem_L_id_2: a_clip_item_2}
    kv = [['PannerCurrentValue', '0.5'], ['PannerIsInverted','true'], ['PannerName', 'Balance'],
    ['currentExplodedTrackIndex', '0'], ['totalExplodedTrackCount', '2'], ['premiereTrackType', 'Stereo']]
    audio_track_1 = Track(keysnvalues=kv, clipitems=clipitems_, enabled='TRUE', locked='FALSE', outputchannelindex=1)




    #### TRACK 2 AUDIO CLIPITEM 1 ####

    # sequence.media.audio.track.clipitem.file
    kv = [['id', file_id_1]]
    file_ = File(keysnvalues=kv)

    # sequence.media.audio.track.clipitem.sourcetrack
    sourcetrack_ = SourceTrack(mediatype='audio', trackindex=2)

    # sequence.media.audio.track.clipitem
    kv = [['id', audio_clipitem_R_id_1], ['premiereChannelType', 'stereo']]
    a_clipitem_1 = ClipItem(keysnvalues=kv,  name=clipitem_name_1, enabled='TRUE', duration=clip_dur_1, rate=rate_,
                         start=clip_start_1, end=clip_end_1, in_=clip_in_1, out=clip_out_1, file=file_,
                            sourcetrack=sourcetrack_,)


    #### TRACK 2 AUDIO CLIPITEM 2 ####

    # sequence.media.audio.track.clipitem.file
    kv = [['id', file_id_2]]
    file_ = File(keysnvalues=kv)

    # sequence.media.audio.track.clipitem.sourcetrack
    sourcetrack_ = SourceTrack(mediatype='audio', trackindex=2)

    # sequence.media.audio.track.clipitem
    kv = [['id', audio_clipitem_R_id_2], ['premiereChannelType', 'stereo']]
    a_clipitem_2 = ClipItem(keysnvalues=kv,  name=clipitem_name_2, enabled='TRUE', duration=clip_dur_2, rate=rate_,
                         start=clip_start_2, end=clip_end_2, in_=clip_in_2, out=clip_out_2, file=file_,
                            sourcetrack=sourcetrack_)


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

    text_file = open("output_main_03.xml", "w")
    text_file.write(line)
    text_file.close()

















