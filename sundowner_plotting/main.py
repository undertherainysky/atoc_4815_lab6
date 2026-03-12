import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sundowner_plotting import read_file


singleDay_df = read_file("wxobs20250213.txt")
singleDay_df.plot(y= ['Hi_Temp', 'Low_Temp', 'Temp_Out'],
    figsize=(9, 4),
    title='February 13th, 2025 Temperature Time Series',
    ylabel='Temperature (°C)',
    grid=True,
    alpha=0.7
)
plt.savefig("tempplot02132025.png", dpi=200, bbox_inches = 'tight')
plt.tight_layout()
plt.show()




# plan:
    # first: consider what kinds of data we want
        # idea 1: accumulation of precip
            # pros: could generate cool graphs
            # cons: requires so much data 
        # idea 2: look at special days, like feb 13th or something
            # pros: less data, unless if comparing across years
            # cons: a little bit more creativity in graphing required
        # idea 3: other accumulations
            # best paired with idea 1, potentially multiple graphs across different variables
            # pros: more even cooler graphs
            # cons: a LOT of data
    # second: import - done!
    # third: refactor - done!
    # four: identify path - done!
        # test grabbing data - pathway found!
    # fifth: test loading text files - done!