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
        'X-GitHub-Request-Id': '8336:3EF8:23C1B80:32B2853:594AC437',
        'Date': 'Wed, 21 Jun 2017 19:08:39 GMT',
        'Expires': 'Wed, 21 Jun 2017 19:18:39 GMT',
        'Content-Encoding': 'gzip', 'Cache-Control': 'max-age=600',
        'Last-Modified': 'Tue, 13 Jun 2017 19:37:33 GMT',
        'Server': 'GitHub.com',
        'Content-Type': 'text/html; charset=utf-8',
        'Access-Control-Allow-Origin': '*',
        'Transfer-Encoding': 'chunked'
    },
    body='<!DOCTYPE html>\n'
         '<html>\n'
         '<head>\n'
         '  <meta charset=\'utf-8\'>\n'
         '  <meta http-equiv=\'X-UA-Compatible\' content=\'IE=Edge\'>\n'
         '  <link href=\'lib/mapbox.js/latest/mapbox.css\' rel=\'stylesheet\' />\n'
         '  <link rel=\'stylesheet\' href=\'css/font-awesome/css/font-awesome.min.css\'>\n'
         '  <link rel=\'stylesheet\' href=\'css/fonts/mplus.css\'>\n'
         '  <title>geojson.io</title>\n'
         '  <link href=\'lib/draw/leaflet.draw.css\' rel=\'stylesheet\' />\n'
         '  <link href=\'lib/codemirror/lib/codemirror.css\' rel=\'stylesheet\' />\n'
         '  <link href=\'css/base.css\' rel=\'stylesheet\' />\n'
         '  <link href=\'css/marker.css\' rel=\'stylesheet\' />\n'
         '  <link href=\'css/github_browse.css\' rel=\'stylesheet\' />\n'
         '  <link href=\'css/site.css\' rel=\'stylesheet\' />\n'
         '  <link href=\'css/theme.css\' rel=\'stylesheet\' />\n'
         '  <link rel=\'icon\' type=\'image/x-icon\' href=\'/img/favicon.png\' />\n'
         '  <meta name=\'author\' content=\'MapBox\' />\n'
         '  <meta name=\'description\' content=\'simply edit geojson map data\' />\n'
         '  <meta property=\'og:site_name\' content=\'geojson.io\'/>\n'
         '  <meta name=\'viewport\' content=\'initial-scale=1,maximum-scale=1\'>\n'
         '  <!--[if lt IE 9]>\n'
         '    <script type=\'text/javascript\' src=\'lib/aight.min.js\'></script>\n'
         '  <![endif]-->\n'
         '  <script src=\'lib/mapbox.js/latest/mapbox.js\'></script>\n'
         '  <script src=\'lib/raven.min.js\'></script>\n'
         '  <meta http-equiv="Content-Security-Policy" content="\n'
         '    default-src\n'
         '      \'self\'\n      ;\n'
         '    child-src\n'
         '      \'self\'\n'
         '      blob:\n      ;\n'
         '    connect-src\n'
         '      \'self\'\n      *\n      ;\n'
         '    font-src\n'
         '      \'self\'\n      ;\n'
         '    frame-src\n'
         '      \'self\'\n      ;\n'
         '    img-src\n'
         '      \'self\'\n'
         '      data:\n      *\n      ;\n'
         '    script-src\n'
         '      \'self\'\n'
         '      \'unsafe-eval\'\n'
         '      \'unsafe-inline\'\n'
         '      https://cdn.segment.com\n'
         '      https://assets.customer.io\n'
         '      https://secure.gaug.es\n'
         '      https://www.google-analytics.com\n      ;\n'
         '    style-src\n'
         '      \'self\'\n'
         '      \'unsafe-inline\'\n      ;\n  ">\n'
         '  <script>\n'
         '  if (/a\\.tiles\\.mapbox\\.com/.test(L.mapbox.config.HTTP_URL)) {\n'
         '    Raven.config(\'https://c2d096c944dd4150ab7e44b0881b4a46@app.getsentry.com/11480\', {\n'
         '      whitelistUrls: [/geojson\\.io/],\n'
         '      ignoreErrors: [\n'
         '          \'Uncaught Error: Error connecting to extension ckibcdccnfeookdmbahgiakhnjcddpki\',\n'
         '          \'Uncaught Error: Error connecting to extension pioclpoplcdbaefihamjohnefbikjilc\'\n'
         '      ]\n'
         '    }).install();\n  }\n'
         '  </script>\n'
         '  <style>\n'
         '  /*\n'
         '   * http://seclab.stanford.edu/websec/framebusting/framebust.pdf\n'
         '   */\n'
         '  body { display: none; }\n'
         '  </style>\n'
         '</head>\n'
         '<body id=\'geojsonio-body\'>\n\n'
         '<div class=\'geojsonio\'></div>\n\n'
         '<script>\n'
         'if (self == top) {\n'
         '  document.getElementsByTagName ("body")[0].style.display = \'block\';\n'
         '} else {\n'
         '  top.location = self.location;\n'
         '}\n'
         '</script>\n'
         '<script src=\'dist/delegate.js\'></script>\n'
         '<script src=\'dist/lib.js\'></script>\n'
         '<script src=\'dist/site.js\'></script>\n'
         '<script type=\'text/javascript\'>\n'
         'if (/a\\.tiles\\.mapbox\\.com/.test(L.mapbox.config.HTTP_URL)) {\n'
         '  var _gauges = _gauges || [];\n'
         '  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n'
         '  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n'
         '  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n'
         '  })(window,document,\'script\',\'https://www.google-analytics.com/analytics.js\',\'ga\');\n\n'
         '  ga(\'create\', \'UA-12158002-18\', \'auto\');\n'
         '  ga(\'send\', \'pageview\');\n}\n'
         '</script>\n'
         '</body>\n'
         '</html>\n'
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
    parameters=u'map?bbox=27.,53.85379229563698,'
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
    parameters=u'map?bbox='
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
    parameters=u'map?bbox='
               u'27.61649608612061,53.85379229563698,'
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
