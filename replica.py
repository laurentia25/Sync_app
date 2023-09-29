import os

from source import Source


class Replica:
    def __init__(self, r_path, s_path):
        self.r_path = r_path
        self.source = Source(s_path)

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
        pass
        replica = self.get_components()
        replica_items = replica["folder_components"]
        s_elements = self.source.get_folder_components()
        # print(s_elements)
        for components in s_elements["folder_components"]:
            # print(components)
            if components not in replica_items:
                # print(replica_items)
                print(components)
                # if isinstance(components, dict):
                #     # get folder name in order to define path in replica folder
                #     component = list(components.keys())[0]
                #     component_path = os.path.join(self.r_path, component)
                #     # create folder in replica
                #     os.mkdir(component_path)
                #     print(component_path)
                # else:
                #     pass

    def rename_folder_file(self):
        # verifica daca toate componentele folderului sunt identice in cele 2 surse
        # daca da, atunci folderul a fost redenumit in sursa
        # schimba denumirea si in replica
        pass

    def delete_folder_file(self):
        pass
        # verifica daca fisierul/folderul trebuie sterse sau updatate

    def sync(self, time):
        pass


obj = Replica("C:\\Replica", "C:\\Source")
obj.create_folder_file()
obj.get_components()
