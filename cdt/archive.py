#!/usr/bin/env python

##########################################################
# Imports
##########################################################
# Python stdlibs
import tarfile as tarfile
import re as regex
import json as jsonlib
import os as os
import shutil as shutil

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

    def changeIndex(self, folderInfo):
        json = self.__getIndex__()
        json.update(folderInfo)

    def append(self, folder):
        os.mkdir('cgt-build-cgt')
        os.chdir('cgt-build-cgt')
        tar = tarfile.open('../' + self.archive, 'r:gz')
        tar.extractall()
        shutil.copytree('../' + folder, './' + folder)
        tar.close()
        tar = tarfile.open('../' + self.archive, 'w:gz')
        directory = os.listdir('./')
        for folder in directory:
            tar.add(folder)
        tar.close()
        os.chdir('../')
        shutil.rmtree('cgt-build-cgt')

    def getIndex(self, folder):
        json = self.__getIndex__()
        return json[folder]

    """
    Private methods
    """
    def __getIndex__(self):
        tar = tarfile.open(self.archive, 'r:gz')
        for member in tar.getmembers():
            if regex.match(r'.*index.json', member.name):
                index = self.tar.extractfile(member)
                content = index.read().decode('utf-8')
                self.json = content
                break
        tar.close()
        return self.json

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
