# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='meal.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\nmeal.proto\"\xd5\x02\n\x04Meal\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x16\n\x0e\x61lternate_name\x18\x02 \x01(\t\x12\x1d\n\x04item\x18\x04 \x03(\x0b\x32\x0f.Meal.MealItems\x12\x1f\n\x05\x64rink\x18\x05 \x03(\x0b\x32\x10.Meal.DrinkItems\x1aH\n\tMealItems\x12\x11\n\titem_name\x18\x01 \x02(\t\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x0e.Meal.FoodType:\nINGREDIENT\x1a?\n\nDrinkItems\x12\x12\n\ndrink_name\x18\x01 \x02(\t\x12\x1d\n\x04type\x18\x02 \x01(\x0e\x32\x0f.Meal.DrinkType\"4\n\x08\x46oodType\x12\x0e\n\nINGREDIENT\x10\x00\x12\x0b\n\x07\x46ILLING\x10\x01\x12\x0b\n\x07TOPPING\x10\x02\"&\n\tDrinkType\x12\n\n\x06\x42UBBLY\x10\x00\x12\r\n\tALCOHOLIC\x10\x01')
)



_MEAL_FOODTYPE = _descriptor.EnumDescriptor(
  name='FoodType',
  full_name='Meal.FoodType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INGREDIENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILLING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOPPING', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=264,
  serialized_end=316,
)
_sym_db.RegisterEnumDescriptor(_MEAL_FOODTYPE)

_MEAL_DRINKTYPE = _descriptor.EnumDescriptor(
  name='DrinkType',
  full_name='Meal.DrinkType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUBBLY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALCOHOLIC', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=318,
  serialized_end=356,
)
_sym_db.RegisterEnumDescriptor(_MEAL_DRINKTYPE)


_MEAL_MEALITEMS = _descriptor.Descriptor(
  name='MealItems',
  full_name='Meal.MealItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_name', full_name='Meal.MealItems.item_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Meal.MealItems.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=197,
)

_MEAL_DRINKITEMS = _descriptor.Descriptor(
  name='DrinkItems',
  full_name='Meal.DrinkItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drink_name', full_name='Meal.DrinkItems.drink_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Meal.DrinkItems.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=262,
)

_MEAL = _descriptor.Descriptor(
  name='Meal',
  full_name='Meal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Meal.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alternate_name', full_name='Meal.alternate_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item', full_name='Meal.item', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drink', full_name='Meal.drink', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MEAL_MEALITEMS, _MEAL_DRINKITEMS, ],
  enum_types=[
    _MEAL_FOODTYPE,
    _MEAL_DRINKTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=356,
)

_MEAL_MEALITEMS.fields_by_name['type'].enum_type = _MEAL_FOODTYPE
_MEAL_MEALITEMS.containing_type = _MEAL
_MEAL_DRINKITEMS.fields_by_name['type'].enum_type = _MEAL_DRINKTYPE
_MEAL_DRINKITEMS.containing_type = _MEAL
_MEAL.fields_by_name['item'].message_type = _MEAL_MEALITEMS
_MEAL.fields_by_name['drink'].message_type = _MEAL_DRINKITEMS
_MEAL_FOODTYPE.containing_type = _MEAL
_MEAL_DRINKTYPE.containing_type = _MEAL
DESCRIPTOR.message_types_by_name['Meal'] = _MEAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Meal = _reflection.GeneratedProtocolMessageType('Meal', (_message.Message,), dict(

  MealItems = _reflection.GeneratedProtocolMessageType('MealItems', (_message.Message,), dict(
    DESCRIPTOR = _MEAL_MEALITEMS,
    __module__ = 'meal_pb2'
    # @@protoc_insertion_point(class_scope:Meal.MealItems)
    ))
  ,

  DrinkItems = _reflection.GeneratedProtocolMessageType('DrinkItems', (_message.Message,), dict(
    DESCRIPTOR = _MEAL_DRINKITEMS,
    __module__ = 'meal_pb2'
    # @@protoc_insertion_point(class_scope:Meal.DrinkItems)
    ))
  ,
  DESCRIPTOR = _MEAL,
  __module__ = 'meal_pb2'
  # @@protoc_insertion_point(class_scope:Meal)
  ))
_sym_db.RegisterMessage(Meal)
_sym_db.RegisterMessage(Meal.MealItems)
_sym_db.RegisterMessage(Meal.DrinkItems)


# @@protoc_insertion_point(module_scope)
