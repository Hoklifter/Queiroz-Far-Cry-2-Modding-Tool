import xml.etree.ElementTree as et
import os
import re

class FC2XmlNode:
    def __init__(self) -> None:
        pass

    def get_master(self):
        if isinstance(self, FC2XmlElement):
            master = self.element_instance
        elif isinstance(self, FC2XmlParent):
            master = self.entity.element_instance

        return master

    def __len__(self):
        counter = 0
        for _ in self.get_master():
            counter +=1
        return counter

    def get_element_from_xpath(self,
            xpath:str,
            parent:'FC2XmlElement | FC2XmlParent',
            search_method='find'
        ) -> 'FC2XmlElement | list[FC2XmlElement, ...]':#type:ignore

        parent = self.get_master()
        found = getattr(parent, search_method)(xpath)
        if isinstance(found, list):
            found = [FC2XmlElement(element) for element in found]
        elif isinstance(found, et.Element):
            found = FC2XmlElement(found)

        return found

    def splitted_name(self, xml_instance:'FC2Xml'=None):
        """Returns splitted version of self.name
        [class, weapon]
        0 will always be the class
        Will do specific cases for specific files if you pass it as an argument

        """
        splitted_name = re.split(pattern=r"\.|_", string=self.name)
        class_name = splitted_name[0]
        object_name = splitted_name[1]

        if isinstance(xml_instance, FC2Xml) and xml_instance.basename == 'weapons.xml':

            #Ied is a different case since the name is at the end
            if (object_name.lower() == 'ied') and (class_name.lower() == 'explosives'):
                if len(splitted_name) > 3:
                    object_name = splitted_name[3:]
                else:
                    object_name = splitted_name[1:]
                object_name = ''.join(object_name)


        return class_name, object_name
#Há granadas sendo tratadas como armas por causa dessa função de separar as armas por categorias
# Por exemplo : Grenades.M79_Grenade e Secondary.M79. Ambos após splittados se tornariam m79. Isso é um problema
    def populate_stats(self, stats:dict[str : dict["xpath" : str]], attrib_key='element') -> None:
        """
        stats input example:
        'horizontal_recoil' : {
            'xpath' : './/value[@name='fHorizontalRecoilPerShot']'
        }

        output:

        'horizontal_recoil' : {
            "xpath" : ".//value[@name='fHorizontalRecoilPerShot']"
            "element" : <CODE.OBJECTS.objects.FC2XmlElement object at 0x794e336a0820> or None
        }


        input:
            stat_name : stat_info={
            "xpath" : str

        output:
            stat_name : stat_info={
                "xpath" : str
                item_key : FC2XmlElement or None
            }

        """
        parent = self.get_master()
        for stat_name, stat_info in stats.items():
            stats[stat_name][attrib_key] = self.get_element_from_xpath(xpath=stat_info['xpath'], parent=parent)

    def __getitem__(self, indexes):
        child = self.get_master()
        if isinstance(indexes, list):
            for index in indexes:
                child = child[index]
        elif isinstance(indexes, int):
            child = child[indexes]
        else:
            raise TypeError()

        return FC2XmlElement(child)

    def __setitem__(self, indexes, value):
        child = self[indexes]
        child_type = type(child)
        if not isinstance(value, child_type):
            raise TypeError(f'{child_type} can only be set to another {child_type}.')

        child = value


    def __iter__(self):
        master = self.get_master()
        for child in master:
            yield FC2XmlElement(child)


class FC2XmlElement(FC2XmlNode):
    def __init__(self, element_instance:et.Element):
        super().__init__()

        self.element_instance = element_instance
        self.name = self.get_name(self.element_instance)
        self.text = self.element_instance.text

    def get_name(self, element:et.Element):
        return element.get('name') or element.get('type') or  f"<{element.tag}  hash={element.get('hash')}>"


class FC2XmlParent(FC2XmlNode):
    def __init__(self, element_instance:et.Element):
        super().__init__()

        self.name = element_instance[0].text
        self.entity = FC2XmlElement(element_instance[1])
        self.element_instance = element_instance

class FC2Xml(et.ElementTree):
    def __init__(self, path):
        self.path = os.path.realpath(path)
        et.ElementTree.__init__(self, file=self.path)

        self.basename = self.get_basename()
        self.parents = self.get_parents()
        self.unified_parents = self.unify_elements()

    def get_basename(self):
        basename:str = os.path.basename(self.path).lower()
        if '_' in basename:
            basename = basename.split('_', 1)[1]

        return basename

    def get_parents(self) -> list[FC2XmlParent, ...]: #type:ignore
        parents = self._root.findall("object")
        _parents = []

        for parent in parents:
            parent = FC2XmlParent(parent)
            _parents.append(parent)

        return _parents

    def unify_elements(self, elem_list=None) -> dict:
        """Return joined list of similar elements
        If no element list argument is passed, the function will iterate through the element who called it"""
        elem_list = elem_list or self.parents

        unused_classes = ['aimcurves']
        unused_elems = []

        abbreviated_names = {}

        for elem in elem_list:
            elem_class, elem_name = elem.splitted_name(xml_instance=self)
            elem_class = elem_class.lower()
            elem_name = elem_name.lower()
            if elem_class in unused_classes or elem_name in unused_elems:
                continue

            if elem_class not in abbreviated_names:
                abbreviated_names[elem_class] = {}

            if elem_name not in abbreviated_names[elem_class]:
                abbreviated_names[elem_class][elem_name] = []

            abbreviated_names[elem_class][elem_name].append(elem)

        # from pprint import pprint
        # pprint(
        #     abbreviated_names
        # )
        return abbreviated_names

    def save_document(self):
        self.write(self.path, short_empty_elements=False)
