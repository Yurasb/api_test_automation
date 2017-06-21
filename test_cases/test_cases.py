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
    parameters=u'18/52.52060/31.18780',
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
