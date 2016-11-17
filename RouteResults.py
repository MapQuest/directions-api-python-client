# Python 2.7

# MapQuest Inc.

"""Provides a container to hold route results 

This class provides storage for route results and  the 
corresponding getters and setters. Consumed fields include:
    - sessionID
    - locations (list)
    - route legs (list)
    - time, realtime
    - distance
    - link IDs (for traffic reroute)
    - traffic support
"""

__author__ = 'akhil.jaggarwal@mapquest.com'

class RouteResults(object):
    # RouteResults(sessionID
    def __init__(self, sessionid=''):
        self.sessionID = sessionid 
        self.realTime = 0
        self.time = 0
        self.distance = 0
        self.locations = [] 
        self.legs = []
        self.origin = None
        self.destination = None
        self.glinksList = []
        self.shapePoints = []
        self.routeLinkCount = 0
        self.rerouteLinks = []

    def getOriginLLFromLoc(self):
        if len(self.locations) > 0:
            return self.locations[0]['latLng']

    def getDestLLFromLoc(self):
        if len(self.locations) > 0:
            return self.locations[1]['latLng'] 

    def getOriginCityFromLoc(self):
        if len(self.locations) > 0:
            return self.locations[0]['adminArea5']

    def getDestCityFromLoc(self):
        if len(self.locations) > 0:
            return self.locations[1]['adminArea5']
        
    def getOriginStreetFromLoc(self):
        if len(self.locations) > 0:
            return self.locations[0]['street']

    def getDestStreetFromLoc(self):
        if len(self.locations) > 0:
            return self.locations[1]['street']

    def getOrigStateFromLoc(self):
        if len(self.locations) > 0:
            return self.locations[0]['adminArea3']

    def getDestStateFromLoc(self):
        if len(self.locations) > 0:
            return self.locations[1]['adminArea3']

    def setRerouteLinks(self, links):
        # must have at least two links
        if len(links) > 2:
            # extract the last two link IDs
            for i in xrange(1,3):
                self.rerouteLinks.append(self.glinksList[-i]['gefID'])

    def getRerouteLinks(self):
        return self.rerouteLinks

    def setRouteLinkCount(self, count):
        self.routeLinkCount = count

    def getRouteLinkCount(self):
        return self.routeLinkCount

    def setShapePoints(self, shapes):
        self.shapePoints = shapes

    def getShapePoints(self):
        return self.shapePoints

    def setGuidanceLinks(self, links):
        self.glinksList = links
        # extract the last two linkIDs 
        # for the traffic reroute request
        self.setRerouteLinks(self.glinksList)

    def getGuidanceLinks(self):
        return self.glinksList

    def setLocations(self, locs):
        self.locations = locs

    def getLocations(self):
        return self.locations

    def setLegs(self, legs):
        self.legs = legs

    def getLegs(self):
        return self.legs

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    def setRealTime(self, realtime):
        self.realTime = realtime

    def getRealTime(self):
        return self.realTime

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setSessionID(self, sessionID):
        self.sessionID = sessionID

    def getSessionID(self):
        return self.sessionID

    def setOrigin(self, origin):
        self.origin = origin

    def setDestination(self, destination):
        self.destination = destination

