import json
from modules.config import Config
from enum import Enum

class Data:
    def __init__(self, config: Config):
        self.config = config
        with open(config.data_json) as f:
            self.data = json.load(f)

    def get_data(self):
        return self.data
    
    def get_networks(self):
        return self.data['networks']

    def get_mainnet_chains(self, chains):
        return self.data['mainnet'][chains]
    
    def get_chains_data(self, networks, chains_name):
        if networks == "mainnet":
            chains_list = self.config.list_mainnet
        if networks == "testnet":
            chains_list = self.config.list_testnet
        if chains_name not in chains_list:
            print(f"Error: Chain '{chains_name}' is not available in the '{networks}' network.")
            return None 
        return self.data[networks][chains_name]
    
    def get_common_data(self):
        return self.data['common']

class File(Enum):
    @classmethod
    def initialize(cls, config):
        cls.INSTALLATION = config.list_file[0] if len(config.list_file) > 0 else None
        cls.SETUP_CONFIG = config.list_file[1] if len(config.list_file) > 1 else None
        cls.CREATE_WALLET = config.list_file[2] if len(config.list_file) > 2 else None
        cls.CREATE_SETUP_VALIDATOR = config.list_file[3] if len(config.list_file) > 3 else None
        cls.CREATE_COMMAND_LINE = config.list_file[4] if len(config.list_file) > 4 else None
        cls.UPGRADE = config.list_file[5] if len(config.list_file) > 5 else None    