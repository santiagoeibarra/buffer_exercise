import pytest
from buffer import Buffer
from buffer import BufferEmpty


def test_buffer_lifo_extract():
    """
    Extract elements for a LIFO
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
    thebuffer = Buffer(policy='FIFO')
    item_a = "Hello"
    item_b = "Old"
    item_c = "World"
    thebuffer.insert(item_a)
    thebuffer.insert(item_b)
    thebuffer.insert(item_c)
    assert thebuffer.extract() == item_a


def test_buffer_fifo_insert():
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
'''




path = "/algun/path/al/archivo.txt"

f = open(path, "w")
line = f.read()
f.close()

with open(path, "w") as f:
	line = f.read()

'''

