# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers

class AuthCryptosignRequest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAuthCryptosignRequest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AuthCryptosignRequest()
        x.Init(buf, n + offset)
        return x

    # AuthCryptosignRequest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AuthCryptosignRequest
    def Pubkey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AuthCryptosignRequest
    def ChannelBinding(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def AuthCryptosignRequestStart(builder): builder.StartObject(2)
def AuthCryptosignRequestAddPubkey(builder, pubkey): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(pubkey), 0)
def AuthCryptosignRequestAddChannelBinding(builder, channelBinding): builder.PrependUint8Slot(1, channelBinding, 0)
def AuthCryptosignRequestEnd(builder): return builder.EndObject()