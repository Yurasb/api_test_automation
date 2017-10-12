# -*- coding: utf-8 -*-

from StringIO import StringIO
from lxml import etree


def parse_body(body):
    xml = StringIO(body)
    doc = etree.parse(xml)
    return doc
