BIGTIDE
=======

.. image:: https://travis-ci.org/syahperdana/BIGTIDE.svg?branch=master
        :target: https://travis-ci.org/syahperdana/BIGTIDE
        :alt: Travis Build Status

.. image:: https://ci.appveyor.com/api/projects/status/m3g53jr8k443ejun/branch/master?svg=true
        :target: https://ci.appveyor.com/project/syahperdana/bigtide/branch/master
        :alt: Appveyor Build Status

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
        :target: ../master/LICENSE
        :alt: License Information

:Author: Aldwin Syahperdana
:Contact: syahperdana@gmail.com
:Date: 2019-03-21 10:23:53 +0700
:Status: Work in progress
:Revision: 01
:Version: 0.1
:Copyright:
	BIGTIDE and this documentation is:

	Copyright © 2019 Masboyo Software Foundation. All rights reserved.

.. meta::
   :keywords: reStructuredText, demonstration, demo, parser
   :description lang=en: A demonstration of the reStructuredText
       markup language, containing examples of all basic
       constructs and many advanced constructs.

.. contents:: Table of Contents

Backgrounds
-----------

The Indonesian Geospatial Information Agency (BIG) announce the plan to establish sea level monitoring network after 24 :sup:`th` December 2004 Sumatera Tsunami, which devastated the coastal area of Aceh and the surrounding countries in the Indian Ocean. While the progress on the development of the sea level monitoring network was relatively slow, BIG has 136 tide gauge stations located at all part of Indonesia (**Fig. 1.**) to date (2019). However, assuming that one tide gauge station represents a tidal regime of about 100 km of coast line length, an ideal number of permanent tide gauge stations for the whole country should be about 810 stations.

.. class:: no-web

    .. figure:: https://raw.githubusercontent.com/syahperdana/BIGTIDE/syahperdana-misc/Misc/inatidemap.jpg
        :alt: Map of Indonesia tide gauge station
        :width: 75%
        :align: center

**Fig. 1.** Tide gauge stations across Indonesia

Introductions
-------------

Tide data owned by BIG is kept in the database system and is connected to Indonesia Tsunami Early Warning System (Ina-TEWS) at The Indonesian Meteorological, Climatological, and Geophysical Agency (BMKG) to some stations and also to other international institutions. The purpose of this script are for retrieving real time sea level data stored in BIG server, from last ten days. The data resolution is 150 seconds (2.5 minutes), with vertical precision of 1 cm. Periodical execution of this script will result in bigger database and longer data range (do not forget to backup the data periodically too), which mean this script will generate sea level records database along time. The output are in .csv format which contains date, time, and sea level height (**Fig. 2.**).

.. class:: no-web

    .. figure:: https://raw.githubusercontent.com/syahperdana/BIGTIDE/syahperdana-misc/Misc/dirtree.jpg
        :alt: Directory structure of BIGTIDE script
        :width: 100%
        :align: center

**Fig. 2.** Directory tree of BIGTIDE

Requirements
------------

Created and tested with Python 3.6.5 (with backward compatible to >= 2.7.x), on Ubuntu 18.04 LTS. The only additional packages required are numpy (1.16.2). Do not forget to modify the :literal:`MainDir` variable inside `main.py <https://github.com/syahperdana/BIGTIDE/blob/0d720846a8952b797bf89e992d938517bc918f91/main.py#L68>`__:

.. code-block:: python

	print("      Real Time Observation      ")
	print("     Version 1.0 by: MasBoyo     \n")
	
	MainDir = "/root/PasutBIG/Data" # Change to your directory path where this script located
	
	if os.path.isdir(MainDir) is False:
		os.mkdir(MainDir)
		print("\nDirectory \"" + MainDir + "\" created")
	else:

*Update:*
- Also runs on Termux (tested on Android 9.0 Pie)
