try:
    import torch
    print("torch:", torch.__version__)
except ImportError:
    print("torch not installed")

try:
    import torchvision
    print("torchvision:", torchvision.__version__)
except ImportError:
    print("torchvision not installed")

try:
    import cv2
    print("cv2 (OpenCV):", cv2.__version__)
except ImportError:
    print("cv2 not installed")

try:
    import matplotlib
    print("matplotlib:", matplotlib.__version__)
except ImportError:
    print("matplotlib not installed")

try:
    import numpy
    print("numpy:", numpy.__version__)
except ImportError:
    print("numpy not installed")
