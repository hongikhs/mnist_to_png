import png
import csv
import numpy as np
mnist_file = 'mnist_train_100'
m = open(mnist_file + '.csv', encoding='utf-8')
mnist = csv.reader(m, delimiter=',')
fnum = 1

for row in mnist:
    label = row[0]
    image = list(map(int, row[1:]))
    print(label, len(image))
    f = open(mnist_file + '\\' + label + '\\' + str(fnum) + '.png', 'wb')
    w = png.Writer(28, 28, greyscale=True)
    image2d = (255-np.array(image)).reshape((28, 28)).tolist()
    w.write(f, image2d)
    f.close()
    fnum += 1

m.close()
