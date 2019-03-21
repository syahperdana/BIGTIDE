# BIGTIDE
<h2>Backgrounds</h2>
The Indonesian Geospatial Information Agency (BIG) announce the plan to establish sea level monitoring network after 24<sup>th</sup> December 2004 Sumatera Tsunami, which devastated the coastal area of Aceh and the surrounding countries in the Indian Ocean. While the progress on the development of the sea level monitoring network was relatively slow, BIG has 136 tide gauge stations located at all part of Indonesia (Fig. 1.) to date (2019). However, assuming that one tide gauge station represents a tidal regime of about 100 km of coast line length, an ideal number of permanent tide gauge stations for the whole country should be about 810 stations.
<p align="center">
  <img width="75%" src="/Misc/inatidemap.jpg" title="Map of Indonesia tide gauge station">
</p>
<h5 align="center"><b>Fig. 1.</b> Tide gauge stations across Indonesia</h5>

<h2>Introductions</h2>
Tide data owned by BIG is kept in the database system and is connected to Indonesia Tsunami Early Warning System (Ina-TEWS) at The Indonesian Meteorological, Climatological, and Geophysical Agency (BMKG) to some stations and also to other international institutions. The purpose of this script are for retrieving real time sea level data stored in BIG server, from last ten days. The data resolution is 150 seconds (2.5 minutes), with vertical precision of 1 cm. Periodical execution of this script will result in bigger database and longer data range (do not forget to backup the data periodically too), which mean this script will generate sea level records database along time. The output are in .csv format which contains date, time, and sea level height (Fig. 2.).
<p align="center">
  <img src="/Misc/dirtree.jpg" title="Directory structure of BIGTIDE script">
</p>
<h5 align="center"><b>Fig. 2.</b> Directory tree of BIGTIDE</h5>

<h2>Requirements</h2>
Created and tested with Python 3.6.5 (with backward compatible to >= 2.7.x), on Ubuntu 18.04 LTS. The only additional packages required are numpy (1.16.2). Do not forget to modify the MainDir variable inside main.py:<br/>

```python
print("      Real Time Observation      ")
print("     Version 1.0 by: MasBoyo     \n")

MainDir = "/root/PasutBIG/Data" # Change to your directory path where this script located

if os.path.isdir(MainDir) is False:
	os.mkdir(MainDir)
	print("\nDirectory \"" + MainDir + "\" created")
else:
```
