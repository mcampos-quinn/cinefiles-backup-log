#A Python script to log redundant backups of CineFiles document scans

##About [CineFiles](https://cinefiles.bampfa.berkeley.edu/cinefiles/)
CineFiles contains scanned images of reviews, press kits, festival and showcase program notes, newspaper articles, and other documents from the [PFA Library’s](http://bampfa.org/about/film-library-study-center) extensive collection covering world cinema, past and present. Citations are available for all documents, and page images are available for documents with copyright clearance. New titles and document images are added daily.

CineFiles currently includes documents on the films of more than 150 major international directors, materials describing silent Soviet cinema, and PFA's unique collection of exhibitor manuals, among other documents.

##Rationale for this script
Although UC Berkeley provides backups of all our original and derivative content, PFA has always maintained redundant backups of CineFiles master image files: first on CD, then a RAID drive. During our migration to a new web-based database, we relied on 15-year-old CD backups to reconnect over 1000 TIFF images that had gone missing during the various loads. 

We previously used a license of the proprietary iView indexing system. Our license was on a PowerPC-based Mac system, though, and we currently only have access to a text version of the data in our iView catalogs, including file name, size, MIME Type, filepath, etc. 

Our backups will as of 2016 be on a DROBO system, and we will run this script monthly using Automator to index our image backups. the backup logs will be saved to Google Drive for reference. 

###Contributors
Michael Campos-Quinn

The file size calculation came from this Stack Overflow thread:

http://stackoverflow.com/questions/14996453/python-libraries-to-calculate-human-readable-filesize-from-bytes