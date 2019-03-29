#!/usr/bin/python

"""
Input Output File function
"""

import os
import sys
import tarfile
import time
if sys.version_info >= (3, 0):
	import urllib.request
else:
	import urllib

def reporthook(count, block_size, total_size):
	global start_time
	if count == 0:
		start_time = time.time()
		return
	time.sleep(0.01)
	duration = time.time() - start_time
	progress_size = int(count * block_size)
	speed = int(progress_size / (1024 * duration))
	percent = min(int(count * block_size * 100 / total_size), 100)
	sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
					(percent, progress_size / (1024 * 1024), speed, duration))
	sys.stdout.flush()

def get_size(filename):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(filename):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
	return total_size

def backup(outputname, inputname, size):
	totalsize = 0
	with tarfile.open(outputname, "w:gz") as tar:
		for file in inputname:
			filesize = os.path.getsize(file)
			tar.add(file, arcname = file.split('PasutBIG')[1])
			totalsize += filesize
			percent = min(int(100 * totalsize / size), 100)
			sys.stdout.write("\r...%d%%, %d MB" %
					(percent, totalsize / (1024 * 1024)))
			sys.stdout.flush()
	tar.close()

def save(url, filename):
	if sys.version_info >= (3, 0):
		urllib.request.urlretrieve(url, filename, reporthook)
	else:
		urllib.urlretrieve(url, filename, reporthook)
