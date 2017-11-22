import pandas as pd
import numpy as np

data=pd.DataFrame(np.array([[1,2],[1,2]]),columns=['A','B'])
def main():
    return data.head()

if __name__=="__main__":
    main()
