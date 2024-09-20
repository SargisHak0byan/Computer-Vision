#%% md
# #### See where your python.exe is located 
#%%
import sys
print(sys.executable)
#%% md
# #### See your working directory
#%%
import os
print(os.getcwd())
#%% md
# #### Test your imports
#%%
import cv2
import numpy as np
import matplotlib
#%% md
# #### Display the version of OpenCV 
#%%
print(cv2.__version__)
#%%
