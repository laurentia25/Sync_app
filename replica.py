import os

from source import Source


class Replica:
    def __init__(self, r_path, s_path):
        self.r_path = r_path
        self.source = Source(s_path)
        self.s_path = s_path

    def get_components(self):
        # get a list with all directories available at self.r_path
        replica_components = os.listdir(self.r_path)
        # preparing the structure for replica
        replica = {"folder_components": []}
        # adding as a list item all the folder elements in the list folder_components
        for component in replica_components:
            component_path = os.path.join(self.r_path, component)
            replica["folder_components"].append(component)
            index = replica["folder_components"].index(component)
            # check if each item list from replica_components is a directory
            # if the condition above is true:
            # create dictionaries with folder name as Key and folder components as key values
            if os.path.isdir(component_path):
                sub_element = os.listdir(component_path)
                if sub_element:
                    replica["folder_components"][index] = {component: sub_element}
        return replica

    def create_folder_file(self):
        # get replica items:
        replica_items = os.listdir(self.r_path)
        # get source items:
        s_elements = os.listdir(self.s_path)
        # check if source items exist in replica items
        for s_items in s_elements:
            if s_items not in replica_items:
                s_item_path = os.path.join(self.s_path, s_items)
                r_item_path = os.path.join(self.r_path, s_items)
                if os.path.isdir(s_item_path):
                    # create in replica all folders which already exist in source
                    os.mkdir(r_item_path)
                    each_folder_components = os.listdir(s_item_path)
                    for each_folder_component in each_folder_components:
                        s_item_comp_path = os.path.join(s_item_path, each_folder_component)
                        r_item_comp_path = os.path.join(r_item_path, each_folder_component)
                        if os.path.isdir(s_item_comp_path):
                            os.mkdir(r_item_comp_path)
                        else:
                            with open(s_item_comp_path, 'r') as s_file, open(r_item_comp_path, 'w') as r_file:
                                r_file.write(s_file.read())
                else:
                    with open(s_item_path, 'r') as source_file, open(r_item_path, 'w') as replica_file:
                        replica_file.write(source_file.read())

    def delete_folder_file(self):
        # get source items:
        source_items = os.listdir(self.s_path)
        # get replica items:
        r_elements = os.listdir(self.r_path)
        # check if replica items don't exist in source items, if true -> delete the item in replica folder
        for r_items in r_elements:
            if r_items not in source_items:
                r_item_path = os.path.join(self.r_path, r_items)
                # delete item if it's a file
                if os.path.isfile(r_item_path):
                    os.remove(r_item_path)
                # delete item if it's a folder
                else:
                    # identify items in folder -> create a list
                    directory_items = os.listdir(r_item_path)
                    # iterate through item list of the directory
                    for directory_item in directory_items:
                        # recompose path to each item af the directory
                        dir_item_path = os.path.join(r_item_path, directory_item)
                        os.remove(dir_item_path)
                    else:
                        os.rmdir(r_item_path)


# obj = Replica("C:\\Replica", "C:\\Source")
# obj.delete_folder_file()

