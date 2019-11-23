# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: slp_graphsearchrpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='slp_graphsearchrpc.proto',
  package='graphsearch',
  syntax='proto3',
  serialized_options=_b('\n\034io.grpc.examples.graphsearchB\020GraphSearchProtoP\001\242\002\002GS'),
  serialized_pb=_b('\n\x18slp_graphsearchrpc.proto\x12\x0bgraphsearch\"\"\n\x12GraphSearchRequest\x12\x0c\n\x04txid\x18\x01 \x01(\t\"\"\n\x10GraphSearchReply\x12\x0e\n\x06txdata\x18\x01 \x03(\x0c\x32\x65\n\x12GraphSearchService\x12O\n\x0bGraphSearch\x12\x1f.graphsearch.GraphSearchRequest\x1a\x1d.graphsearch.GraphSearchReply\"\x00\x42\x37\n\x1cio.grpc.examples.graphsearchB\x10GraphSearchProtoP\x01\xa2\x02\x02GSb\x06proto3')
)




_GRAPHSEARCHREQUEST = _descriptor.Descriptor(
  name='GraphSearchRequest',
  full_name='graphsearch.GraphSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txid', full_name='graphsearch.GraphSearchRequest.txid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=75,
)


_GRAPHSEARCHREPLY = _descriptor.Descriptor(
  name='GraphSearchReply',
  full_name='graphsearch.GraphSearchReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txdata', full_name='graphsearch.GraphSearchReply.txdata', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['GraphSearchRequest'] = _GRAPHSEARCHREQUEST
DESCRIPTOR.message_types_by_name['GraphSearchReply'] = _GRAPHSEARCHREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GraphSearchRequest = _reflection.GeneratedProtocolMessageType('GraphSearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHSEARCHREQUEST,
  '__module__' : 'slp_graphsearchrpc_pb2'
  # @@protoc_insertion_point(class_scope:graphsearch.GraphSearchRequest)
  })
_sym_db.RegisterMessage(GraphSearchRequest)

GraphSearchReply = _reflection.GeneratedProtocolMessageType('GraphSearchReply', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHSEARCHREPLY,
  '__module__' : 'slp_graphsearchrpc_pb2'
  # @@protoc_insertion_point(class_scope:graphsearch.GraphSearchReply)
  })
_sym_db.RegisterMessage(GraphSearchReply)


DESCRIPTOR._options = None

_GRAPHSEARCHSERVICE = _descriptor.ServiceDescriptor(
  name='GraphSearchService',
  full_name='graphsearch.GraphSearchService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=113,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='GraphSearch',
    full_name='graphsearch.GraphSearchService.GraphSearch',
    index=0,
    containing_service=None,
    input_type=_GRAPHSEARCHREQUEST,
    output_type=_GRAPHSEARCHREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRAPHSEARCHSERVICE)

DESCRIPTOR.services_by_name['GraphSearchService'] = _GRAPHSEARCHSERVICE

# @@protoc_insertion_point(module_scope)