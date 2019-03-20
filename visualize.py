import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def createWordCloud(text):
    try:
        print('Generating word cloud\n')
        cloud = WordCloud(max_words=500, background_color="black").generate(text)

        # Display the generated image:
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
#        wordcloud.to_file('images/mongodb-wordcloud.png')

    except:
        print('Error occured while creating word cloud\n')


