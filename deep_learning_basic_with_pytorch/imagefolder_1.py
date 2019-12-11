import torchvision
from torchvision import transforms

import matplotlib.pyplot as plt

origin_data_path = 'custom_data/origin_data'

# Transforms are common image transformations.
# https://pytorch.org/docs/stable/torchvision/transforms.html#torchvision.transforms.Compose
# Compose several transforms together (chaining)
'''
transforms.Compose([
    transforms.CenterCrop(10),
    transforms.ToTensor()
])
'''
trans = transforms.Compose([
    transforms.Resize(size=(64,128))
])

# https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder
# A generic data loader where the images are arranged in this way:
'''
origin_data
├── grey (class 1)
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   └── 6.png
└── red (class 2)
    ├── 1.png
    ├── 2.png
    ├── 3.png
    └── 4.png  
'''
# https://www.programcreek.com/python/example/105102/torchvision.datasets.ImageFolder
train_data_origin = torchvision.datasets.ImageFolder(root=origin_data_path, transform=trans)

for num, value in enumerate(train_data_origin):
    data, label = value
    print(num, data, label)

    if label == 0:
        data.save('custom_data/train_data/gray/%d_%d.jpeg' % (num, label))
    else:
        data.save('custom_data/train_data/red/%d_%d.jpeg' % (num, label))
    # plt.imshow(data)
    # plt.show()
    # break