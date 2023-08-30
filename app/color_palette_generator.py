import cv2
from sklearn.cluster import KMeans
from collections import Counter


def rgb2hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_colors(image_path):
    """takes image, classifies colours with K-means cluster and returns a list of 4 most used colours as output"""

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixels = image.reshape(-1, 3)

    kmeans = KMeans(n_init = 'auto')
    kmeans.fit(pixels)

    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    label_counts = Counter(labels)

    top_colors = [centers[label] for label, count in label_counts.most_common(4)]

    colors = []
    for color in top_colors:
        colors.append(rgb2hex(color))

    return colors





