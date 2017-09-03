import inspect
from common import *
import pyorient
import os
import json

class OrientDBDao:

    def __init__(self):
        self.client = None
        print "Calling " + str(self.__class__) + "." + currentMethodName()
        self.connect()


    def connect(self):
        self.client = pyorient.OrientDB("localhost", 2424)
        session_id = self.client.connect("root", os.environ.get("ORIENTDB_PWD"))
        # self.client.db_create('Bible', pyorient.DB_TYPE_GRAPH)
        # self.initDB()
        self.client.db_open('Bible', 'root', os.environ.get("ORIENTDB_PWD"))


    def getClient(self):
        return self.client

    def initDB(self):
        self.client.db_drop('Bible')
        self.client.db_create('Bible', pyorient.DB_TYPE_GRAPH)
        self.client.db_open('Bible', 'root', os.environ.get("ORIENTDB_PWD"))
        self.client.command('CREATE Class Text extends V')
        self.client.command('CREATE Class Concept extends V')
        self.client.command('CREATE Class Relates extends E')


    def insertTextNode(self, jsonContent):
        print "Calling " + str(self.__class__) + "." + currentMethodName()
        command = "CREATE VERTEX Text CONTENT " + json.dumps(jsonContent)
        print(command)
        cluster_id = self.client.command(command)

    def hasConcept(self, conceptID):
        return len(self.client.query("select from Concept where ConceptID = '%s'" % conceptID, 10, '*:0')) > 0

    def upsertConceptNode(self, conceptID, conceptName):
        if not self.hasConcept(conceptID):
            print "Calling " + str(self.__class__) + "." + currentMethodName()
            command = "CREATE VERTEX Concept CONTENT " + json.dumps({'ConceptID': conceptID, 'ConceptName' : conceptName})
            print(command)
            cluster_id = self.client.command(command)

    def linkConcept(self, textID, conceptID):
        self.upsertConceptNode(conceptID, conceptID)
        command = "create edge Relates from (" + \
                  ("select from Text where TextID = '%s'" % textID) + \
                    ") to (" + \
                    "select from Concept where ConceptID = '%s'" % conceptID + \
                    ")"
        print command
        edges = self.client.command(
           command
        )

    def extractEntityGod(self, text):
        return 'god' in text.lower()

    def extractEntityJesus(self, text):
        return 'jesus' in text.lower()

    def insertBibleChapter(self, book, chapter, text):
        textID = book + '-' + chapter
        self.insertTextNode({
            'BookName' : 'Bible',
            'TextID' : textID,
            'Book' : book,
            'Chapter' : chapter,
            'Text' : text})

        # Extract concepts
        if self.extractEntityGod(text):
            print 'Found God'
            self.linkConcept(textID, 'God')
        if self.extractEntityJesus(text):
            print 'Found Jesus'
            self.linkConcept(textID, 'Jesus')


    def findNode(self, id):
        result = self.client.query("select from Text where TextID = '%s'" % id, 10, '*:0')
        return result

    def listDB(self):
        print self.client.db_list()