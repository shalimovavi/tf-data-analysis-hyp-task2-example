import pandas as pd
import numpy as np
import scipy.stats as st


chat_id = 1267315308 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_v = st.cramervonmises_2samp(x, y)[1]
    if (p_v < 0.1):
        return True
    else:
        return False
    
