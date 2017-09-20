# -*- coding: utf-8 -*-
from StringIO import StringIO
from lxml import etree


def get_doc(content):
    xml = StringIO(content)
    doc = etree.parse(xml)
    return doc
