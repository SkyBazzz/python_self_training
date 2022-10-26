import re
from xml.dom.minidom import parse, Node
from xml.etree.ElementTree import parse as e_parse

FILE_PATH = "resources/simple_xml.xml"


def ugly():
    with open(FILE_PATH, "r") as text:
        full_text = text.read()
        found = re.findall('<title>(.*)</title>', full_text)
        for title in found:
            print(title)


def pretty():
    xml_tree = parse(FILE_PATH)
    for node1 in xml_tree.getElementsByTagName('title'):
        for node2 in node1.childNodes:
            if node2.nodeType == Node.TEXT_NODE:
                print(node2.data)


def the_prettiest():
    tree = e_parse(FILE_PATH)
    for E in tree.findall('title'):
        print(E.text)


ugly()
pretty()
the_prettiest()
