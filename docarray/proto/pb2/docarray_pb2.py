# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: docarray.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0e\x64ocarray.proto\x12\x08\x64ocarray\x1a\x1cgoogle/protobuf/struct.proto\"A\n\x11\x44\x65nseNdArrayProto\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x12\r\n\x05shape\x18\x02 \x03(\r\x12\r\n\x05\x64type\x18\x03 \x01(\t\"g\n\x0cNdArrayProto\x12*\n\x05\x64\x65nse\x18\x01 \x01(\x0b\x32\x1b.docarray.DenseNdArrayProto\x12+\n\nparameters\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xe2\x02\n\tNodeProto\x12\x0e\n\x04\x62lob\x18\x01 \x01(\x0cH\x00\x12(\n\x06tensor\x18\x02 \x01(\x0b\x32\x16.docarray.NdArrayProtoH\x00\x12\x0e\n\x04text\x18\x03 \x01(\tH\x00\x12)\n\x06nested\x18\x04 \x01(\x0b\x32\x17.docarray.DocumentProtoH\x00\x12.\n\x06\x63hunks\x18\x05 \x01(\x0b\x32\x1c.docarray.DocumentArrayProtoH\x00\x12+\n\tembedding\x18\x06 \x01(\x0b\x32\x16.docarray.NdArrayProtoH\x00\x12\x11\n\x07\x61ny_url\x18\x07 \x01(\tH\x00\x12\x13\n\timage_url\x18\x08 \x01(\tH\x00\x12\x12\n\x08text_url\x18\t \x01(\tH\x00\x12\x0c\n\x02id\x18\n \x01(\tH\x00\x12.\n\x0ctorch_tensor\x18\x0b \x01(\x0b\x32\x16.docarray.NdArrayProtoH\x00\x42\t\n\x07\x63ontent\"\x82\x01\n\rDocumentProto\x12/\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.docarray.DocumentProto.DataEntry\x1a@\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.docarray.NodeProto:\x02\x38\x01\";\n\x12\x44ocumentArrayProto\x12%\n\x04\x64ocs\x18\x01 \x03(\x0b\x32\x17.docarray.DocumentProtob\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'docarray_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _DOCUMENTPROTO_DATAENTRY._options = None
    _DOCUMENTPROTO_DATAENTRY._serialized_options = b'8\001'
    _DENSENDARRAYPROTO._serialized_start = 58
    _DENSENDARRAYPROTO._serialized_end = 123
    _NDARRAYPROTO._serialized_start = 125
    _NDARRAYPROTO._serialized_end = 228
    _NODEPROTO._serialized_start = 231
    _NODEPROTO._serialized_end = 585
    _DOCUMENTPROTO._serialized_start = 588
    _DOCUMENTPROTO._serialized_end = 718
    _DOCUMENTPROTO_DATAENTRY._serialized_start = 654
    _DOCUMENTPROTO_DATAENTRY._serialized_end = 718
    _DOCUMENTARRAYPROTO._serialized_start = 720
    _DOCUMENTARRAYPROTO._serialized_end = 779
# @@protoc_insertion_point(module_scope)
