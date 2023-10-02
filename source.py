import os


class Source:
    def __init__(self, path):
        self.path = path

    def get_folder_components(self):
        folder_components = os.listdir(self.path)
        source = {"folder_components": []}
        for component in folder_components:
            component_path = os.path.join(self.path, component)
            source["folder_components"].append(component)
            index = source["folder_components"].index(component)
            if os.path.isdir(component_path):
                sub_element = os.listdir(component_path)
                if sub_element:
                    source["folder_components"][index] = {component: sub_element}
        return source


# obs = Source("C:\\Source")
