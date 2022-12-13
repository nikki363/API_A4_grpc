from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

AVAILABLE: StatusType
COMEDY: GenreType
DESCRIPTOR: _descriptor.FileDescriptor
HORROR: GenreType
ROMANCE: GenreType
TAKEN: StatusType
THRILLER: GenreType

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "publishingYear", "title", "type"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    author: str
    publishingYear: int
    title: str
    type: GenreType
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., type: _Optional[_Union[GenreType, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: Book
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["book", "message"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    book: Book
    message: str
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book", "message"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    book: Book
    message: str
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["InventoryNumber", "book", "type"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    InventoryNumber: int
    TYPE_FIELD_NUMBER: _ClassVar[int]
    book: Book
    type: StatusType
    def __init__(self, InventoryNumber: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., type: _Optional[_Union[StatusType, str]] = ...) -> None: ...

class GenreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class StatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
