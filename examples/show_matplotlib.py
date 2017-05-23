import logging
logging.basicConfig(level=logging.INFO)

import matplotlib.pyplot as plt
import pyrealsense as pyrs

with pyrs.Service():
    dev = pyrs.Device()
    dev.wait_for_frames()
    plt.imshow(dev.color)
    plt.show()
