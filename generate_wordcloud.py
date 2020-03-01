from pdf_to_text import pdf_to_text
import os

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import string

# PLEASE ENTER:
#---------------------------------------------------------------------
pdf_dirname = 'MADS Resumes'
txt_filename = 'text_from_all_pdfs.txt'
wordcloud_filename = 'wordcloud.png'
#---------------------------------------------------------------------


def generate_wordcloud(in_path, out_path):
    with open(in_path, 'r', encoding="utf-8") as text_file:
        text = text_file.read().replace('\n', ' ')

        # remove non-printable characters
        printable = set(string.printable)
        text = ''.join(filter(lambda x: x in printable, text))

    wordcloud = WordCloud(
        font_path='C:\\Users\\llarocque\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Montserrat-Medium.ttf',
        height=1080,
        width=1920,
        stopwords=STOPWORDS,
        background_color="white").generate(text)

    wordcloud.to_file(out_path)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def pdf_to_wordcloud(pdf_dir, txt_fname, out_fname):
    pdf_to_text(pdf_dir, txt_fname)  # creates txt file from all PDFs
    txt_path = os.path.join(os.getcwd(), pdf_dir, txt_fname)  # determine path of txt file
    generate_wordcloud(txt_path, out_fname)  # use txt file to generate wordcloud


if __name__ == "__main__":
    pdf_to_wordcloud(os.path.join(os.getcwd(), pdf_dirname), 'text_from_all_pdfs.txt', wordcloud_filename)
