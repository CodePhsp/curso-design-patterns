from file_interface import FileStrategy
from PIL import Image, ImageTk
import fitz


class PdfStrategy(FileStrategy):
    def process_file(self, file):
        
        try:
            document_pdf = fitz.open(stream=file, filetype='pdf')
            page_document = document_pdf.load_page(0)
            pixmap = page_document.get_pixmap()
            
            pdf_stream = Image.frombytes('RGB', [pixmap.width, pixmap.height], pixmap.samples)
            
            # Lógica de descromprssão do arquivodo tipo .pdf
            
        except Exception as erro:
            print('Erro decopress pdf: ', erro)