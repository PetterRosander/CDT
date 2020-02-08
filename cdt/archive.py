#!/usr/bin/env python

##########################################################
# Imports
##########################################################
# Python stdlibs
import tarfile as tarfile
import re as regex
import json as jsonlib
import os as os

##########################################################
# Functions
##########################################################


##########################################################
# Module entry/class
##########################################################
class Archive():
    def __init__(self, archive):
        self.archive = archive  # tarfile.open(archive, 'r:gz')

    def extract(self, folder):
        tar = tarfile.open(self.archive, 'r:gz')
        for member in tar.getmembers():
            if regex.match(r'.*' + folder, member.name):
                self.tar.extract(member, path='./out')
        tar.close()

    def append(self, folder):
        os.system('gunzip ' + self.archive)
        tar = tarfile.open(self.archive[:-3], 'a')
        tar.add(folder)
        os.system('gzip ' + self.archive[:-3])
        tar.close()

    def getIndex(self, folder):
        tar = tarfile.open(self.archive, 'r:gz')
        for member in tar.getmembers():
            if regex.match(r'.*index.json', member.name):
                index = self.tar.extractfile(member)
                content = index.read().decode('utf-8')
                self.json = content
                break
        tar.close()
        return self._json[folder]

    # dhef

    """
    Class public members with
    getters and setters
    """
    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, json):
        self._json = jsonlib.loads(json)
