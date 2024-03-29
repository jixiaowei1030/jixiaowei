# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Proxy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Proxy.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bProxy.proto\x12\x05proto\"\x12\n\x03\x43md\x12\x0b\n\x03\x63md\x18\x01 \x03(\t\"#\n\x06Result\x12\x0c\n\x04info\x18\x01 \x01(\t\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t2/\n\x05Proxy\x12&\n\x07\x45xecute\x12\n.proto.Cmd\x1a\r.proto.Result\"\x00\x62\x06proto3')
)




_CMD = _descriptor.Descriptor(
  name='Cmd',
  full_name='proto.Cmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='proto.Cmd.cmd', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=22,
  serialized_end=40,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='proto.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='proto.Result.info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err', full_name='proto.Result.err', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=42,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['Cmd'] = _CMD
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cmd = _reflection.GeneratedProtocolMessageType('Cmd', (_message.Message,), {
  'DESCRIPTOR' : _CMD,
  '__module__' : 'Proxy_pb2'
  # @@protoc_insertion_point(class_scope:proto.Cmd)
  })
_sym_db.RegisterMessage(Cmd)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'Proxy_pb2'
  # @@protoc_insertion_point(class_scope:proto.Result)
  })
_sym_db.RegisterMessage(Result)



_PROXY = _descriptor.ServiceDescriptor(
  name='Proxy',
  full_name='proto.Proxy',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=79,
  serialized_end=126,
  methods=[
  _descriptor.MethodDescriptor(
    name='Execute',
    full_name='proto.Proxy.Execute',
    index=0,
    containing_service=None,
    input_type=_CMD,
    output_type=_RESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROXY)

DESCRIPTOR.services_by_name['Proxy'] = _PROXY

# @@protoc_insertion_point(module_scope)
