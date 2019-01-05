from file_type_classifier import FileTypeClassifier
from image_file_type import ImageFileType
import settings
import pydicom


def read_single_input_file(input_file):
    dataset_file = pydicom.dcmread(input_file)
    return dataset_file


def main():
    print("Starting main")
    print(settings.tags_to_offset)
    file_type_classifier = FileTypeClassifier()

    image_file = ImageFileType()

    file_types_configuration = image_file.file_types_configuration

    print(type(file_types_configuration))
    print(file_types_configuration)
    print(file_types_configuration['CT'])
    print(type(file_types_configuration['CT']['tags_to_anonymize']))
    print(file_types_configuration['CT']['tags_to_anonymize'])


    input_dataset_file = read_single_input_file(settings.test_input_file)
    # print(input_dataset_file)

    input_file_type = FileTypeClassifier.identify(input_dataset_file)
    print("input_file_type:", input_file_type)

    tags = file_types_configuration[input_file_type]['tags_to_anonymize']
    print("tags:", type(tags), tags)

    print("tags to deal with on {} are: {}".format(input_file_type, tags))

    # input_dataset_file[settings.tags_to_offset["name"]].value = ''
    # input_dataset_file[(16, 16)].value = ''
    print(input_dataset_file)
    # tags_list = ImageFileType(file_type, configuration_file_path)

    # for tag in tags:
    #     image_file_type.anonymize_blank_value(ds_file, tag)

    # image_file_type.anonymize_blank_value(ds_file, ('0x10', '0x10'))

    # print(ds_file)


if __name__ == "__main__":
    main()



