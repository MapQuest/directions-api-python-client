# Python 2.7

# MapQuest Inc.

__author__ = 'akhil.jaggarwal@mapquest.com'

import requests 
import json

from RouteOptions import RouteOptions

class RouteService(object):
    """Handles route requests to the MapQuest Directions API. 
    More details at http://www.mapquestapi.com/directions/
    """
    __BASE_MQAPI_URL__ = 'http://mapquestapi.com'
    __INT_MQAPI_URL__ = 'http://web-integration.mapquestapi.com'
    __BASE_POIQRY_URK__ = 'http://cdr-pqrs-int.cloud.mapquest.com/'

    __GUIDANCE__ = 'guidance/v2'
    __DIRECTIONS__ = 'directions/v2'
    __VERSION__ = 'v2'

    # Key actions
    __validate__ = 'validate'

    # Route Actions #
    __route__ = 'route'
    __alternateroutes__ = 'alternateroutes'
    __optimizedroute__ = 'optimizedroute'
    __routematrix__ = 'routematrix'
    __routeshape__ = 'routeshape'
    __pathfromroute__ = 'pathfromroute'
    __from_session__ = 'getFromSession'

    def __init__(self, key):
        """
        @param key: an API key to use with the Directions service
        @type key: string

        @param url: directions services endpoint to target
        @type: url: string
        """
        if not key:
            raise ValueError("Must provide an API key to use the\
                    Directions service.")
        if not self.validateKey(key):
            raise ValueError("Invalid API key provided")
        self.key = key

        self.request_params= None
        self.request_body = None
        self.request_headers = None
        self.payload = None

        self.directionsSessionID = None
        self.guidanceSessionID = None
        self.places = None

    def clean(self):
        self.request_params = {}
        self.request_body = {}
        self.request_headers = {}
        self.payload = {}

    def validateKey(self, key):
        payload = {'key':key}
        url = '%s/%s'%(RouteService.__BASE_MQAPI_URL__,\
                RouteService.__validate__)
        if requests.get(url, payload).status_code != 200:
            return False
        return True

    def makeRequestPayload(self, *args, **kwargs):
        """Out format: from=&to=&to=...&key=
        """


        locations = kwargs['locations']
        if 'options' in kwargs: 
            self.payload.update(kwargs['options'].getRouteOptions())

        self.payload['from'] = locations[0]

        self.payload['to'] = []
        for loc in locations[1:]:
            self.payload['to'].append(loc)

    def directions(self, *args, **kwargs):
        """does a simple directions route request and stores the 
        parsed result in a RouteResults object. origin is always
        passed as the first parameter
        
        @param: origin, destination
        @format: 'number, street, city, state'
        @format: 'city,state'
        @format: 'latitude,longitude'
 
        e.g.: "Lancaster,PA&to=York,PA"
               32.52027,-92.10313,33.435032,-112.712108

        @param: options: route options
        """
        self.payload = {}
        if not kwargs['locations']:
            raise ValueError("Request missing locations")

        self.makeRequestPayload(**kwargs)
        
        if self.payload is None:
            raise ValueError("Error preparing payload")

        return self.getRoute(RouteService.__DIRECTIONS__,\
                RouteService.__route__,\
                params=self.payload) 

    def guidanceRoute(self, *args, **kwargs):
        """does a simple guidance route request and stores the 
        parsed result in a RouteResults object
        """

        self.makeRequestPayload(**kwargs)

        return self.getRoute(RouteService.__GUIDANCE__,\
                RouteService.__route__,\
                params=self.payload)

    def alternateRoute(self, *args, **kwargs):
        """The Alternate Routes function provides an easy way to 
        request multiple potential routes between two locations.
        """
        self.payload = {}
        maxRoutes = 1
        timeOverage = 25.0 
        if 'maxRoutes' in kwargs:
            maxRoutes = kwargs['maxRoutes']
        if 'timeOverage' in kwargs:
            timeOverage = kwargs['timeOverage']

        altRouteOptions = {'maxRoutes':maxRoutes,\
                'timeOverage':timeOverage}
        self.payload.update(altRouteOptions)
        self.makeRequestPayload(**kwargs)

        return self.getRoute(RouteService.__DIRECTIONS__,\
                RouteService.__alternateroutes__,\
                params=self.payload)

    def optimizedRoute(self, **kwargs):
        """A function that allows a user to find the route with the most 
        optimized drive time / shortest distance / walking time that 
        includes all intermediate locations. The origin and destination 
        locations remain fixed, but the intermediate locations are re-ordered 
        to find the optimal path through the set of locations.
        """
        locations = self.getLocationsPayload(kwargs['locations'])

        return self.getRoute(RouteService.__DIRECTIONS__,\
                RouteService.__optimizedroute__,\
                'json=%s'%(locations))

    def routeMatrix(self, *args, **kwargs):
        """A function that allows a user to find the times and 
        distances between a set of points.
        @kwparam allToAll
        @kwparam manyToOne
        @kwparam distance
        @kwparam time
        @kwparam locations
        @kwparam info
        """
        payload = self.getLocationsPayload(kwargs['locations'])
        kwargs.pop('locations')
        if kwargs:
            payload['options'] = kwargs
        return self.getRoute(RouteService.__DIRECTIONS__,\
                RouteService.__routematrix__,\
                'json=%s'%(payload))

    def getLocationsPayload(self, locations_list):
        locations = {'locations':[]}
        for location in locations_list:
            locations['locations'].append(location)

        return locations

    def routeShape(self, *args, **kwargs):
        """ A function that allows a user to find the times and distances 
        between a set of points.
        @kwargs: mapState:{width: 320, height:240, 
                          scale:1733371, 
                          center:{lat:lat, 
                                  lng:lng}
                        }
                OR
                {'options': 'fullShape':Boolean,
                            'generalize':Boolean
                }

        """
        sessionID = str(self.directions(*args, **kwargs)['route']['sessionId'])

        if sessionID is None:
            raise ValueError('Error extracting sessionID from route request')

        payload = {'options':{}}
        payload['options']['fullShape'] = True
        payload['options']['generalize'] = True
        if 'fullShape' in kwargs:
            payload['options']['fullShape'] = kwargs['fullShape']
        if 'generalize' in kwargs:
            payload['options']['generalize'] = kwargs['generalize']

        payload['sessionId'] = sessionID

        return self.getRoute(RouteService.__DIRECTIONS__,\
                RouteService.__routeshape__,\
                'json=%s'%payload)

    def pathFromRoute(self, *args, **kwargs):
        """ The Path from Route function provides an easy method 
        for searching along the corridor defined by a route. 
        The function provides the times/distances needed to reach 
        a set of Locations from an existing route
        -> also needs generalize=decimal
        """
        payload = {}
        if 'options' not in kwargs:
            kwargs['options'] = RouteOptions()

        directions = self.directions(*args, **kwargs)
        payload['sessionId'] = str(directions['route']['sessionId'])
        points = directions['route']['shape']['shapePoints']
        points_str_list =  (','.join(str(point) for point in points))

        payload['points'] = points_str_list

        if len(payload['points']) == 0:
            raise ValueError("No shape points in directions JSON response")
        
        if 'maxTime' in kwargs and 'maxDistance' in kwargs:
            raise ValueError("Must provide one of 'maxDistance' or \
                    'maxTime'")

        if 'maxTime' in kwargs:
            payload['maxTime'] = kwargs['maxTime']
        elif 'maxDistance' in kwargs:
            payload['maxDistance'] = kwargs['maxDistance']

        return self.getRoute(RouteService.__DIRECTIONS__,\
                RouteService.__pathfromroute__,\
                payload)

    def getRoute(self, endpoint, action, params):
        url = '%s/%s/%s?key=%s'%(RouteService.__INT_MQAPI_URL__,\
                endpoint,\
                action, self.key)

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
