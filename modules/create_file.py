import os
from mdutils.mdutils import MdUtils
from modules.config import Config
from modules.data import Data, File
from modules.utils import Util

class CreateMarkdown:
    def __init__(self, config:Config, data: Data, util: Util):
        self.config = config
        self.data = data
        self.util = util
        self.current_directory = os.getcwd()
        File.initialize(config)

    def installation_file(self, filepath, data, common_data):
        mdFile = MdUtils(file_name=filepath)
        mdFile.new_header(level=1, title=self.config.list_file[0])

        # Install Dependencies
        script = ''.join([str(item) for item in common_data['scriptDependencies']])
        mdFile.insert_code(f"{script}", language='bash')
        
        # Install Go
        mdFile.new_header(level=2, title="Install Go")
        script = ''.join([str(item) for item in common_data['scriptGolang']])
        script = script.replace("goVersion", data['goVersion'])
        mdFile.insert_code(f"{script}", language='bash')

        # Download Binary
        mdFile.new_header(level=2, title="Download Binary")
        script = ''.join([str(item) for item in data['scriptBinary']])
        mdFile.insert_code(f"{script}", language='bash')
        
        # Setup Variables
        mdFile.new_header(level=2, title="Setup Variables")
        script = ''.join([str(item) for item in common_data['exportEnv']])
        replacements = {
            "chain_id": data['chain_id'],
            "name_chain": data['name_chain'],
            "name_port": data['name_port'],
            "custom_port": data['custom_port'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Config and Init app
        mdFile.new_header(level=2, title="Config and Init app")
        script = ''.join([str(item) for item in common_data['scriptInit']])
        replacements = {
            "name_chain": data['name_chain'],
            "name_port": data['name_port'],
            "binary": data['binary'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')
        # Create Markdown file
        mdFile.create_md_file()

    def setup_config_file(self, filepath, data, common_data):
        mdFile = MdUtils(file_name=filepath)
        mdFile.new_header(level=1, title=self.config.list_file[1])

        # Custom ports
        mdFile.new_header(level=2, title="Custom Ports(Optional)")
        script = ''.join([str(item) for item in common_data['scriptCustomPortsApp']])
        replacements = {
            "name_chain": data['name_chain'],
            "name_home": data['home'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        script = ''.join([str(item) for item in common_data['scriptCustomPortsConfig']])
        replacements = {
            "name_chain": data['name_chain'],
            "name_home": data['home'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Setup Pruning, gas prices
        mdFile.new_header(level=2, title="Setup Pruning, gas prices")
        script = ''.join([str(item) for item in common_data['scriptPruningGasPrices']])
        replacements = {
            "min_gas_prices": data['min_gas_prices'],
            "name_home": data['home'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Setup genesis and addrbook
        mdFile.new_header(level=2, title="Setup genesis and addrbook")
        script = ''.join([str(item) for item in common_data['scriptGenesisAddrbook']])
        replacements = {
            "url_genesis": data['url_genesis'],
            "url_addrbook": data['url_addrbook'],
            "name_home": data['home'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Create systemd service
        mdFile.new_header(level=2, title="Create systemd service")
        script = ''.join([str(item) for item in common_data['scriptSystemd']])
        replacements = {
            "name_home": data['home'],
            "binary": data['binary'],
            "name": data['name'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')
        
        # Start service
        mdFile.new_header(level=2, title="Start service")
        script = ''.join([str(item) for item in common_data['scriptStart']])
        replacements = {
            "binary": data['binary'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Create Markdown file
        mdFile.create_md_file()

    def create_wallet_file(self, filepath, data, common_data):
        mdFile = MdUtils(file_name=filepath)
        mdFile.new_header(level=1, title=self.config.list_file[2])
        mdFile.new_header(level=2, title="Create wallet")
        script = ''.join([str(item) for item in common_data['scriptCreateWallet']])
        replacements = {
            "binary": data['binary'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')
        # Create Markdown file
        mdFile.create_md_file()

    def create_setup_validator_file(self, filepath, data, common_data):
        mdFile = MdUtils(file_name=filepath)
        mdFile.new_header(level=1, title=self.config.list_file[3])

        #Check status
        mdFile.new_header(level=2, title="Check status")
        script = ''.join([str(item) for item in common_data['scriptCheckStatus']])
        replacements = {
            "binary": data['binary'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        #Create validator
        mdFile.new_header(level=2, title="Create validator")
        if data['custom_create_val']:
            script = ''.join([str(item) for item in common_data['scriptCreateValidatorFile']])
        else:
            script = ''.join([str(item) for item in common_data['scriptCreateValidator']])
        fees = ''.join([str(item) for item in data['fees_method']])
        replacements = {
            "binary": data['binary'],
            "amount_denom": data['amount_denom'],
            "name_chain": data['name_chain'],
            "fees_method": data['fees_method'].replace("\n","\\\n"),
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Create Markdown file
        mdFile.create_md_file()

    def create_command_line_file(self, filepath, data, common_data):
        mdFile = MdUtils(file_name=filepath)
        mdFile.new_header(level=1, title=self.config.list_file[4])

        #Tokens
        mdFile.new_header(level=2, title="Tokens")
        script = ''.join([str(item) for item in common_data['scriptCommandLine']])
        fees = ''.join([str(item) for item in data['fees_method']])
        replacements = {
            "binary": data['binary'],
            "name_chain": data['name_chain'],
            "amount_denom": data['amount_denom'],
            "fees_method": data['fees_method'].replace("\n","-y \n\n"),
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Key management
        mdFile.new_header(level=2, title="Key management")
        script = ''.join([str(item) for item in common_data['scriptKeyManagement']])
        replacements = {
            "binary": data['binary'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')
        
        #Validator Operations
        mdFile.new_header(level=2, title="Validator Operations")
        script = ''.join([str(item) for item in common_data['scriptValidatorOperations']])
        replacements = {
            "binary": data['binary'],
            "fees_method": data['fees_method'].replace("\n",""),
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Service Operations
        mdFile.new_header(level=2, title="Service Operations")
        script = ''.join([str(item) for item in common_data['scriptServiceOperations']])
        replacements = {
            "binary": data['binary'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')

        # Create Markdown file
        mdFile.create_md_file()

    def upgrade_file(self, filepath, data, common_data):
        mdFile = MdUtils(file_name=filepath)
        mdFile.new_header(level=1, title=self.config.list_file[5])
        mdFile.new_header(level=2, title="Upgrade")
        script = ''.join([str(item) for item in common_data['scriptUpgrade']])
        replacements = {
            "binary": data['binary'],
        }
        for old_value, new_value in replacements.items():
            script = script.replace(old_value, new_value)
        mdFile.insert_code(f"{script}", language='bash')
        
        # Create Markdown file
        mdFile.create_md_file()

    def generate_markdown(self):
        # Define network types and corresponding chain lists
        networks_map = {
            'mainnet': self.config.list_mainnet,
            'testnet': self.config.list_testnet,
        }
        
        # Define the files to create along with their corresponding method calls
        file_methods = {
            File.INSTALLATION: self.installation_file,
            File.SETUP_CONFIG: self.setup_config_file,
            File.CREATE_WALLET: self.create_wallet_file,
            File.CREATE_SETUP_VALIDATOR: self.create_setup_validator_file,
            File.CREATE_COMMAND_LINE: self.create_command_line_file,
        }

        for network, chains in networks_map.items():
            for chain in chains:

                # Get data and path for current network and chain
                chains_data = self.data.get_chains_data(network, chain)
                common_data = self.data.get_common_data()
                path = self.util.get_current_path(network, chain)

                # Create the necessary directory
                self.util.create_directory(path)

                # Iterate over file types and create files using their corresponding methods
                for file_type, method in file_methods.items():
                    filepath = self.util.get_filepath(path, file_type)
                    method(filepath, chains_data, common_data)
                print(f"Create file for {network} {chain} in path: {path}")
