import pytest

import ccsv

def test_second_row():
	assert(ccsv.getsecondrow('test2.csv') == ['2019/03/11 13:23:00','0000.70','0000.68'])

def test_last_row():
	assert(ccsv.getlastrow('test2.csv') == ['2019/03/28 14:00:00','0000.69','0000.64'])

def test_save_db():
	assert(ccsv.savedb('test1.csv') == "20190311Z132300-20190328Z140000.csv")

def test_save_dbf():
	assert(ccsv.savedbf('test2.csv') == "20190311Z132300-20190328Z140000.csv")
