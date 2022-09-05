# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/qxdzbc/p6/proto/rpc/worksheet/WorksheetServiceProtos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.qxdzbc.p6.proto import CommonProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_CommonProtos__pb2
from com.qxdzbc.p6.proto import DocProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_DocProtos__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from com.qxdzbc.p6.proto import WorksheetProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_WorksheetProtos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>com/qxdzbc/p6/proto/rpc/worksheet/WorksheetServiceProtos.proto\x12!com.qxdzbc.p6.proto.rpc.worksheet\x1a&com/qxdzbc/p6/proto/CommonProtos.proto\x1a#com/qxdzbc/p6/proto/DocProtos.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a)com/qxdzbc/p6/proto/WorksheetProtos.proto\"\'\n\x16\x43\x65llCountResponseProto\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\"Y\n\x17GetAllCellResponseProto\x12>\n\x0f\x63\x65llAddressList\x18\x01 \x03(\x0b\x32%.com.qxdzbc.p6.proto.CellAddressProto\"\x92\x01\n\x1f\x43heckContainAddressRequestProto\x12\x33\n\x04wsId\x18\x01 \x01(\x0b\x32%.com.qxdzbc.p6.proto.WorksheetIdProto\x12:\n\x0b\x63\x65llAddress\x18\x02 \x01(\x0b\x32%.com.qxdzbc.p6.proto.CellAddressProto\"o\n\x19GetUsedRangeResponseProto\x12\x41\n\x0crangeAddress\x18\x01 \x01(\x0b\x32&.com.qxdzbc.p6.proto.RangeAddressProtoH\x00\x88\x01\x01\x42\x0f\n\r_rangeAddressb\x06proto3')



_CELLCOUNTRESPONSEPROTO = DESCRIPTOR.message_types_by_name['CellCountResponseProto']
_GETALLCELLRESPONSEPROTO = DESCRIPTOR.message_types_by_name['GetAllCellResponseProto']
_CHECKCONTAINADDRESSREQUESTPROTO = DESCRIPTOR.message_types_by_name['CheckContainAddressRequestProto']
_GETUSEDRANGERESPONSEPROTO = DESCRIPTOR.message_types_by_name['GetUsedRangeResponseProto']
CellCountResponseProto = _reflection.GeneratedProtocolMessageType('CellCountResponseProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLCOUNTRESPONSEPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.rpc.worksheet.WorksheetServiceProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.rpc.worksheet.CellCountResponseProto)
  })
_sym_db.RegisterMessage(CellCountResponseProto)

GetAllCellResponseProto = _reflection.GeneratedProtocolMessageType('GetAllCellResponseProto', (_message.Message,), {
  'DESCRIPTOR' : _GETALLCELLRESPONSEPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.rpc.worksheet.WorksheetServiceProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.rpc.worksheet.GetAllCellResponseProto)
  })
_sym_db.RegisterMessage(GetAllCellResponseProto)

CheckContainAddressRequestProto = _reflection.GeneratedProtocolMessageType('CheckContainAddressRequestProto', (_message.Message,), {
  'DESCRIPTOR' : _CHECKCONTAINADDRESSREQUESTPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.rpc.worksheet.WorksheetServiceProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.rpc.worksheet.CheckContainAddressRequestProto)
  })
_sym_db.RegisterMessage(CheckContainAddressRequestProto)

GetUsedRangeResponseProto = _reflection.GeneratedProtocolMessageType('GetUsedRangeResponseProto', (_message.Message,), {
  'DESCRIPTOR' : _GETUSEDRANGERESPONSEPROTO,
  '__module__' : 'com.qxdzbc.p6.proto.rpc.worksheet.WorksheetServiceProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.qxdzbc.p6.proto.rpc.worksheet.GetUsedRangeResponseProto)
  })
_sym_db.RegisterMessage(GetUsedRangeResponseProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CELLCOUNTRESPONSEPROTO._serialized_start=282
  _CELLCOUNTRESPONSEPROTO._serialized_end=321
  _GETALLCELLRESPONSEPROTO._serialized_start=323
  _GETALLCELLRESPONSEPROTO._serialized_end=412
  _CHECKCONTAINADDRESSREQUESTPROTO._serialized_start=415
  _CHECKCONTAINADDRESSREQUESTPROTO._serialized_end=561
  _GETUSEDRANGERESPONSEPROTO._serialized_start=563
  _GETUSEDRANGERESPONSEPROTO._serialized_end=674
# @@protoc_insertion_point(module_scope)
