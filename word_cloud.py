# -*- coding: utf-8 -*-
'''
Created on 2017-11-07 14:46
---------
@summary:
---------
@author: Boris
'''

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from cut_text import CutText

def main(text):
    wordcloud = WordCloud(font_path='simsun.ttc', background_color="white")#中文需要指定字体
    # wordcloud = WordCloud(font_path='simsun.ttc', margin=5, width=1800, height=800, max_words=2000, max_font_size=60,
    #                       random_state=42)
    wordcloud.generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    wordcloud.to_file('D:/dora.jpg')
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    cut_text = CutText()
    cut_text.set_stop_words('stop_words.txt')
    with open('text.txt', 'r', encoding = 'utf-8') as file:
        text = file.read()
        text = cut_text.cut(text)
        text = ' '.join(text)

        print(text)

        main(text)