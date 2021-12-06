import json
import fitz
from docx import Document


class PdfParser:
    """
        Represents pdf parser.

        ...

        Attributes:
        ----------
            content : str
                some content
            text : List[]
                contain serialized text data.

        Methods:
        --------

        read_file()
            Return whole text from the pdf file.

        parse_content()
            Return json encrypted content for future functions of extracting.

        """
    def __init__(self, content):
        self.content = content
        self.text = []

    def read_file(self, *args):
        file_name = 'Lab_6_Fep_2.pdf'
        with open(file_name) as f:
            f = fitz.open(file_name)
            for current_page in range(len(f)):
                page = f.load_page(current_page)
                page_text = page.get_text("text")
                self.text.append(page_text)
                final_text = ' '.join(self.text)
        return final_text

    def parse_content(self, *args):
        return json.dumps(self.text)


class DocxParser:
    """
        Represents docx parser.

        ...

        Attributes:
        ----------
            content : str
                some content
            text : List[]
                contain serialized text data.

        Methods:
        --------

        read_file()
            Return whole text from the docx file.

        parse_content()
            Return json encrypted content for future functions of extracting.

        """
    def __init__(self, content):
        self.content = content
        self.text = []

    def read_file(self, *args):
        file_name = 'Lab_6_Fep_2.docx'
        with open(file_name, 'rb') as f:
            f = Document(file_name)
            for current_page in f.paragraphs:
                self.text.append(current_page.text)
                final_text = ' \n'.join(self.text)
        return final_text

    def parse_content(self, *args):
        return json.dumps(self.text)


class Extractor:
    """
        Represents Extractor.

        ...

        Attributes:
        ----------
            content : str
                some content

        Methods:
        --------

        extract_dates()
            Return array of datetime objects.

        extract_numbers()
            Return array of number objects.

        extract_names()
            Return array of names objects.

        """
    def __init__(self, content):
        self.content = content

    def extract_dates(self):
        pass

    def extract_numbers(self):
        pass

    def extract_names(self):
        pass


class Processor:
    """
        Represents Processor (facade class).

        ...

        Methods:
        --------

        operation()
            Return array of results.

        """
    def __init__(self, pdf_parser: PdfParser, docx_parser: DocxParser) -> None:
        self._pdf_parser = pdf_parser or PdfParser(content='')
        self._docx_parser = docx_parser or DocxParser(content='')

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._pdf_parser.read_file('Lab_6_Fep_2.pdf'))
        results.append(self._docx_parser.read_file('Lab_6_Fep_2.pdf'))

        results.append(self._pdf_parser.parse_content('Lab_6_Fep_2.docx'))
        results.append(self._docx_parser.parse_content('Lab_6_Fep_2.docx'))
        return "\n".join(results)


def client_code(processor: Processor) -> None:
    print(processor.operation(), end="")


if __name__ == "__main__":
    pdf_parser = PdfParser(content='')
    docx_parser = DocxParser(content='')
    processor = Processor(pdf_parser, docx_parser)
    client_code(processor)
