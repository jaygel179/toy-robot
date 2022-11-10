from exceptions import FileReaderException


class InputOutputHandler:
    def read(self, file_location=None):
        data = []
        try:
            with open(file_location) as f:
                data = f.read().split("\n")
        except Exception:
            raise FileReaderException(f"File '{file_location}' not found.")

        return data

    def write(self, data):
        # can write into a file but console out for now
        print(data)
