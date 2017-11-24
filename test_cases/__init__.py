# -*- coding: utf-8 -*-

from lxml import etree


def get_xmlschema(xsd_path):
    with open(xsd_path, 'r') as xsd:
        xmlschema_doc = etree.parse(xsd)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        return xmlschema
