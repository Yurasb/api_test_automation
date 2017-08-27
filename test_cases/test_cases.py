# -*- coding: utf-8 -*-


class Case(object):
    def __init__(
            self, parameters, status_code, headers, body
    ):
        self.url_parametes = parameters
        self.expected_status_code = status_code
        self.expected_headers = headers
        self.expected_body = body


valid_case = Case(
    parameters=u'/map?bbox='
               u'27.61649608612061,53.85379229563698,'
               u'27.671985626220707,53.886459293813054',
    status_code=200,
    headers={
        'Cache-Control': 'private, max-age=0, must-revalidate',
        'Transfer-Encoding': 'chunked',
        'Keep-Alive': 'timeout=5, max=100',
        'Content-Disposition': 'attachment; filename="map.osm"',
        'Content-Type': 'text/xml; charset=utf-8',
        'Server': 'Apache/2.4.18 (Ubuntu)',
        'Connection': 'Keep-Alive',
        'Content-Encoding': 'gzip',
        'Date': 'Sun, 20 Aug 2017 20:29:37 GMT'
    },
    xsd=open('../test_cases/valid_case.xsd', 'r')
)

invalid_case_1 = Case(
    parameters=u'/map?bbox=',
    status_code=400,
    headers={
        'Content-Length': '88',
        'Cache-Control': 'no-cache',
        'Server': 'Apache/2.4.18 (Ubuntu)',
        'Connection': 'close',
        'Error': 'The parameter bbox is required, and must be '
                 'of the form min_lon,min_lat,max_lon,max_lat.',
        'Date': 'Mon, 21 Aug 2017 20:05:34 GMT',
        'Content-Type': 'text/plain; charset=utf-8'
    },
    body='The parameter bbox is required, and must be of'
         ' the form min_lon,min_lat,max_lon,max_lat.'
)

invalid_case_2 = Case(
    parameters=u'/map?bbox=27.,53.85379229563698,'
               u'27.671985626220707,53.886459293813054',
    status_code=400,
    headers={
        'Content-Length': '95',
        'Content-Disposition': 'attachment; filename="map.osm"',
        'Cache-Control': 'no-cache',
        'Server': 'Apache/2.4.18 (Ubuntu)',
        'Connection': 'close',
        'Error': 'You requested too many nodes (limit is 50000).'
                 ' Either request a smaller area, or use planet.osm',
        'Date': 'Mon, 21 Aug 2017 20:12:22 GMT',
        'Content-Type': 'text/plain; charset=utf-8'
    },
    body='You requested too many nodes (limit is 50000).'
         ' Either request a smaller area, or use planet.osm'
)

invalid_case_3 = Case(
    parameters=u'/map?bbox='
               u'100.61649608612061,53.85379229563698,'
               u'27.671985626220707,53.886459293813054',
    status_code=400,
    headers={
        'Content-Length': '118',
        'Cache-Control': 'no-cache',
        'Server': 'Apache/2.4.18 (Ubuntu)',
        'Connection': 'close',
        'Error': 'The latitudes must be between -90 and 90,'
                 ' longitudes between -180 and 180 and the minima must be less than the maxima.',
        'Date': 'Mon, 21 Aug 2017 20:16:55 GMT',
        'Content-Type': 'text/plain; charset=utf-8'
    },
    body='The latitudes must be between -90 and 90,'
         ' longitudes between -180 and 180 and the minima must be less than the maxima.'
)

invalid_case_4 = Case(
    parameters=u'/map?bbox='
               u'27.61649608612061,53.85379229563698,'
               u'27.671985626220707,52.886459293813054',
    status_code=400,
    headers={
        'Content-Length': '118',
        'Cache-Control': 'no-cache',
        'Server': 'Apache/2.4.18 (Ubuntu)',
        'Connection': 'close',
        'Error': 'The latitudes must be between -90 and 90,'
                 ' longitudes between -180 and 180 and the minima must be less than the maxima.',
        'Date': 'Mon, 21 Aug 2017 20:16:55 GMT',
        'Content-Type': 'text/plain; charset=utf-8'
    },
    body='The latitudes must be between -90 and 90,'
         ' longitudes between -180 and 180 and the minima must be less than the maxima.'
)

invalid_case_5 = Case(
    parameters=u'',
    status_code=404,
    headers={
        'Status': '404 Not Found',
        'X-Request-Id': 'WZsI38AAQEAADVtVxEAAAKv',
        'X-XSS-Protection': '1; mode=block',
        'X-Content-Type-Options': 'nosniff',
        'X-Download-Options': 'noopen',
        'X-Powered-By': 'Phusion Passenger 5.1.7',
        'Keep-Alive': 'timeout=5, max=100',
        'Connection': 'Keep-Alive',
        'Content-Length': '623',
        'Server': 'Apache/2.4.18 (Ubuntu)',
        'X-Runtime': '0.003807',
        'X-Permitted-Cross-Domain-Policies': 'none',
        'Date': 'Mon, 21 Aug 2017 20:10:11 GMT',
        'X-Frame-Options': 'sameorigin',
        'Content-Type': 'text/html; charset=utf-8'
    },
    body='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n'
         '   "http://www.w3.org/TR/html4/loose.dtd">\n'
         '<html>\n'
         '<body>\n'
         '  <img src="/assets/osm_logo.png" style="float:left; margin:10px">\n'
         '  <div style="float:left;">\n'
         '    <h1>File not found</h1>  \n'
         '    <p>Couldn\'t find a file/directory/API operation by that name on the OpenStreetMap server (HTTP 404)</p>\n'
         '    <p>Feel free to <a href="http://wiki.openstreetmap.org/wiki/Contact" title="Various contact channels explained">contact</a> the OpenStreetMap community if you have found a broken link / bug. Make a note of the exact URL of your request.</p>\n'
         '  </div>\n'
         '</body>\n'
         '</html>\n'
)

test_cases = [valid_case, invalid_case_1, invalid_case_2, invalid_case_3, invalid_case_4, invalid_case_5]


def get_case(index):
    return test_cases[index]
