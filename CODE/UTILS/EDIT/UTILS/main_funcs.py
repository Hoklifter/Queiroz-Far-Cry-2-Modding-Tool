from xml.etree.ElementTree import (
    Element

)

from .get_shit import (
    get_child_elements_info,
    get_element_info
)

from .print_shit import (
    print_elements
)

def show_options(self):
    """Show the user all options that the current element offer e.g

    self.current = {
        'object' : {
            'value' : {},
            'hash' : {},
            'object' : {},
        }
    }

    will print:
    1 - value {}
    2 - hash {}
    3 - object {}
    4 - to go back

    """
    self.current = self.stack[-1]

    if self.current is self.parents:
        options = self.parents_names
    else:
        options = get_child_elements_info(self.current)

    self.options = options
    print_elements(options)
    
def ask_for_input(self):
    if self.current is not self.parents:
        prompt = f"""You are in {self.current_info!r}
{len(self.options)} - To go back
{len(self.options) + 1} - To edit
{len(self.options) + 2} - To Save
Navigate Through the objects. Select one's number: """
    else:
        prompt = f"""
You are in {self.current_info!r}
Navigate Through the objects. Select one's number: """
    
    self.user_input = int(input(prompt))
    print()
    
def remove_current_from_stack(self):
    self.stack.pop()
    self.current = self.stack[-1]
    if self.current == self.parents:
        self.current_info == "ROOT"
    else:
        self.current_info = get_element_info(self.stack[-1])

def add_selection_to_stack(self):
    self.current_info = self.options[self.user_input]
    selection = self.current[self.user_input]
    self.stack.append(selection)


def edit_current(self):
    new_tag = input("New tag (Empty to leave as it is) :\n")
    new_attrib = input("New attributes in the format name='Name',x=y (Empty to leave as it is) :\n")
    new_text = input("New text (Empty to leave as it it is) :\n")

    if new_tag:
        self.current.tag = new_tag
    if new_attrib:
        new_attribs = new_attrib.split(",")
        for attrib in new_attribs:
            key, value = attrib.split('=')
            self.current.set(key, value)
    if new_text:
        self.current.text = new_text

def save_document(self):
    self.domtree.write(self.filename)

def logic_based_on_user_input(self):
    """
    if user input < 0:
        do nothing
    if user input == amount of options:
        go back

    if user input == amount of options +1:
        edit mode
    
    if user input inside range of options:
        select element in index
    """

    amount_of_options = len(self.options)

    if self.user_input < 0:
        pass
    elif self.user_input == amount_of_options:
        remove_current_from_stack(self)
    elif self.user_input == amount_of_options + 1:
        edit_current(self)
    elif self.user_input >= amount_of_options + 2:
        save_document(self)
    else:
        add_selection_to_stack(self)
        