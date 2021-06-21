from xml.etree.ElementTree import Element, SubElement

class Node:
    def __init__(self, tag=None, keysnvalues=None, **kwargs):
        self.tag = tag
        self.children = {}
        for child_key, child_val in kwargs.items():
            if child_key[-1]=='_':
                child_key_ = child_key[:-1]
            else:
                child_key_ = child_key
            #print(self.tag, child_key_, child_val)
            self.children[str(child_key_)] = child_val
            #print(self.children)
        self._keysnvalues = keysnvalues

    def make_node(self):
        root_node = Element(self.tag)
        if self._keysnvalues:
            for i in self._keysnvalues:
                root_node.set(i[0], i[1])
        #print(self.tag, '*******************')
        #print(self.children)
        for key, val in self.children.items():
            #print(key, val)
            if val != None:
                if isinstance(val, dict):
                    for kkey, vval in val.items():
                        if isinstance(vval, Node):
                            key_node = vval.make_node()
                            #print('key_node', key_node)
                            root_node.append(key_node)
                        else:
                            key_node = SubElement(root_node, kkey)
                            #print('key_node', key_node)
                            key_node.text = str(vval)
                else:
                    if isinstance(val, Node):
                        key_node = val.make_node()
                        #print('key_node', key_node)
                        root_node.append(key_node)
                    else:
                        key_node = SubElement(root_node, key)
                        #print('key_node', key_node)
                        key_node.text = str(val)
        return root_node

    def __str__(self):
        line = 'Node tag: {}\nChildren: {}'.format(self.tag, str(self.children))
        return line


class QTCodec(Node):
    def __init__(self, codecname='Apple ProRes 422', codectypename='Apple ProRes 422',
                 codectypecode='apcn', codecvendorcode='appl', spatialquality=1024,
                 temporalquality=0, keyframerate=0, datarate=0):
        super().__init__(tag='qtcodec', codecname=codecname, codectypename=codectypename,
                 codectypecode=codectypecode, codecvendorcode=codecvendorcode, spatialquality=spatialquality,
                 temporalquality=temporalquality, keyframerate=keyframerate, datarate=datarate)


class Data(Node):
    def __init__(self, qtcodec=None):
        super().__init__(tag='data', qtcodec=qtcodec)


class AppSpecificData(Node):
    def __init__(self, appname='Final Cut Pro', appmanufacturer='Apple Inc.', appversion='7.0', data=None):
        super().__init__(tag='appspecificdata', appname=appname, appmanufacturer=appmanufacturer,
                         appversion=appversion, data=data)


class Codec(Node):
    def __init__(self, name='Apple ProRes 422', appspecificdata=None):
        super().__init__(tag='codec', name=name, appspecificdata=appspecificdata)


class Rate(Node):
    def __init__(self, timebase=25, ntsc='FALSE'):
        super().__init__(tag='rate', timebase=timebase, ntsc=ntsc)

class SampleCharacteristics(Node):
    def __init__(self, rate=None, codec=None, width=None, height=None, anamorphic=None, pixelaspectratio=None,
                 fielddominance=None, colordepth=None, depth=None, samplerate=None):
        super().__init__(tag='samplecharacteristics', rate=rate, codec=codec, width=width, height=height,
                         anamorphic=anamorphic, pixelaspectratio=pixelaspectratio, fielddominance=fielddominance,
                         colordepth=colordepth, depth=depth, samplerate=samplerate)

class Format(Node):
    def __init__(self, samplecharacteristics=None):
        super().__init__(tag='format', samplecharacteristics=samplecharacteristics)


class Video(Node):
    def __init__(self, samplecharacteristics=None, format=None, track=None):
        super().__init__(tag='video', samplecharacteristics=samplecharacteristics, format=format, track=track)


class Audio(Node):
    def __init__(self, samplecharacteristics=None, channelcount=None, numOutputChannels=None, format=None,
                 outputs=None, **tracks):
        super().__init__(tag='audio', samplecharacteristics=samplecharacteristics, channelcount=channelcount,
                         numOutputChannels=numOutputChannels, format=format, outputs=outputs, **tracks)

class Outputs(Node):
    def __init__(self, **groups):
        super().__init__(tag='outputs', **groups)

class Group(Node):
    def __init__(self, index=None, numchannels=None, downmix=None, channel=None):
        super().__init__(tag='group', index=index, numchannels=numchannels, downmix=downmix,
                         channel=channel)

class Channel(Node):
    def __init__(self, index=None):
        super().__init__(tag='channel', index=index)


class Media(Node):
    def __init__(self, video=None, audio=None):
        super().__init__(tag='media', video=video, audio=audio)

class File(Node):
    def __init__(self, keysnvalues=None, name=None, pathurl=None, rate=None, duration=None, media=None):
        super().__init__(tag='file', keysnvalues=keysnvalues, name=name, pathurl=pathurl, rate=rate,
                         duration=duration, media=media)

class Link(Node):
    def __init__(self, linkclipref=None, mediatype=None, trackindex=None, clipindex=None, groupindex=None):
        super().__init__(tag='link', linkclipref=linkclipref, mediatype=mediatype,
                         trackindex=trackindex, clipindex=clipindex, groupindex=groupindex)

class ClipItem(Node):
    def __init__(self, keysnvalues=None,  name=None, enabled=None, duration=None, rate=None, start=None, end=None,
                 in_=None, out=None, file=None, sourcetrack=None, pixelaspectratio=None, anamorphic=None, **links):
        super().__init__(tag='clipitem', keysnvalues=keysnvalues, name=name, enabled=enabled, duration=duration,
                         rate=rate, start=start, end=end, in_=in_, out=out, pixelaspectratio=pixelaspectratio,
                         anamorphic=anamorphic, file=file, sourcetrack=sourcetrack, **links)

class Track(Node):
    def __init__(self, keysnvalues=None, clipitems=None, enabled=None, locked=None, outputchannelindex=None):
        super().__init__(tag='track', keysnvalues=keysnvalues, clipitems=clipitems, enabled=enabled,
                         locked=locked, outputchannelindex=outputchannelindex)


class Timecode(Node):
    def __init__(self, rate=None, string=None, frame=None, displayformat=None):
        super().__init__(tag='timecode', rate=rate, string=string, frame=frame, displayformat=displayformat)

class SourceTrack(Node):
    def __init__(self, mediatype=None, trackindex=None):
        super().__init__(tag='sourcetrack', mediatype=mediatype, trackindex=trackindex)


class Sequence(Node):
    def __init__(self, keysnvalues=None, duration=None, rate=None, name=None, media=None, timecode=None):
        super().__init__(tag='sequence', keysnvalues=keysnvalues, duration=duration, rate=rate, name=name,
                         media=media, timecode=timecode)

class XMEML(Node):
    def __init__(self, keysnvalues=None, **kwargs):
        super().__init__(tag='xmeml', keysnvalues=keysnvalues, **kwargs)






