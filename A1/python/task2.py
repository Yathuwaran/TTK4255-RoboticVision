
import numpy as np
import matplotlib.pyplot as plt

# %% Task 2.1
img = plt.imread("data/grass.jpg")
h,w = img.shape[:2]

print("Image height: {}\nImage width: {}".format(h,w))

# %% Task 2.2
fig1, axs = plt.subplots(1, 3, figsize=(10,3))
fig1.suptitle('RGB Channels')
for i in range(3):
    axs[i].imshow(img[:,:,i])
    axs[i].set_title("Channel {}".format(i+1))
plt.savefig("figures/channels.jpg")
plt.show()
#Channel 2 belongs to green
# %% Task 2.3
threshold_green = img[:,:,1] > 120
plt.imshow(threshold_green, cmap='gray')
plt.savefig("figures/threshold.jpg")

# %% Task 2.4
r = img[:,:,0]/img.sum(axis=2)
g = img[:,:,1]/img.sum(axis=2)
b = img[:,:,2]/img.sum(axis=2)
imgs = [r,g,b]
channels = ["R", "G", "B"
]
fig2, axs = plt.subplots(1, 3, figsize=(10,3))
fig2.suptitle('RGB Channels normalized')

for i in range(3):
    axs[i].imshow(imgs[i])
    axs[i].set_title("Channel {}".format(channels[i]))
plt.savefig("figures/channels_norm.jpg")
plt.show()

# %% Task 2.5

threshold_green = g > 0.4
plt.imshow(threshold_green, cmap='gray')
plt.savefig("figures/thresholded_norm_green.jpg")
plt.show()
