import os, string
from PyPDF2 import PdfReader

def get_words_from_file(text_path):
    """
    Extracts words from a file, handling text and PDF formats (using PyPDF2).
    Args:
        text_path (str): Path to the file.
    Returns:
        list: A list of words from the file, or None if an error occurs.
    """
    
    # Check file extension
    filename, file_extension = os.path.splitext(text_path)
    if file_extension.lower() == '.pdf':
        return get_text_from_pdf(text_path)
    else:
        # Use your existing text file processing approach here (e.g., get_words_from_text)
        return get_words_from_text(text_path) # Replace with your text file function

def get_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyPDF2 library.
    Args:
        pdf_path (str): Path to the PDF file.    
    Returns:
        str: The extracted text content from the PDF.
    """
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return preprocessing(text)
    except FileNotFoundError as e:
        print(e)
        print(f"Error: PDF file not found at {pdf_path}")
        return
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return


def get_words_from_text(text_path):
    """Reads text from a file, skips encoding errors, and returns words.
    Args:
        text_path (str): Path to the text file.
    Returns:
        list: A list of words from the text file, with errors gracefully handled.
    Note:
    This implementation has two main trade-offs:
    (i) Less Reliable Decoding: This method doesn't guarantee accurate decoding of all characters, especially those outside the basic ASCII range.
    (ii) Data Loss: Characters that can't be decoded as UTF-8 are skipped, potentially leading to data loss.
    """

    try:
        # Open the file with UTF-8 encoding (common encoding). This will allow for a slighly higer efficiency if this enocding is found.
        with open(text_path, encoding='utf-8') as f:
            text = f.read()

    except FileNotFoundError:
        print(f"FileNotFoundError: file not found at {text_path}")
        return

    except UnicodeDecodeError:
        # If UTF-8 fails, open as bytes and iterate character-by-character
        with open(text_path, 'rb') as f:
            text = bytearray() # an array designed to store data in bytes, each one representing 8 bits (binary digits), allowing for 256 possible values (0 to 255).
            for byte in iter(lambda: f.read(1), b''): # creates an iterable with iter(lambda: f.read(1), b''), which reads one byte (calling f.read(1)) untill the empty byte string b'' is found.
                # Try decoding each byte as UTF-8, skip if error
                try:
                    char = byte.decode('utf-8')
                except UnicodeDecodeError:
                    continue
                text.append(char.encode('ascii', errors='ignore').decode('ascii'))

            # Convert bytes to string
            text = ''.join(text)

    return preprocessing(text)

def preprocessing(text):
    text =  " ".join(text.split()) # make the spaces of at most one blankspace
    text = text.lower()
    modified = ""
    for c in text:
        if c == " " or c in string.ascii_lowercase and c not in '\x02': # He\x02llo! It’s me. -> hello its me (note that ’ != ', and \x02 == )
            modified += c
    
    words = modified.split()
    return words