import enum


class MESSAGE(str, enum.Enum):
    empty = "Linked list is empty."
    notPresent = " index is not present in the linked list."
    outOfBound = "Index is out of bound."
    targetIdxNotFound = "Node with idx '%s' not found"
    targetDataNotFound = "Node with data '%s' not found"
