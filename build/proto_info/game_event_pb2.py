# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game_event.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game_event.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10game_event.proto\"\x9e\x06\n\x16SSL_Referee_Game_Event\x12<\n\rgameEventType\x18\x01 \x02(\x0e\x32%.SSL_Referee_Game_Event.GameEventType\x12\x36\n\noriginator\x18\x02 \x01(\x0b\x32\".SSL_Referee_Game_Event.Originator\x12\x0f\n\x07message\x18\x03 \x01(\t\x1aG\n\nOriginator\x12*\n\x04team\x18\x01 \x02(\x0e\x32\x1c.SSL_Referee_Game_Event.Team\x12\r\n\x05\x62otId\x18\x02 \x01(\r\"\xf9\x03\n\rGameEventType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43USTOM\x10\x01\x12\x15\n\x11NUMBER_OF_PLAYERS\x10\x02\x12\x13\n\x0f\x42\x41LL_LEFT_FIELD\x10\x03\x12\x08\n\x04GOAL\x10\x04\x12\x10\n\x0cKICK_TIMEOUT\x10\x05\x12\x17\n\x13NO_PROGRESS_IN_GAME\x10\x06\x12\x11\n\rBOT_COLLISION\x10\x07\x12\x15\n\x11MULTIPLE_DEFENDER\x10\x08\x12\x1f\n\x1bMULTIPLE_DEFENDER_PARTIALLY\x10\t\x12\x1c\n\x18\x41TTACKER_IN_DEFENSE_AREA\x10\n\x12\t\n\x05ICING\x10\x0b\x12\x0e\n\nBALL_SPEED\x10\x0c\x12\x14\n\x10ROBOT_STOP_SPEED\x10\r\x12\x12\n\x0e\x42\x41LL_DRIBBLING\x10\x0e\x12\x19\n\x15\x41TTACKER_TOUCH_KEEPER\x10\x0f\x12\x10\n\x0c\x44OUBLE_TOUCH\x10\x10\x12\x1c\n\x18\x41TTACKER_TO_DEFENCE_AREA\x10\x11\x12#\n\x1f\x44\x45\x46\x45NDER_TO_KICK_POINT_DISTANCE\x10\x12\x12\x10\n\x0c\x42\x41LL_HOLDING\x10\x13\x12\x11\n\rINDIRECT_GOAL\x10\x14\x12\x19\n\x15\x42\x41LL_PLACEMENT_FAILED\x10\x15\x12\x10\n\x0c\x43HIP_ON_GOAL\x10\x16\"8\n\x04Team\x12\x10\n\x0cTEAM_UNKNOWN\x10\x00\x12\x0f\n\x0bTEAM_YELLOW\x10\x01\x12\r\n\tTEAM_BLUE\x10\x02'
)



_SSL_REFEREE_GAME_EVENT_GAMEEVENTTYPE = _descriptor.EnumDescriptor(
  name='GameEventType',
  full_name='SSL_Referee_Game_Event.GameEventType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NUMBER_OF_PLAYERS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BALL_LEFT_FIELD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOAL', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KICK_TIMEOUT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_PROGRESS_IN_GAME', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOT_COLLISION', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_DEFENDER', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_DEFENDER_PARTIALLY', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ATTACKER_IN_DEFENSE_AREA', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ICING', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BALL_SPEED', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_STOP_SPEED', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BALL_DRIBBLING', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ATTACKER_TOUCH_KEEPER', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_TOUCH', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ATTACKER_TO_DEFENCE_AREA', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEFENDER_TO_KICK_POINT_DISTANCE', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BALL_HOLDING', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INDIRECT_GOAL', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BALL_PLACEMENT_FAILED', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHIP_ON_GOAL', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=256,
  serialized_end=761,
)
_sym_db.RegisterEnumDescriptor(_SSL_REFEREE_GAME_EVENT_GAMEEVENTTYPE)

_SSL_REFEREE_GAME_EVENT_TEAM = _descriptor.EnumDescriptor(
  name='Team',
  full_name='SSL_Referee_Game_Event.Team',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEAM_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEAM_YELLOW', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEAM_BLUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=763,
  serialized_end=819,
)
_sym_db.RegisterEnumDescriptor(_SSL_REFEREE_GAME_EVENT_TEAM)


_SSL_REFEREE_GAME_EVENT_ORIGINATOR = _descriptor.Descriptor(
  name='Originator',
  full_name='SSL_Referee_Game_Event.Originator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='team', full_name='SSL_Referee_Game_Event.Originator.team', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='botId', full_name='SSL_Referee_Game_Event.Originator.botId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=253,
)

_SSL_REFEREE_GAME_EVENT = _descriptor.Descriptor(
  name='SSL_Referee_Game_Event',
  full_name='SSL_Referee_Game_Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameEventType', full_name='SSL_Referee_Game_Event.gameEventType', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='originator', full_name='SSL_Referee_Game_Event.originator', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='SSL_Referee_Game_Event.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SSL_REFEREE_GAME_EVENT_ORIGINATOR, ],
  enum_types=[
    _SSL_REFEREE_GAME_EVENT_GAMEEVENTTYPE,
    _SSL_REFEREE_GAME_EVENT_TEAM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=819,
)

_SSL_REFEREE_GAME_EVENT_ORIGINATOR.fields_by_name['team'].enum_type = _SSL_REFEREE_GAME_EVENT_TEAM
_SSL_REFEREE_GAME_EVENT_ORIGINATOR.containing_type = _SSL_REFEREE_GAME_EVENT
_SSL_REFEREE_GAME_EVENT.fields_by_name['gameEventType'].enum_type = _SSL_REFEREE_GAME_EVENT_GAMEEVENTTYPE
_SSL_REFEREE_GAME_EVENT.fields_by_name['originator'].message_type = _SSL_REFEREE_GAME_EVENT_ORIGINATOR
_SSL_REFEREE_GAME_EVENT_GAMEEVENTTYPE.containing_type = _SSL_REFEREE_GAME_EVENT
_SSL_REFEREE_GAME_EVENT_TEAM.containing_type = _SSL_REFEREE_GAME_EVENT
DESCRIPTOR.message_types_by_name['SSL_Referee_Game_Event'] = _SSL_REFEREE_GAME_EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SSL_Referee_Game_Event = _reflection.GeneratedProtocolMessageType('SSL_Referee_Game_Event', (_message.Message,), {

  'Originator' : _reflection.GeneratedProtocolMessageType('Originator', (_message.Message,), {
    'DESCRIPTOR' : _SSL_REFEREE_GAME_EVENT_ORIGINATOR,
    '__module__' : 'game_event_pb2'
    # @@protoc_insertion_point(class_scope:SSL_Referee_Game_Event.Originator)
    })
  ,
  'DESCRIPTOR' : _SSL_REFEREE_GAME_EVENT,
  '__module__' : 'game_event_pb2'
  # @@protoc_insertion_point(class_scope:SSL_Referee_Game_Event)
  })
_sym_db.RegisterMessage(SSL_Referee_Game_Event)
_sym_db.RegisterMessage(SSL_Referee_Game_Event.Originator)


# @@protoc_insertion_point(module_scope)