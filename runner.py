#!/usr/bin/env python

"""
    Example of using Directions API
"""

from RouteOptions import RouteOptions
from AdvancedRouteOptions import AdvancedRouteOptions
from RouteShapeOptions import RouteShapeOptions
from RouteService import RouteService

if __name__ == '__main__':
    options = RouteOptions()
    service = RouteService('YOUR-MAPQUEST-DEVELOPER-API-KEY')

    locations = ['Lancaster, PA', 'York, PA']
    locations3 = ['Lancaster, PA', 'York, PA', 'State College, PA']
    
    # get a simple route
    route = service.directions(locations=['Lancaster, PA', 'York, PA'])
    
    routeWithOptions = service.directions(locations=['Lancaster, PA', 'York, PA'], options=options)
