# import pydicom
import settings
import json


class ImageFileType:
    def __init__(self):
        self.file_types_configuration = self.get_file_types_configuration()

    def anonymize_blank_value(self, dataset_file, tag):
        dataset_file[tag].value = ''

    @staticmethod
    def get_file_types_configuration():
        with open(settings.file_types_configuration_file, "r") as input_file:
            file_types_configuration = json.load(input_file)
        return file_types_configuration

