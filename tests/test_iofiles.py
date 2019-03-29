import pytest

from PasutBIG.iofile import backup, get_size, save

def test_get_size():
	assert(get_size('./tests') <= 711696)
