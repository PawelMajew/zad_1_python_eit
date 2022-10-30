#Paweł Majewski EiT Programowanie w języku Python
#zad_17
# Sparsuj przygotowanego XML (parserem DOM) i go
# zmodyfikuj np. zmień wartość któregoś tag’a i zapisz do nowego
# pliku
import xml.dom.minidom


def parse_and_change_tag(file,tag,new_tag):
    DOMTree = xml.dom.minidom.parse(file)
    collection = DOMTree.documentElement

    movies = collection.getElementsByTagName(tag)[0]
    movies.tagName = new_tag

    with open("new_file.xml", "wb") as f:
        f.write(collection.toxml("utf-8"))


if __name__ == '__main__':
    parse_and_change_tag("new.xml", "movie", "newTag")
