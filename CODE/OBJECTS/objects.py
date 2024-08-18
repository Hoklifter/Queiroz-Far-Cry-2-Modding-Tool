import xml.etree.ElementTree as et
import tkinter
import os

class FC2XmlElement:
    def __init__(self, element:et.Element):
        self.element_instance = element
        self.name = self.get_name(self.element_instance)
        self.text = self.element_instance.text

    def get_name(self, element:et.Element):
        return element.get('name') or element.get('type') or  f"<{element.tag}  hash={element.get('hash')}>"

    def __len__(self):
        counter = 0
        for _ in self.element_instance:
            counter +=1
        return counter
    
    def set_child_value(self, child_index, value):
        child = self.element_instance[child_index]
        child.text = value
    
    
class FC2XmlParent:
    def __init__(self, element_instance:et.Element):
        self.name = element_instance[0].text
        self.entity = FC2XmlElement(element_instance[1])
        self.element_instance = element_instance

class FC2Xml(et.ElementTree):
    def __init__(self, path):
        self.path = os.path.realpath(path)
        et.ElementTree.__init__(self, file=self.path)
        self.basename = os.path.basename(self.path)
        self.parents = self.get_parents()
        
    def get_parents(self):
        parents = self._root.findall("object")
        _parents = []

        for parent in parents:
            parent = FC2XmlParent(parent)
            _parents.append(parent)

        return _parents
    
    def save_document(self):
        self.write(self.path)
    