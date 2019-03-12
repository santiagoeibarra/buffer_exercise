import pytest
from buffer import Buffer
from buffer import BufferEmpty


def test_buffer_lifo_extract():
    """
    Test function extract elements for a LIFO queue
    """
    thebuffer = Buffer(policy='LIFO')
    item_a = "Hello"
    item_b = "Old"
    item_c = "World"
    thebuffer.insert(item_a)
    thebuffer.insert(item_b)
    thebuffer.insert(item_c)
    assert thebuffer.extract() == item_c


def test_buffer_fifo_extract():
    """
    Test function extract elements for a FIFO queue
    """
    thebuffer = Buffer(policy='FIFO')
    item_a = "Hello"
    item_b = "Old"
    item_c = "World"
    thebuffer.insert(item_a)
    thebuffer.insert(item_b)
    thebuffer.insert(item_c)
    assert thebuffer.extract() == item_a


def test_buffer_fifo_insert():
    """
    Test function insert elements for a FIFO queue
    """ 
    buf = Buffer("FIFO")
    item_a = "Hola"
    item_b = " "
    item_c = "Mundo"
    buf.insert(item_a)
    buf.insert(item_b)
    buf.insert(item_c)

    assert buf.extract() == item_a
    assert buf.extract() == item_b


def test_buffer_lifo_insert():
    """
    Test function insert elements for a LIFO queue
    """     
    buf = Buffer("LIFO")
    item_a = "Hola"
    item_b = " "
    item_c = "Mundo"
    buf.insert(item_a)
    buf.insert(item_b)
    buf.insert(item_c)

    assert buf.extract() == item_c
    assert buf.extract() == item_b


def test_buffer_empty():
    buf = Buffer("FIFO")

    with pytest.raises(BufferEmpty):
        buf.extract()

def test_last_value_is_none():
    buf = Buffer("LIFO")
    item_a = "None"
    item_b = 100
    item_c = None
    buf.insert(item_a)
    buf.insert(item_b)
    buf.insert(item_c)
    assert buf.extract() is None

def test_first_value_is_none():
    buf = Buffer("FIFO")
    item_a = None
    item_b = 100
    item_c = "abc"
    buf.insert(item_a)
    buf.insert(item_b)
    buf.insert(item_c)
    assert buf.extract() is None

def test_buffer_is_not_empty():
    buf = Buffer("FIFO")
    first = "Primer elemnto"
    second = "Segundo elemento"
    buf.insert(first)
    assert len(buf) > 0


'''




path = "/algun/path/al/archivo.txt"

f = open(path, "w")
line = f.read()
f.close()

with open(path, "w") as f:
    line = f.read()

'''

