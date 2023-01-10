from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandReply(_message.Message):
    __slots__ = ["desc", "display_name", "name", "names", "owner", "value", "yes"]
    DESC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    YES_FIELD_NUMBER: _ClassVar[int]
    desc: str
    display_name: str
    name: str
    names: _containers.RepeatedScalarFieldContainer[str]
    owner: int
    value: Value
    yes: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., desc: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ..., names: _Optional[_Iterable[str]] = ..., yes: bool = ..., owner: _Optional[int] = ...) -> None: ...

class CommandRequest(_message.Message):
    __slots__ = ["argument", "desc", "display_name", "enums", "exception", "id", "value"]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENUMS_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    argument: str
    desc: str
    display_name: str
    enums: _containers.RepeatedCompositeFieldContainer[NamedValue]
    exception: str
    id: int
    value: Value
    def __init__(self, id: _Optional[int] = ..., display_name: _Optional[str] = ..., desc: _Optional[str] = ..., exception: _Optional[str] = ..., argument: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ..., enums: _Optional[_Iterable[_Union[NamedValue, _Mapping]]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventReply(_message.Message):
    __slots__ = ["desc", "display_name", "name", "names", "owner", "value", "yes"]
    DESC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    YES_FIELD_NUMBER: _ClassVar[int]
    desc: str
    display_name: str
    name: str
    names: _containers.RepeatedScalarFieldContainer[str]
    owner: int
    value: Value
    yes: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., desc: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ..., names: _Optional[_Iterable[str]] = ..., yes: bool = ..., owner: _Optional[int] = ...) -> None: ...

class EventRequest(_message.Message):
    __slots__ = ["argument", "desc", "display_name", "enums", "id", "time", "value"]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENUMS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    argument: str
    desc: str
    display_name: str
    enums: _containers.RepeatedCompositeFieldContainer[NamedValue]
    id: int
    time: int
    value: Value
    def __init__(self, id: _Optional[int] = ..., display_name: _Optional[str] = ..., desc: _Optional[str] = ..., time: _Optional[int] = ..., argument: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ..., enums: _Optional[_Iterable[_Union[NamedValue, _Mapping]]] = ...) -> None: ...

class NamedValue(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: Value
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...

class ObjectReply(_message.Message):
    __slots__ = ["id", "ids", "type", "yes"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    YES_FIELD_NUMBER: _ClassVar[int]
    id: int
    ids: _containers.RepeatedScalarFieldContainer[int]
    type: str
    yes: bool
    def __init__(self, id: _Optional[int] = ..., ids: _Optional[_Iterable[int]] = ..., type: _Optional[str] = ..., yes: bool = ...) -> None: ...

class ObjectRequest(_message.Message):
    __slots__ = ["id", "name", "reason", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    reason: str
    type: str
    def __init__(self, id: _Optional[int] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ParameterReply(_message.Message):
    __slots__ = ["desc", "display_name", "enums", "name", "owner", "value", "yes"]
    DESC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENUMS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    YES_FIELD_NUMBER: _ClassVar[int]
    desc: str
    display_name: str
    enums: _containers.RepeatedCompositeFieldContainer[NamedValue]
    name: str
    owner: int
    value: Value
    yes: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., desc: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ..., enums: _Optional[_Iterable[_Union[NamedValue, _Mapping]]] = ..., yes: bool = ..., owner: _Optional[int] = ...) -> None: ...

class ParameterRequest(_message.Message):
    __slots__ = ["desc", "display_name", "enum_name", "enums", "id", "value"]
    DESC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENUMS_FIELD_NUMBER: _ClassVar[int]
    ENUM_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    desc: str
    display_name: str
    enum_name: str
    enums: _containers.RepeatedCompositeFieldContainer[NamedValue]
    id: int
    value: Value
    def __init__(self, id: _Optional[int] = ..., display_name: _Optional[str] = ..., desc: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ..., enums: _Optional[_Iterable[_Union[NamedValue, _Mapping]]] = ..., enum_name: _Optional[str] = ...) -> None: ...

class StateStream(_message.Message):
    __slots__ = ["id", "maker_id", "request_id", "state"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AFTER_CREATING_OBJECT: StateStream.State
    AFTER_SETTING_PARAMETER: StateStream.State
    BEFORE_REMOVING_OBJECT: StateStream.State
    EXECUTING_COMMAND: StateStream.State
    GETTING_AVAILABLE_CHILDREN: StateStream.State
    ID_FIELD_NUMBER: _ClassVar[int]
    MAKER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    maker_id: int
    request_id: int
    state: StateStream.State
    def __init__(self, state: _Optional[_Union[StateStream.State, str]] = ..., id: _Optional[int] = ..., request_id: _Optional[int] = ..., maker_id: _Optional[int] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ["bool_value", "datetime_value", "dict_value", "double_value", "list_value", "long_value", "string_value"]
    class Dict(_message.Message):
        __slots__ = ["value"]
        class ValueEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.MessageMap[str, Value]
        def __init__(self, value: _Optional[_Mapping[str, Value]] = ...) -> None: ...
    class List(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedCompositeFieldContainer[Value]
        def __init__(self, value: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    LONG_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    datetime_value: int
    dict_value: Value.Dict
    double_value: float
    list_value: Value.List
    long_value: int
    string_value: str
    def __init__(self, bool_value: bool = ..., long_value: _Optional[int] = ..., double_value: _Optional[float] = ..., datetime_value: _Optional[int] = ..., string_value: _Optional[str] = ..., list_value: _Optional[_Union[Value.List, _Mapping]] = ..., dict_value: _Optional[_Union[Value.Dict, _Mapping]] = ...) -> None: ...
