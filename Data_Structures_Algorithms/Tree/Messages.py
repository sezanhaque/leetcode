import enum


class MESSAGE(str, enum.Enum):
    empty = "List is empty."
    notPresent = " index is not present in the list."
    outOfBound = "Index is out of bound."
    targetIdxNotFound = "Node with idx '%s' not found"
    targetDataNotFound = "Node with data '%s' not found"
