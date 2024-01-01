import glob

    # Attributes
class Status:
    # Variables
    INPUT_READY = False
    SETTING_UPDATED = False
    ERR_MSG = ""
    LIST_INPUT_FILES = []

    @staticmethod
    def clear_error_message():
        Status.ERR_MSG = ""
    

    @staticmethod
    def update_list_input_files(input_path: str, file_ext: str):
        Status.LIST_INPUT_FILES = [file for file in glob.glob(input_path + './*.{}'.format(file_ext))]