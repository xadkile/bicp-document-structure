# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/qxdzbc/p6/proto/DocProtos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.qxdzbc.p6.proto import CommonProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_CommonProtos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#com/qxdzbc/p6/proto/DocProtos.proto\x12\x13\x63om.qxdzbc.p6.proto\x1a&com/qxdzbc/p6/proto/CommonProtos.proto\"\x82\x01\n\x0eWorksheetProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x04\x63\x65ll\x18\x02 \x03(\x0b\x32\x1e.com.qxdzbc.p6.proto.CellProto\x12\x34\n\x05wbKey\x18\x03 \x01(\x0b\x32%.com.qxdzbc.p6.proto.WorkbookKeyProto\"\x84\x01\n\x11RangeAddressProto\x12\x36\n\x07topLeft\x18\x01 \x01(\x0b\x32%.com.qxdzbc.p6.proto.CellAddressProto\x12\x37\n\x08\x62otRight\x18\x02 \x01(\x0b\x32%.com.qxdzbc.p6.proto.CellAddressProto\"\x9f\x01\n\x0cRangeIdProto\x12<\n\x0crangeAddress\x18\x01 \x01(\x0b\x32&.com.qxdzbc.p6.proto.RangeAddressProto\x12:\n\x0bworkbookKey\x18\x02 \x01(\x0b\x32%.com.qxdzbc.p6.proto.WorkbookKeyProto\x12\x15\n\rworksheetName\x18\x03 \x01(\t\"^\n\tWsWbProto\x12:\n\x0bworkbookKey\x18\x02 \x01(\x0b\x32%.com.qxdzbc.p6.proto.WorkbookKeyProto\x12\x15\n\rworksheetName\x18\x03 \x01(\t\",\n\x10\x43\x65llAddressProto\x12\x0b\n\x03\x63ol\x18\x01 \x01(\x05\x12\x0b\n\x03row\x18\x02 \x01(\x05\"\xa8\x01\n\tCellProto\x12\x36\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32%.com.qxdzbc.p6.proto.CellAddressProto\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32#.com.qxdzbc.p6.proto.CellValueProtoH\x00\x88\x01\x01\x12\x14\n\x07\x66ormula\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_valueB\n\n\x08_formula\"\x9f\x01\n\nCell2Proto\x12,\n\x02id\x18\x01 \x01(\x0b\x32 .com.qxdzbc.p6.proto.CellIdProto\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32#.com.qxdzbc.p6.proto.CellValueProtoH\x00\x88\x01\x01\x12\x14\n\x07\x66ormula\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_valueB\n\n\x08_formula\"`\n\x0e\x43\x65llValueProto\x12\x10\n\x03str\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03num\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x11\n\x04\x62ool\x18\x03 \x01(\x08H\x02\x88\x01\x01\x42\x06\n\x04_strB\x06\n\x04_numB\x07\n\x05_bool\"<\n\x10WorkbookKeyProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04path\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_path\"6\n\x16SimpleScriptEntryProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06script\x18\x02 \x01(\t\"\xc1\x01\n\rWorkbookProto\x12:\n\x0bworkbookKey\x18\x01 \x01(\x0b\x32%.com.qxdzbc.p6.proto.WorkbookKeyProto\x12\x36\n\tworksheet\x18\x02 \x03(\x0b\x32#.com.qxdzbc.p6.proto.WorksheetProto\x12<\n\x07scripts\x18\x03 \x03(\x0b\x32+.com.qxdzbc.p6.proto.SimpleScriptEntryProto\"\x8f\x01\n\x0b\x43\x65llIdProto\x12:\n\x0b\x63\x65llAddress\x18\x01 \x01(\x0b\x32%.com.qxdzbc.p6.proto.CellAddressProto\x12\x34\n\x05wbKey\x18\x02 \x01(\x0b\x32%.com.qxdzbc.p6.proto.WorkbookKeyProto\x12\x0e\n\x06wsName\x18\x03 \x01(\tb\x06proto3')



_WORKSHEETPROTO = DESCRIPTOR.message_types_by_name['WorksheetProto']
_RANGEADDRESSPROTO = DESCRIPTOR.message_types_by_name['RangeAddressProto']
_RANGEIDPROTO = DESCRIPTOR.message_types_by_name['RangeIdProto']
_WSWBPROTO = DESCRIPTOR.message_types_by_name['WsWbProto']
_CELLADDRESSPROTO = DESCRIPTOR.message_types_by_name['CellAddressProto']
_CELLPROTO = DESCRIPTOR.message_types_by_name['CellProto']
_CELL2PROTO = DESCRIPTOR.message_types_by_name['Cell2Proto']
_CELLVALUEPROTO = DESCRIPTOR.message_types_by_name['CellValueProto']
_WORKBOOKKEYPROTO = DESCRIPTOR.message_types_by_name['WorkbookKeyProto']
_SIMPLESCRIPTENTRYPROTO = DESCRIPTOR.message_types_by_name['SimpleScriptEntryProto']
_WORKBOOKPROTO = DESCRIPTOR.message_types_by_name['WorkbookProto']
_CELLIDPROTO = DESCRIPTOR.message_types_by_name['CellIdProto']
WorksheetProto = _reflection.GeneratedProtocolMessageType('WorksheetProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKSHEETPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.WorksheetProto)
  })
_sym_db.RegisterMessage(WorksheetProto)

RangeAddressProto = _reflection.GeneratedProtocolMessageType('RangeAddressProto', (_message.Message,), {
  'DESCRIPTOR' : _RANGEADDRESSPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.RangeAddressProto)
  })
_sym_db.RegisterMessage(RangeAddressProto)

RangeIdProto = _reflection.GeneratedProtocolMessageType('RangeIdProto', (_message.Message,), {
  'DESCRIPTOR' : _RANGEIDPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.RangeIdProto)
  })
_sym_db.RegisterMessage(RangeIdProto)

WsWbProto = _reflection.GeneratedProtocolMessageType('WsWbProto', (_message.Message,), {
  'DESCRIPTOR' : _WSWBPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.WsWbProto)
  })
_sym_db.RegisterMessage(WsWbProto)

CellAddressProto = _reflection.GeneratedProtocolMessageType('CellAddressProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLADDRESSPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.CellAddressProto)
  })
_sym_db.RegisterMessage(CellAddressProto)

CellProto = _reflection.GeneratedProtocolMessageType('CellProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.CellProto)
  })
_sym_db.RegisterMessage(CellProto)

Cell2Proto = _reflection.GeneratedProtocolMessageType('Cell2Proto', (_message.Message,), {
  'DESCRIPTOR' : _CELL2PROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.Cell2Proto)
  })
_sym_db.RegisterMessage(Cell2Proto)

CellValueProto = _reflection.GeneratedProtocolMessageType('CellValueProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLVALUEPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.CellValueProto)
  })
_sym_db.RegisterMessage(CellValueProto)

WorkbookKeyProto = _reflection.GeneratedProtocolMessageType('WorkbookKeyProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKBOOKKEYPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.WorkbookKeyProto)
  })
_sym_db.RegisterMessage(WorkbookKeyProto)

SimpleScriptEntryProto = _reflection.GeneratedProtocolMessageType('SimpleScriptEntryProto', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLESCRIPTENTRYPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.SimpleScriptEntryProto)
  })
_sym_db.RegisterMessage(SimpleScriptEntryProto)

WorkbookProto = _reflection.GeneratedProtocolMessageType('WorkbookProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKBOOKPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.WorkbookProto)
  })
_sym_db.RegisterMessage(WorkbookProto)

CellIdProto = _reflection.GeneratedProtocolMessageType('CellIdProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLIDPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.DocProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.CellIdProto)
  })
_sym_db.RegisterMessage(CellIdProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORKSHEETPROTO._serialized_start=101
  _WORKSHEETPROTO._serialized_end=231
  _RANGEADDRESSPROTO._serialized_start=234
  _RANGEADDRESSPROTO._serialized_end=366
  _RANGEIDPROTO._serialized_start=369
  _RANGEIDPROTO._serialized_end=528
  _WSWBPROTO._serialized_start=530
  _WSWBPROTO._serialized_end=624
  _CELLADDRESSPROTO._serialized_start=626
  _CELLADDRESSPROTO._serialized_end=670
  _CELLPROTO._serialized_start=673
  _CELLPROTO._serialized_end=841
  _CELL2PROTO._serialized_start=844
  _CELL2PROTO._serialized_end=1003
  _CELLVALUEPROTO._serialized_start=1005
  _CELLVALUEPROTO._serialized_end=1101
  _WORKBOOKKEYPROTO._serialized_start=1103
  _WORKBOOKKEYPROTO._serialized_end=1163
  _SIMPLESCRIPTENTRYPROTO._serialized_start=1165
  _SIMPLESCRIPTENTRYPROTO._serialized_end=1219
  _WORKBOOKPROTO._serialized_start=1222
  _WORKBOOKPROTO._serialized_end=1415
  _CELLIDPROTO._serialized_start=1418
  _CELLIDPROTO._serialized_end=1561
# @@protoc_insertion_point(module_scope)
