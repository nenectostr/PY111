"""
My little Stack
"""
from typing import Any

# test temp!
st:list = []

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global st
    st.insert(0, elem)


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    global st
    if len(st) >= 1:
        res = st[0]
        del st[0]
        return res
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    global st
    if ind < len(st):
        return st[ind]
    else:
        return None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global st
    st = []
    return None

if __name__ == '__main__':
    push(6)
    clear()
    print(pop())