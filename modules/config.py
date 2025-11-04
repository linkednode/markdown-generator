import os
import configparser

class Config:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.config_object = configparser.ConfigParser()
        
        try:
            self.config_object.read("config.ini")  # Use read instead of read_file
        except FileNotFoundError:
            print(f"Configuration file not found in {self.current_directory}")
        
        self.path_output = self.config_object.get('GENERAL', 'path_output', fallback=self.current_directory)
        
        self.list_mainnet = []
        if self.config_object.has_section('MAINNET'):  # Check if section exists
            for key in self.config_object.options('MAINNET'):
                self.list_mainnet.append(self.config_object.get("MAINNET", key))
        
        self.list_testnet = []
        if self.config_object.has_section('TESTNET'):  # Check if section exists
            for key in self.config_object.options('TESTNET'):
                self.list_testnet.append(self.config_object.get("TESTNET", key))

        self.list_file = []
        if self.config_object.has_section('FILENAME'):  # Check if section exists
            for key in self.config_object.options('FILENAME'):
                self.list_file.append(self.config_object.get("FILENAME", key))
        
        self.data_json = self.config_object.get('GENERAL', 'data_json')