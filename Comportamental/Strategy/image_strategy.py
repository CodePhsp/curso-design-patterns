from file_interface import FileStrategy
from PIL import Image, ImageTk
import io


class ImageStrategy(FileStrategy):
    def process_file(self, file):
        
        try:
            image_stream = io.BytesIO(file)
            image = Image.open(image_stream)
            image.thumbnail((500, 500))
            
            # Lógica de descompressão do arquivo do tipo .png ou .jpg
        
        except Exception as erro:
            print('Erro decompress file: ', erro)