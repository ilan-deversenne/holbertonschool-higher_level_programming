#!/usr/bin/env python3

"""
XML De/Serialize
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str):
    """
    Docstring for serialize_to_xml

    :param dictionary: Dictionary
    :type dictionary: dict
    :param filename: Filename
    :type filename: str
    """

    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename: str) -> dict:
    """
    Docstring for deserialize_from_xml

    :param filename: Filename
    :type filename: str
    :return: Dictionary of XML File content
    :rtype: dict
    """

    result = {}
    root = ET.parse(filename).getroot()

    for child in root:
        result[child.tag] = child.text

    return result
