import os
import json


class File:
    """class for work with file"""

    def __init__(self) -> None:
        self.path = os.getcwd()

    def __delete_json_files(self) -> None:
        """delete all json files in this directory"""

        # get json files
        json_files = [file for file in os.listdir(self.path) if file.endswith('.json')]

        # delete this files
        for file in json_files:
            os.remove(os.path.join(self.path, file))

    def create_file(self, name: str, result: int) -> None:
        """create new json file with result"""

        # delete old files
        self.__delete_json_files()

        with open(name + '.json', 'w') as file:
            file.write(json.dumps({'result': result}))
