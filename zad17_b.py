#Paweł Majewski EiT Programowanie w języku Python
#zad_17
# Sparsuj przygotowanego XML (parserem SAX)
import xml.sax


class SaxHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_data = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.current_data = tag
        if self.current_data == "movie":
            print(f"\ntitle: {attributes['title']}")

    def characters(self, attributes):
        if self.current_data == "type":
            self.type = attributes
        elif self.current_data == "format":
            self.format = attributes
        elif self.current_data == "year":
            self.year = attributes
        elif self.current_data == "rating":
            self.rating = attributes
        elif self.current_data == "stars":
            self.stars = attributes
        elif self.current_data == "description":
            self.description = attributes

    def endElement(self, attributes):
        if self.current_data == "type":
            print(f"type: {self.type}")
        elif self.current_data == "format":
            print(f"format: {self.format}")
        elif self.current_data == "year":
            print(f"year: {self.year}")
        elif self.current_data == "rating":
            print(f"rating: {self.rating}")
        elif self.current_data == "stars":
            print(f"stars: {self.stars}")
        elif self.current_data == "description":
            print(f"description: {self.description}")
        self.current_data = ""


if __name__ == '__main__':

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    sax_handler = SaxHandler()

    parser.setContentHandler(sax_handler)

    parser.parse("new_b.xml")


