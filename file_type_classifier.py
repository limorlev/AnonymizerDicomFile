import pydicom
import settings


class FileTypeClassifier:
    @staticmethod
    def identify(dataset_file):
        file_type = dataset_file[settings.modality_tag].value
        return file_type
