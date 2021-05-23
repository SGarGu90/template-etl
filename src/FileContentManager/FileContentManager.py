

class FileContentManager:
    file = None

    def __init__(self, dir_path, filename, operation):
        self.dir_path = dir_path.rstrip('/')
        self.filename = filename
        self.operation = operation

    def init_text_file(self):
        """
        Initialice the text file
        """
        self.file = open (f'{self.dir_path}/{self.filename}', self.operation)

    def print_file(self, content):
        """
        Print contentn into file

        Args:
            message (str): Text to insert on file
        """
        self.file.write(content)

    def close_file(self):
        """
        Close opened file
        """
        print("Clossing the FIle")
        self.file.close()
