from file_service import FileService
from image_strategy import ImageStrategy
from pdf_strategy import PdfStrategy


image_strategy = ImageStrategy()

service = FileService(image_strategy)

file = 'teste.png'
service.process_file(file)

# OU

pdf_strategy = PdfStrategy()

service = FileService(pdf_strategy)

file = 'teste.pdf'
service.process_file(file)