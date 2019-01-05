import pydicom


class FileTypeClassifier:
    @staticmethod
    def identify(file_path, modality_tag):
        ds_file = pydicom.dcmread(file_path)
        file_type = ds_file[modality_tag].value
        return file_type, ds_file
