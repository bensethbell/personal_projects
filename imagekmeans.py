from sklearn.cluster import KMeans

def img_kmeans(img_list, num_clusters):
    # convert all images to black and white
    images_bw = []
    for i in img_list:
        images_bw.append(load_to_bw(i))

    # unravel all data
    image_data = []
    for i in images_bw:
        image_data.append(np.array(list(i.getdata())))

    kmeans = KMeans(num_clusters)
    mu_digits = kmeans.fit(image_data[:5]).cluster_centers_

def load_to_bw(url):
    f = cStringIO.StringIO(urllib.urlopen(url).read())
    img = Image.open(f)
    img_bw = img.convert('1')
    return img_bw