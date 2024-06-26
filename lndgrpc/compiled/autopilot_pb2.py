# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lndgrpc/compiled/autopilot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n lndgrpc/compiled/autopilot.proto\x12\x0c\x61utopilotrpc\"\x0f\n\rStatusRequest\" \n\x0eStatusResponse\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\"%\n\x13ModifyStatusRequest\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"\x16\n\x14ModifyStatusResponse\"A\n\x12QueryScoresRequest\x12\x0f\n\x07pubkeys\x18\x01 \x03(\t\x12\x1a\n\x12ignore_local_state\x18\x02 \x01(\x08\"\xfe\x01\n\x13QueryScoresResponse\x12\x42\n\x07results\x18\x01 \x03(\x0b\x32\x31.autopilotrpc.QueryScoresResponse.HeuristicResult\x1a\xa2\x01\n\x0fHeuristicResult\x12\x11\n\theuristic\x18\x01 \x01(\t\x12M\n\x06scores\x18\x02 \x03(\x0b\x32=.autopilotrpc.QueryScoresResponse.HeuristicResult.ScoresEntry\x1a-\n\x0bScoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x90\x01\n\x10SetScoresRequest\x12\x11\n\theuristic\x18\x01 \x01(\t\x12:\n\x06scores\x18\x02 \x03(\x0b\x32*.autopilotrpc.SetScoresRequest.ScoresEntry\x1a-\n\x0bScoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x13\n\x11SetScoresResponse2\xc9\x02\n\tAutopilot\x12\x43\n\x06Status\x12\x1b.autopilotrpc.StatusRequest\x1a\x1c.autopilotrpc.StatusResponse\x12U\n\x0cModifyStatus\x12!.autopilotrpc.ModifyStatusRequest\x1a\".autopilotrpc.ModifyStatusResponse\x12R\n\x0bQueryScores\x12 .autopilotrpc.QueryScoresRequest\x1a!.autopilotrpc.QueryScoresResponse\x12L\n\tSetScores\x12\x1e.autopilotrpc.SetScoresRequest\x1a\x1f.autopilotrpc.SetScoresResponseB4Z2github.com/lightningnetwork/lnd/lnrpc/autopilotrpcb\x06proto3')



_STATUSREQUEST = DESCRIPTOR.message_types_by_name['StatusRequest']
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
_MODIFYSTATUSREQUEST = DESCRIPTOR.message_types_by_name['ModifyStatusRequest']
_MODIFYSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['ModifyStatusResponse']
_QUERYSCORESREQUEST = DESCRIPTOR.message_types_by_name['QueryScoresRequest']
_QUERYSCORESRESPONSE = DESCRIPTOR.message_types_by_name['QueryScoresResponse']
_QUERYSCORESRESPONSE_HEURISTICRESULT = _QUERYSCORESRESPONSE.nested_types_by_name['HeuristicResult']
_QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY = _QUERYSCORESRESPONSE_HEURISTICRESULT.nested_types_by_name['ScoresEntry']
_SETSCORESREQUEST = DESCRIPTOR.message_types_by_name['SetScoresRequest']
_SETSCORESREQUEST_SCORESENTRY = _SETSCORESREQUEST.nested_types_by_name['ScoresEntry']
_SETSCORESRESPONSE = DESCRIPTOR.message_types_by_name['SetScoresResponse']
StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'lndgrpc.compiled.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'lndgrpc.compiled.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)

ModifyStatusRequest = _reflection.GeneratedProtocolMessageType('ModifyStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYSTATUSREQUEST,
  '__module__' : 'lndgrpc.compiled.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.ModifyStatusRequest)
  })
_sym_db.RegisterMessage(ModifyStatusRequest)

ModifyStatusResponse = _reflection.GeneratedProtocolMessageType('ModifyStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYSTATUSRESPONSE,
  '__module__' : 'lndgrpc.compiled.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.ModifyStatusResponse)
  })
_sym_db.RegisterMessage(ModifyStatusResponse)

QueryScoresRequest = _reflection.GeneratedProtocolMessageType('QueryScoresRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSCORESREQUEST,
  '__module__' : 'lndgrpc.compiled.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.QueryScoresRequest)
  })
_sym_db.RegisterMessage(QueryScoresRequest)

QueryScoresResponse = _reflection.GeneratedProtocolMessageType('QueryScoresResponse', (_message.Message,), {

  'HeuristicResult' : _reflection.GeneratedProtocolMessageType('HeuristicResult', (_message.Message,), {

    'ScoresEntry' : _reflection.GeneratedProtocolMessageType('ScoresEntry', (_message.Message,), {
      'DESCRIPTOR' : _QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY,
      '__module__' : 'lndgrpc.compiled.autopilot_pb2'
      # @@protoc_insertion_point(class_scope:autopilotrpc.QueryScoresResponse.HeuristicResult.ScoresEntry)
      })
    ,
    'DESCRIPTOR' : _QUERYSCORESRESPONSE_HEURISTICRESULT,
    '__module__' : 'lndgrpc.compiled.autopilot_pb2'
    # @@protoc_insertion_point(class_scope:autopilotrpc.QueryScoresResponse.HeuristicResult)
    })
  ,
  'DESCRIPTOR' : _QUERYSCORESRESPONSE,
  '__module__' : 'lndgrpc.compiled.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.QueryScoresResponse)
  })
_sym_db.RegisterMessage(QueryScoresResponse)
_sym_db.RegisterMessage(QueryScoresResponse.HeuristicResult)
_sym_db.RegisterMessage(QueryScoresResponse.HeuristicResult.ScoresEntry)

SetScoresRequest = _reflection.GeneratedProtocolMessageType('SetScoresRequest', (_message.Message,), {

  'ScoresEntry' : _reflection.GeneratedProtocolMessageType('ScoresEntry', (_message.Message,), {
    'DESCRIPTOR' : _SETSCORESREQUEST_SCORESENTRY,
    '__module__' : 'lndgrpc.compiled.autopilot_pb2'
    # @@protoc_insertion_point(class_scope:autopilotrpc.SetScoresRequest.ScoresEntry)
    })
  ,
  'DESCRIPTOR' : _SETSCORESREQUEST,
  '__module__' : 'lndgrpc.compiled.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.SetScoresRequest)
  })
_sym_db.RegisterMessage(SetScoresRequest)
_sym_db.RegisterMessage(SetScoresRequest.ScoresEntry)

SetScoresResponse = _reflection.GeneratedProtocolMessageType('SetScoresResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETSCORESRESPONSE,
  '__module__' : 'lndgrpc.compiled.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.SetScoresResponse)
  })
_sym_db.RegisterMessage(SetScoresResponse)

_AUTOPILOT = DESCRIPTOR.services_by_name['Autopilot']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/lightningnetwork/lnd/lnrpc/autopilotrpc'
  _QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY._options = None
  _QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY._serialized_options = b'8\001'
  _SETSCORESREQUEST_SCORESENTRY._options = None
  _SETSCORESREQUEST_SCORESENTRY._serialized_options = b'8\001'
  _STATUSREQUEST._serialized_start=50
  _STATUSREQUEST._serialized_end=65
  _STATUSRESPONSE._serialized_start=67
  _STATUSRESPONSE._serialized_end=99
  _MODIFYSTATUSREQUEST._serialized_start=101
  _MODIFYSTATUSREQUEST._serialized_end=138
  _MODIFYSTATUSRESPONSE._serialized_start=140
  _MODIFYSTATUSRESPONSE._serialized_end=162
  _QUERYSCORESREQUEST._serialized_start=164
  _QUERYSCORESREQUEST._serialized_end=229
  _QUERYSCORESRESPONSE._serialized_start=232
  _QUERYSCORESRESPONSE._serialized_end=486
  _QUERYSCORESRESPONSE_HEURISTICRESULT._serialized_start=324
  _QUERYSCORESRESPONSE_HEURISTICRESULT._serialized_end=486
  _QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY._serialized_start=441
  _QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY._serialized_end=486
  _SETSCORESREQUEST._serialized_start=489
  _SETSCORESREQUEST._serialized_end=633
  _SETSCORESREQUEST_SCORESENTRY._serialized_start=441
  _SETSCORESREQUEST_SCORESENTRY._serialized_end=486
  _SETSCORESRESPONSE._serialized_start=635
  _SETSCORESRESPONSE._serialized_end=654
  _AUTOPILOT._serialized_start=657
  _AUTOPILOT._serialized_end=986
# @@protoc_insertion_point(module_scope)
