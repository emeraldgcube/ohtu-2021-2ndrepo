from urllib import request
from project import Project
import pytoml as toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        sanakirja=toml.loads(content)
        
        return Project(sanakirja["tool"]["poetry"]["name"], sanakirja["tool"]["poetry"]["description"], sanakirja["tool"]["poetry"]["dependencies"], sanakirja["tool"]["poetry"]["dev-dependencies"])
