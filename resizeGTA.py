import numpy as np
import scipy as scp
import scipy.misc
from glob import glob

im_names = sorted(glob('./*/*/*_image.jpg'))
result = []
print('guid/image,N')

for idx,im_name in enumerate(im_names):
    image = scp.misc.imread(im_name)
    image = scp.misc.imresize(image, (512,
                                    960),
                            interp='cubic')
    scp.misc.imsave(im_name, image)

    lb_txt = im_name + '.txt'
    new_lb_txt = im_name + '.new.txt'
    if os.path.exist(lb_txt):
        labels = [line.rstrip() for line in open(lb_txt, 'r')]
        fid = open(new_lb_txt,'w+')
        for label in labels:
            L = (float(label[1]) - 3) * 0.516
            U = (float(label[2]) - 2) * 0.4867
            R = (float(label[3]) - 3) * 0.516
            B = (float(label[4]) - 2) * 0.4867

            newLabel = "{} {} {} {} {}\n".format(labels[0], L, U, R, B)
            fid.write(newLabel)

        fid.close()


