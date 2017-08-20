# -*- coding: utf-8 -*-


def test_xml_schema(xmlschema, doc):
    xmlschema.assertValid(doc)
