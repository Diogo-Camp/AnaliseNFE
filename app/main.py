from xml_parser import XmlParser
if '__name__' == __name__:
    directory_path = r'C:\\Users\\Diogo\\Documents\\pyXML\\pasta_xml\\'
    obj_xml = XmlParser(directory_path)
    print(obj_xml.find_xml_files())
    print(obj_xml)