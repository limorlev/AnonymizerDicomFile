from file_type_classifier import FileTypeClassifier
from image_file_type import ImageFileType
import settings


def main():
    print("Starting main")
    file_type_classifier = FileTypeClassifier()

    file_type, ds_file = file_type_classifier.identify(settings.test_input_file,
                                                       settings.modality_tag)

    image_file = ImageFileType()

    file_types_configuration = image_file.file_types_configuration

    print(type(file_types_configuration))
    print(file_types_configuration)
    print(file_types_configuration['CT'])
    print(type(file_types_configuration['CT']['tags_to_anonymize']))
    print(file_types_configuration['CT']['tags_to_anonymize'])

    # tags_list = ImageFileType(file_type, configuration_file_path)

    # for tag in tags:
    #     image_file_type.anonymize_blank_value(ds_file, tag)

    # image_file_type.anonymize_blank_valu(ds_file, ('0x10', '0x10'))

    # print(ds_file)


if __name__ == "__main__":
    main()


