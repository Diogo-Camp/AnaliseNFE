import os
class XmlParser:
    def __init__(self, directory_path):
        #mudar para o seu
        self.directory_path = directory_path #path da pasta dos arquivos
        
    def find_xml_files(self) -> list:
        """
        Busca todos os xmls no diretorio especifico
        Retorna uma lista de strings onde cada string é o caminho pra um arquivo xml
        """
        
        xml_files = [os.path.join(self.directory_path, file)
                     #os.listdir, recebe um path de arg e retorna uma lista de arquivos e diretorios
                     for file in os.listdir(self.directory_path)
                     if file.endswith('.xml')]
        return xml_files
                             
                    
        
            
    def parse_xml_file(self, file_path):
        """Metodo para extrair dados de um unico arquivo xml"""
        pass
        
    def process_all_xmls():
        """Metodo que processa todos os arquivos xml do dir. tipo run"""
        pass
        
if '__main__' == __name__:
     directory_path = (r'C:/Users/Diogo/Documents/pyXML/app/pasta_xmls/')
     obj_xml = XmlParser(directory_path)
     for file in obj_xml.find_xml_files():
         print(file)
     print(obj_xml)
    