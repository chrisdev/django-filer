#-*- coding: utf-8 -*-
#import zipfile
# zipfile.open() is only available in Python 2.6, so we use the future version
from django.core.files.uploadedfile import SimpleUploadedFile
from zipfile import ZipFile


def unzip(file_obj):
    """
    Take a path to a zipfile and checks if it is a valid zip file
    and returns...
    """
    files = []
    # TODO: implement try-except here
    zip = ZipFile(file_obj)
    bad_file = zip.testzip()
    if bad_file:
        raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)
    infolist = zip.infolist()
    for zipinfo in infolist:
        if zipinfo.filename.startswith('__'):  # do not process meta files
            continue
        file_obj = SimpleUploadedFile(name=zipinfo.filename, content=zip.read(zipinfo))
        files.append((file_obj, zipinfo.filename))
    zip.close()
    return files
