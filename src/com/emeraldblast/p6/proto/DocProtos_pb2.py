# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/emeraldblast/p6/proto/DocProtos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.emeraldblast.p6.proto import CommonProtos_pb2 as com_dot_emeraldblast_dot_p6_dot_proto_dot_CommonProtos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)com/emeraldblast/p6/proto/DocProtos.proto\x12\x19\x63om.emeraldblast.p6.proto\x1a,com/emeraldblast/p6/proto/CommonProtos.proto\"\x90\x01\n\x11RangeAddressProto\x12<\n\x07topLeft\x18\x01 \x01(\x0b\x32+.com.emeraldblast.p6.proto.CellAddressProto\x12=\n\x08\x62otRight\x18\x02 \x01(\x0b\x32+.com.emeraldblast.p6.proto.CellAddressProto\"\xab\x01\n\x0cRangeIdProto\x12\x42\n\x0crangeAddress\x18\x01 \x01(\x0b\x32,.com.emeraldblast.p6.proto.RangeAddressProto\x12@\n\x0bworkbookKey\x18\x02 \x01(\x0b\x32+.com.emeraldblast.p6.proto.WorkbookKeyProto\x12\x15\n\rworksheetName\x18\x03 \x01(\t\",\n\x10\x43\x65llAddressProto\x12\x0b\n\x03\x63ol\x18\x01 \x01(\x05\x12\x0b\n\x03row\x18\x02 \x01(\x05\"\xa1\x01\n\tCellProto\x12\x14\n\x0c\x64isplayValue\x18\x01 \x01(\t\x12\x0f\n\x07\x66ormula\x18\x02 \x01(\t\x12\x0e\n\x06script\x18\x03 \x01(\t\x12\x10\n\x08isObject\x18\x04 \x01(\x08\x12<\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0b\x32+.com.emeraldblast.p6.proto.CellAddressProto\x12\r\n\x05value\x18\x06 \x01(\t\"R\n\x0eWorksheetProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x04\x63\x65ll\x18\x02 \x03(\x0b\x32$.com.emeraldblast.p6.proto.CellProto\"<\n\x10WorkbookKeyProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04path\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_path\"\x8f\x01\n\rWorkbookProto\x12@\n\x0bworkbookKey\x18\x01 \x01(\x0b\x32+.com.emeraldblast.p6.proto.WorkbookKeyProto\x12<\n\tworksheet\x18\x02 \x03(\x0b\x32).com.emeraldblast.p6.proto.WorksheetProtob\x06proto3')



_RANGEADDRESSPROTO = DESCRIPTOR.message_types_by_name['RangeAddressProto']
_RANGEIDPROTO = DESCRIPTOR.message_types_by_name['RangeIdProto']
_CELLADDRESSPROTO = DESCRIPTOR.message_types_by_name['CellAddressProto']
_CELLPROTO = DESCRIPTOR.message_types_by_name['CellProto']
_WORKSHEETPROTO = DESCRIPTOR.message_types_by_name['WorksheetProto']
_WORKBOOKKEYPROTO = DESCRIPTOR.message_types_by_name['WorkbookKeyProto']
_WORKBOOKPROTO = DESCRIPTOR.message_types_by_name['WorkbookProto']
RangeAddressProto = _reflection.GeneratedProtocolMessageType('RangeAddressProto', (_message.Message,), {
  'DESCRIPTOR' : _RANGEADDRESSPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.RangeAddressProto)
  })
_sym_db.RegisterMessage(RangeAddressProto)

RangeIdProto = _reflection.GeneratedProtocolMessageType('RangeIdProto', (_message.Message,), {
  'DESCRIPTOR' : _RANGEIDPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.RangeIdProto)
  })
_sym_db.RegisterMessage(RangeIdProto)

CellAddressProto = _reflection.GeneratedProtocolMessageType('CellAddressProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLADDRESSPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.CellAddressProto)
  })
_sym_db.RegisterMessage(CellAddressProto)

CellProto = _reflection.GeneratedProtocolMessageType('CellProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.CellProto)
  })
_sym_db.RegisterMessage(CellProto)

WorksheetProto = _reflection.GeneratedProtocolMessageType('WorksheetProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKSHEETPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.WorksheetProto)
  })
_sym_db.RegisterMessage(WorksheetProto)

WorkbookKeyProto = _reflection.GeneratedProtocolMessageType('WorkbookKeyProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKBOOKKEYPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.WorkbookKeyProto)
  })
_sym_db.RegisterMessage(WorkbookKeyProto)

WorkbookProto = _reflection.GeneratedProtocolMessageType('WorkbookProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKBOOKPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.WorkbookProto)
  })
_sym_db.RegisterMessage(WorkbookProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RANGEADDRESSPROTO._serialized_start=119
  _RANGEADDRESSPROTO._serialized_end=263
  _RANGEIDPROTO._serialized_start=266
  _RANGEIDPROTO._serialized_end=437
  _CELLADDRESSPROTO._serialized_start=439
  _CELLADDRESSPROTO._serialized_end=483
  _CELLPROTO._serialized_start=486
  _CELLPROTO._serialized_end=647
  _WORKSHEETPROTO._serialized_start=649
  _WORKSHEETPROTO._serialized_end=731
  _WORKBOOKKEYPROTO._serialized_start=733
  _WORKBOOKKEYPROTO._serialized_end=793
  _WORKBOOKPROTO._serialized_start=796
  _WORKBOOKPROTO._serialized_end=939
# @@protoc_insertion_point(module_scope)
