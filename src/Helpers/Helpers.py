import json
import os.path

class HelperClass:

    @staticmethod
    def input_int(message, required_positive = False, allowed_zero = True):
        """
        Request input only integer type allowed. Configurable validate positive and zero values.

        Args:
            message (str): Input message
            required_positive (bool, optional): Force input to be positive number. Defaults to False.
            allowed_zero (bool, optional): Validate number to allow zero value. Defaults to True.

        Returns:
            int: console inserted value that pass configured rules(required_positive and allowed_zero)
        """

        int_value = 0
        while True:
            try:
                int_value = int(input(message))
                is_positive = (int_value >= 0) and required_positive
                is_zero = ((int_value == 0) and allowed_zero)
                is_valid = is_positive and (is_zero or (int_value != 0))
                if not is_valid:
                    type_value = type(int_value)
                    print(f'Integer number > 0 is mandatory. Inserted value is \'{int_value}\' {type_value}')
                    continue
                break
            except ValueError:
                print("Value type integer is mandatory.")

        return int_value

    @staticmethod
    def input_float(message, required_positive = False, allowed_zero = True):
        """
        Request input only float type allowed. Configurable validate positive and zero values.

        Args (rules):
            message (str): Input message
            required_positive (bool, optional): Force input to be positive number. Defaults to False.
            allowed_zero (bool, optional): Validate number to allow zero value. Defaults to True.

        Returns:
            float: console inserted value that pass configured rules(required_positive and allowed_zero)
        """
        float_value = 0
        while True:
            try:
                float_value = float(input(message))
                is_positive = (float_value >= 0) and required_positive
                is_zero = ((float_value == 0) and allowed_zero)
                is_valid = is_positive and (is_zero or (float_value != 0))
                if not is_valid:
                    type_value = type(float_value)
                    print(f'Float number > 0.0 is mandatory. Inserted value is \'{float_value}\' {type_value}')
                    continue
                break
            except ValueError:
                print("Value type float is mandatory.")

        return float_value

    @staticmethod
    def input_str(message = "", options = []):
        """Request normal input string. Configurable with message and options to validate

        Args:
            message (str, optional): Input message. Defaults to "".
            options (list, optional): List of options to validate. Defaults to [].

        Returns:
            str: selected option
        """
        opt = ""
        while True:
            opt = input(message)
            if (len(options) > 0) and (opt not in options):
                type_opt = type(opt)
                print(f'Specific value is mandatory. Inserted value is \'{opt}\' {type_opt}')
                continue
            else:
                break

        return opt

    @staticmethod
    def save_data_to_file(DATA_DIR_PATH = "sample_data", file_name = "example", data = [], overwrite = False):
        """Save data into json file

        Args:
            DATA_DIR_PATH (str): directory path. Defaults to "sample_data"
            file_name (str): file name. Defaults to "example"
            data (list of obj): contains data to save on file
            overwrite (bool, optional): Force overwrite if already exist file. Defaults to False.
        """
        path = f'{DATA_DIR_PATH}/{file_name}.json'
        is_empty_file = False

        if not os.path.isfile(path):
            is_empty_file = True
            open(path, "a")
            with open(path, "w") as write_file:
                json.dump([], write_file)

        if overwrite or is_empty_file:
            with open(path, "w") as write_file:
                json.dump(data, write_file, indent=2, default=str)
        else:
            print ("Data file already exist or is not empty, set overwrite = TRUE to overwrite contents")

    @staticmethod
    def get_data_from_file(DATA_DIR_PATH = "sample_data", file_name = "example"):
        """Get data from json file

        Args:
            DATA_DIR_PATH (str): directory path. Defaults to "sample_data"
            file_name (str): file name. Defaults to "example"

        Returns:
            list json obj: data from file
        """
        path = f'{DATA_DIR_PATH}/{file_name}.json'

        if os.path.isfile(path):
            with open(path) as json_file:
                return json.load(json_file)
        else:
            print(f'File does not exit at "{path}"')

    @staticmethod
    def printt(data, beauty=True):
        """Custom print beauty json data

        Args:
            data (list of items): data to print
            beauty (bool, optional): Defines if beauty or normal print. Defaults to True.
        """
        if beauty:
            print(json.dumps(data, indent=2, sort_keys=True))
        else:
            print(data)