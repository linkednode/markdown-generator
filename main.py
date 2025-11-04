from modules.config import Config
from modules.create_file import CreateMarkdown
from modules.data import Data
from modules.utils import Util

def main():
    config = Config()
    data = Data(config)
    util = Util(config)
    create_markdown = CreateMarkdown(config, data, util)
    create_markdown.generate_markdown()
    

if __name__ == "__main__":
    main()
