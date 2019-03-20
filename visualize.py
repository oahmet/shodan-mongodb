import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def createWordCloud(text):
    try:
        print('Generating word cloud\n')
        cloud = WordCloud(max_words=200, width=1600, height=800).generate(text)

        # Display the generated image:
        plt.figure(figsize=(20, 10), facecolor='k')
        plt.imshow(cloud, interpolation='bilinear')
        plt.tight_layout(pad=0)
        plt.axis("off")
        plt.show()
#        wordcloud.to_file('images/mongodb-wordcloud.png')

    except:
        print('Error occured while creating word cloud\n')


