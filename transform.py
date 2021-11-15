import lxml.html
from lxml import etree
from service import Service


class TransformerToXml():
    def create_html_file(self, services_list: list, path: str, new_file_path: str) -> None:
        import lxml.html
        from lxml import etree
        xslt_doc = etree.parse('template.xslt')
        xslt_transformer = etree.XSLT(xslt_doc)        
        source_doc = etree.parse(path)
        output_doc = xslt_transformer(source_doc)
        output_doc.write(new_file_path, pretty_print=True)
        
    
    def generate_xml_text(self, services_list: list) -> str:
        """Generates complete XML file based on [services_list]

        Args:
            services_list (list): [list of Service type elems]

        Returns:
            str: full xml text
        """
        text = '<?xml version="1.0" encoding="UTF-8"?>\n<services>\n'
        for service in services_list:
            text += self.transform(service)    
        text += "</services>"
        return text
        
    def transform(self, service: Service) -> str:
        """Transforms Service to part of xml file with properties

        Args:
            service (Service): [service]

        Returns:
            str: [part of xml file]
        """
        result = '<service>\n'
        props = service.properties()
        tags = service.get_names_eng()
        for i in range(len(props)):
            if type(props[i]) != list:
                result += f"<{tags[i]}>{props[i]}</{tags[i]}>\n"
            else:
                for item in props[i]:
                    result += f"<{tags[i]}>{item}</{tags[i]}>\n"
        result += "</service>\n"
        return result