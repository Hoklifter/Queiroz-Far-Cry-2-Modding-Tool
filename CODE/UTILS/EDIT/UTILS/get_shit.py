import xml.etree.ElementTree as ET

def get_parents(root):
    parents = root.findall("object")
    parents_names = []

    for parent in parents:
        name = parent.find("value").text        
        parents_names.append(f"ROOT of {name}")

    return parents, parents_names


def get_child_elements_info(parent):
        children_info = []
        for child in parent:
            child_info = get_element_info(child)
            children_info.append(child_info)

        return children_info

def get_element_info(element):
    element_info = ()
    tag = element.tag
    attrib = element.attrib
    text = element.text

    for x in [tag, attrib, text]:
        if x:
            if isinstance(x, str):
                x = x.strip()
            element_info += (x,)
    return element_info
