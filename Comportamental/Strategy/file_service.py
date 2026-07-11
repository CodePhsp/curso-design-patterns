from file_interface import FileStrategy


class FileService:
    def __init__(self, service: FileStrategy):
        self._service = service
    
    def process_file(self, file):
        return self._service.process_file(file)
    