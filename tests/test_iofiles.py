import pytest

from PasutBIG.iofile import backup, get_size, save

def test_backup():
	assert(backup('./PasutBIG/test.tar.gz', ['./PasutBIG/iofile.py', './tests/libcsv.py'], 1000) == 'test.tar.gz')

def test_get_size():
	assert(get_size('./tests/test1.csv') == 1000)

def test_save():
	save('http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js', './tests/jquery.min.js').read()
