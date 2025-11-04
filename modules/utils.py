import os
import modules.config as Config

class Util:
    def __init__(self, config: Config):
        self.config = config
        self.current_directory = os.getcwd()

    def get_current_directory(self):
        return self.current_directory
    
    def get_current_path(self, networks, chains_name):
        # Construct the full path outside the current directory based on the config's path_output
        path = os.path.join(self.config.path_output, networks, chains_name)
        return path
    
    def create_directory(self, path):
        os.makedirs(path, exist_ok=True)

    def get_filepath(self, path, filename):
        return os.path.join(path, filename)
