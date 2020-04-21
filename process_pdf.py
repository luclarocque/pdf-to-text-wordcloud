# Based on code from GitHub: nadya-p/pdf_to_text.py
# Adapted to be able to produce single file containing text from all PDFs

from tika import parser
import os


def pdf_contains(pdf_directory, terms_to_find, txt_filename):
    """

    :param pdf_directory:
    :param txt_filename:
    :param terms_to_find: list of terms to search for in each
    :return:
    """
    pdf_path = os.path.join(os.getcwd(), pdf_directory)
    print("*****" * 12)
    print("Looking for PDFs in", pdf_path)
    print("*****" * 12)
    terms_dict = dict()
    for root, dirs, files in os.walk(pdf_directory):
        for file in files:
            path_to_pdf = os.path.join(root, file)
            [stem, ext] = os.path.splitext(path_to_pdf)
            if ext == '.pdf':
                print("Processing " + path_to_pdf)
                pdf_contents = parser.from_file(path_to_pdf)
                pdf_string = pdf_contents['content'].strip().lower()
                # add found terms to the terms_dict
                terms_dict[file] = list(filter(lambda term: term.lower() in pdf_string, terms_to_find))

    path_to_txt = os.path.join(root, txt_filename)
    with open(path_to_txt, 'w', encoding="utf-8") as txt_file:
        print("Writing to " + path_to_txt)
        for terms in terms_dict.values():
            for term in terms:
                txt_file.write(' {} '.format(term))
            txt_file.write('\n')


if __name__ == "__main__":
    terms_to_find = ['Python', 'SQL', 'Java', 'JavaScript', 'C++', 'C#', 'Tableau', 'Matlab', 'HTML', 'CSS']
    subdir = 'MADS Resumes'
    pdf_contains(subdir, terms_to_find, txt_filename='found_terms.txt')