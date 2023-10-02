import os


class Source:
    def __init__(self, path):
        self.path = path

    def get_folder_components(self):
        # get a list with all folder components
        folder_components = os.listdir(self.path)
        # define the structure to be followed
        source = {"folder_components": []}
        # iterate through folder components
        for component in folder_components:
            # recompose path for each component
            component_path = os.path.join(self.path, component)
            # add each component to the list defined at line 12
            source["folder_components"].append(component)
            # get each component's index
            index = source["folder_components"].index(component)
            # check if the component is a directory
            if os.path.isdir(component_path):
                # get a list with all component's items
                sub_element = os.listdir(component_path)
                # check if sub_element exists
                if sub_element:
                    # replace each item from the list with a dictionary
                    # dict key = component name
                    # dict values = files in component directory
                    source["folder_components"][index] = {component: sub_element}
        return source

