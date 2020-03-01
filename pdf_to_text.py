# Based on code from GitHub: nadya-p/pdf_to_text.py
# Adapted to be able to produce single file containing text from all PDFs

from tika import parser
import os


def pdf_to_text(pdf_directory, txt_filename, individual=False):
    print("*****" * 12)
    print("Looking for PDFs in", os.path.join(os.getcwd(), pdf_directory))
    print("*****" * 12)
    for root, dirs, files in os.walk(pdf_directory):
        for file in files:
            path_to_pdf = os.path.join(root, file)
            [stem, ext] = os.path.splitext(path_to_pdf)
            if ext == '.pdf':
                print("Processing " + path_to_pdf)
                pdf_contents = parser.from_file(path_to_pdf)
                if individual:
                    path_to_txt = stem + '.txt'
                    with open(path_to_txt, 'w', encoding="utf-8") as txt_file:
                        print("Writing contents to " + path_to_txt)
                        txt_file.write(pdf_contents['content'].strip())
                else:
                    path_to_txt = os.path.join(root, txt_filename)
                    with open(path_to_txt, 'a', encoding="utf-8") as txt_file:
                        print("Appending contents to " + path_to_txt)
                        txt_file.write(pdf_contents['content'].strip() + '\n')


if __name__ == "__main__":
    subdir = 'MADS Resumes'
    pdf_to_text(os.path.join(os.getcwd(), subdir), txt_filename='text_from_all_pdfs.txt')