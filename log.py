#!/usr/bin/env python

import os, os.path, time, urllib, mimetypes, csv, datetime

fileNames = ["File Name"]
fileSize = ["File Size"]
imageMIME = ["MIME Type"]
lastModified = ["Last Modified"]
imageFilePaths = ["File Path"]

today = str(datetime.date.today())
backup_dir = raw_input("directory to back up: ")

# this file size calc came from:
# http://stackoverflow.com/questions/14996453/python-libraries-to-calculate-human-readable-filesize-from-bytes
suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    if nbytes == 0: return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

for root, dirs, files in os.walk(backup_dir):
  for ifile in files:
    if ifile.endswith((".jpg",".tiff",".tif")):
        path = os.path.join(root, ifile)
        rawSize = os.path.getsize(path)
        easySize = humansize(rawSize)
        fileNames.append(ifile)
        fileSize.append(easySize)
        imageFilePaths.append(path)
        lastModified.append(time.ctime(os.path.getmtime(path))) #note to self: add "last modified: "?
        url = urllib.pathname2url(path)
        imageMIME.append(mimetypes.guess_type(url)[0])

rows = zip(fileNames,fileSize,imageMIME,lastModified,imageFilePaths)
with open("Desktop/cinefiles-backup-log_"+today+".csv", "wb")as bu:
    writer = csv.writer(bu)
    for row in rows:
        writer.writerow(row)

# print(imageFilePaths)
# print(lastModified)
# print(imageMIME)
# print(fileNames)
# print(fileSize)