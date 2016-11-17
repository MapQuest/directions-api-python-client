# directions-api-python-client

Simple Python client to call MapQuest's Directions API. Supported operations:

1) Route:
The core and most basic function of our Directions API. Route provides information on how to get from point A to point B, or points C, D and E. Quite simply, it shows you and your users how to get where they are going.

2) AlternateRoute:
The Alternate Routes function allows users to request multiple potential routes between two locations.

3) OptimizedRoute:
The Optimized Route function allows users to customize their route experience to their preferences, including the quickest drive time, the shortest drive distance, or even how long it would take to walk instead of driving. The origin and destination locations remain fixed, but the route is ordered to find the optimal path.

4) RouteMatrix:
The Route Matrix function enables the user to see the times and distance between locations. Want to know how many miles it is between Denver and Chicago? Need to know how long it will take to drive from your home/office to a store? Route matrix provides this information.

5) RouteShape:
The Route Shape function provides a visual indicator (a shape) of a previously requested route between any number of points. Generally, this is a line leading from location to location.

6) PathFromRoute:
The Path from Route function provides the times/distances needed to reach a set of locations from an existing route.

7) FromSession:
The FromSession function fetches a previously computed route given a session ID.

# Complete documentation at: https://developer.mapquest.com/documentation/directions-api/

Example:

```python
from RouteOptions import RouteOptions
from AdvancedRouteOptions import AdvancedRouteOptions
from RouteShapeOptions import RouteShapeOptions
from RouteService import RouteService

if __name__ == '__main__':
    options = RouteOptions()
    service = RouteService('YOUR_MAPQUEST_DEVELOPER_API_KEY')

    location_list = ['Lancaster, PA', 'York, PA']
    multi_location_list = ['Lancaster, PA', 'State College, PA', 'York, PA']

    # directions
    dirRoute1 = service.directions(locations=['Lancaster, PA', 'York, PA'])

    dirRoute2 = service.directions(locations=['Lancaster, PA', 'York, PA'], options=options)

    dirRoute3 = service.directions(locations=location_list)
    multiDirRoute = service.directions(locations=multi_location_list, options=options)

    # guidance
    guidRoute = service.guidanceRoute(locations=['Lancaster,PA', 'York,PA'])
    
    # alternate route
    altRoute = service.alternateRoute(locations=['Lancaster, PA', 'York, PA'])
    altRouteWithOptions = service.alternateRoute(locations=['Lancaster, PA', 'York, PA'], maxRoutes=2, timeOverage=26)
    
    altRouteWithDefaultOptions = service.alternateRoute(locations=locations, options=options)
    altRouteWithDefaultAndCustomOpts = service.alternateRoute(locations=locations, maxRoutes=2, timeOverage=26, options=options)

    # optimized route
    optRoute = service.optimizedRoute(locations=locations3)
    optRouteWithOptions = service.optimizedRoute(locations=locations, options=options)

    # route matrix
    routeMatrix = service.routeMatrix(locations=locations,allToAll=True)

    # route shape
    routeShape = service.routeShape(locations=locations, fullShape=True)

    # path from route
    pathFromRoute = service.pathFromRoute(locations=locations, maxTime=5)
```
