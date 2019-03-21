import os
import glob
import csv
import sys
import time
if sys.version_info >= (3, 0):
	import urllib.request
else:
	import urllib
import numpy as np
from collections import OrderedDict

if not getattr(__builtins__, "WindowsError", None):
    class WindowsError(OSError): pass

def reporthook(count, block_size, total_size):
	global start_time
	if count == 0:
		start_time = time.time()
		return
	time.sleep(0.01)
	duration = time.time() - start_time
	progress_size = int(count * block_size)
	speed = int(progress_size / (1024 * duration))
	percent = min(int(count*block_size*100/total_size),100)
	sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
					(percent, progress_size / (1024 * 1024), speed, duration))
	sys.stdout.flush()

def getsecondrow(filename):
	with open(filename, 'r') as f:
		for row, line in enumerate(f):
			if row == 1:
				secondrow = line.split(",")
				break
		return secondrow

def getlastrow(filename):
	with open(filename, 'r') as f:
		lastrow = None
		for lastrow in csv.reader(f): pass
		return lastrow

def save(url, filename):
	if sys.version_info >= (3, 0):
		urllib.request.urlretrieve(url, filename, reporthook)
	else:
		urllib.urlretrieve(url, filename, reporthook)

def savedb(filename):
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		firstrow = next(reader)
	lastrow = getlastrow(filename)
	filerename = firstrow[0].replace('/', r'').replace(' ', r'Z').replace(':', r'') + "-" + lastrow[0].replace('/', r'').replace(' ', r'Z').replace(':', r'') + ".csv"
	return filerename

def savedbf(filename):
	secondrow = getsecondrow(filename)
	lastrow = getlastrow(filename)
	filerename = secondrow[0].replace('/', r'').replace(' ', r'Z').replace(':', r'') + "-" + lastrow[0].replace('/', r'').replace(' ', r'Z').replace(':', r'') + ".csv"
	return filerename

print("\nIndonesian Tidal Station Database")
print("      Real Time Observation      ")
print("     Version 1.0 by: MasBoyo     \n")
	
MainDir = "/root/PasutBIG/Data" # Change to your directory path where this script located

if os.path.isdir(MainDir) is False:
	os.mkdir(MainDir)
	print("\nDirectory \"" + MainDir + "\" created")
else:
	print("\nDirectory \"" + MainDir + "\" already existed")

Results = []
with open("PasutBIG.csv") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		Results.append(row)
npResults = np.array(Results)

Province = []
for row in range(len(npResults)):
	Province.append(npResults[row][1])

uProvince = OrderedDict()
for row in Province:
	uProvince[row] = True

Pos = [2,3,4]
for row in range(len(uProvince)):
	SelectProvince = list(uProvince.items())[row][0]
	ProvDir = os.path.join(MainDir, SelectProvince)
	if os.path.isdir(ProvDir) is False:
		os.mkdir(ProvDir)
		print("\nDirectory \"" + ProvDir + "\" created")
	else:
		print("\nDirectory \"" + ProvDir + "\" already existed")
	Group = []
	for raw in range(len(Results)):
		if Results[raw][1] == SelectProvince:
			Group.append(npResults[raw][Pos])
			StationDir = os.path.join(ProvDir, npResults[raw][2])

			if os.path.isdir(StationDir) is False:
				os.mkdir(StationDir)
				print("Directory \"" + StationDir + "\" created")
			else:
				print("Directory \"" + StationDir + "\" already existed")

			TideData = os.path.join(StationDir, "temp.csv")
			save(npResults[raw][4], TideData)
			print(" | Station " + npResults[raw][2] + " data downloaded")
			TideDataRename = os.path.join(StationDir, savedb(TideData))

			try:
				os.rename(TideData, TideDataRename)
			except WindowsError as e:
				print("File \"" + TideDataRename + "\" already existed")
				os.remove(TideData)

			with open(TideDataRename) as f:
				reader = csv.reader(f, delimiter = ',')
				nColumn = len(next(reader))
				Header = ""
				for col in range(nColumn):
					if col == 0:
						Header += "Col" + str(col)
					else:
						Header += ",Col" + str(col)
				Header += "\n"

			r = open(TideDataRename, "r")
			oline = r.readlines()
			oline.insert(0,Header)
			r.close()
			r = open(TideDataRename, "w")
			r.writelines(oline)
			r.close()

			delimiter = ','
			csvs = glob.glob(os.path.join(StationDir, '*.csv'))
			TideMerge = os.path.join(StationDir, 'merged_data.csv')
			if sys.version_info >= (3, 0):
				f = open(TideMerge, "w", newline = "")
			else:
				f = open(TideMerge, 'wb')
			master_csv = csv.writer(f)
			first_csv = open(csvs[0], 'rb')
			if sys.version_info >= (3, 0):
				headers = first_csv.readline().decode().strip().split(delimiter)
			else:
				headers = first_csv.readline().strip().split(delimiter)
			master_csv.writerow(headers)

			for line in first_csv:
				if sys.version_info >= (3, 0):
					master_csv.writerow(line.decode().strip().split(delimiter))
				else:
					master_csv.writerow(line.strip().split(delimiter))
			first_csv.close()
			os.remove(csvs[0])

			for file in csvs[1:]:
				current_csv = open(file, 'rb')
				for line_num, line in enumerate(current_csv):
					if line_num > 0:
						if sys.version_info >= (3, 0):
							master_csv.writerow(line.decode().strip().split(delimiter))
						else:
							master_csv.writerow(line.strip().split(delimiter))
				current_csv.close()
				os.remove(file)
			f.close()

			rows = open(TideMerge).read().split('\n')
			newrows = []
			for row in rows:
				if row not in newrows:
					newrows.append(row)
			os.remove(TideMerge)
			TideFilter = os.path.join(StationDir, 'filtered_data.csv')
			f = open(TideFilter, 'w')
			f.write('\n'.join(newrows))
			f.close()

			FinalDataRename = os.path.join(StationDir, savedbf(TideFilter))
			try:
				os.rename(TideFilter, FinalDataRename)
			except WindowsError as e:
				print("File \"" + FinalDataRename + "\" already existed")
				os.remove(TideFilter)

print("\nProcess complete!")
