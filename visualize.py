import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def createWordCloud(text):
    try:
        print('Generating word cloud\n')
        cloud = WordCloud().generate(text)

        # Display the generated image:
        plt.figure(figsize=(10, 8), facecolor='white', edgecolor='blue')
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    except:
        print('Error occured while creating word cloud\n')


