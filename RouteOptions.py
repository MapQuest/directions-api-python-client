# Python 2.7

# MapQuest Inc.

"""Provides a container to hold route requests
"""

__author__ = 'akhil.jaggarwal@mapquest.com'

import json

class RouteOptions(object):
    """
    This class stores the options applicable to a directions or guidance 
    route request. More details at www.mapquestapi.com/directions/.
    """
    def __init__(self, sessionId=None, unit='m', routeType='fastest', 
            avoidTimedConditions='false', doReverseGeocode='true', narrativeType='text', 
            enhancedNarrative='false', maxLinkId=0, locale='en_US', generalize=1.0, avoids=None, 
            disallows=None, prefers=None, mustAvoidLinkIds=None, tryAvoidLinkIds=None, 
            stateBoundaryDisplay=None, ctryBoundaryDisplay=None, cyclingRoadFactor=None,
            roadGradeStrategy=None, drivingStyle=None, highwayEfficiency=None, 
            manMaps=None, walkingSpeed=None, fullShape=None, shapeFormat=None, 
            inShapeFormat=None, outShapeFormat=None):
        self.routeOptions = dict()

        self.key = None

        if sessionId:
            self.routeOptions['sessonId'] = sessionID
        self.routeOptions['unit'] = unit
        self.routeOptions['routeType'] = routeType
        self.routeOptions['avoidTimedConditions'] = avoidTimedConditions
        self.routeOptions['doReverseGeocode'] = doReverseGeocode
        self.routeOptions['narrativeType'] = narrativeType
        self.routeOptions['enhancedNarrative'] = enhancedNarrative
        self.routeOptions['maxLinkId'] = maxLinkId
        self.routeOptions['locale'] = locale

        
        # advanced route options
        if avoids:
            self.routeOptions['avoids'] = avoids
        if disallows:
            self.routeOptions['disallows'] = disallows
        if prefers:
            self.routeOptions['prefers'] = prefers
        if mustAvoidLinkIds:
            self.routeOptions['mustAvoidLinkIds'] = mustAvoidLinkIds
        if tryAvoidLinkIds:
            self.routeOptions['tryAvoidLinkIds'] = tryAvoidLinkIds
        if stateBoundaryDisplay:
            self.routeOptions['stateBoundaryDisplay'] = stateBoundaryDisplay
        if ctryBoundaryDisplay:
            self.routeOptions['countryBoundaryDisplay'] = countryBoundaryDisplay
        if cyclingRoadFactor:
            self.routeOptions['cyclingRoadFactor'] = cyclingRoadFactor
        if roadGradeStrategy:
            self.routeOptions['roadGradeStrategy'] = roadGradeStrategy
        if drivingStyle:
            self.routeOptions['drivingStyle'] = drivingStyle
        if highwayEfficiency:
            self.routeOptions['highwayEfficiency'] = highwayEfficiency
        if manMaps:
            self.routeOptions['manMaps'] = manMaps
        if walkingSpeed:
            self.routeOptions['walkingSpeed'] = walkingSpeed

        # route shape options
        if fullShape:
            self.routeOptions['fullShape'] = fullShape
        if shapeFormat:
            self.routeOptions['shapeFormat'] = shapeFormat
        if inShapeFormat:
            self.routeOptions['inShapeFormat'] = inShapeFormat
        if outShapeFormat:
            self.routeOptions['outShapeFormat'] = outShapeFormat
        if generalize:
            self.routeOptions['generalize'] = generalize
    
    def setKey(self, key):
        self.routeOptions['key'] = key

    def setOrigin(self, origin):
        self.routeOptions['from'] = origin
    
    def setDestination(self, destination):
        self.routeOptions['to'] = destination

    def __repr__(self):
        return str(self.routeOptions)
    
    def __str__(self):
        return str(self.routeOptions)

    def getRouteOptions(self):
        return self.routeOptions

    def getRouteOptionsJSON(self):
        return json.dumps(self.routeOptions)
