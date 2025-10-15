import streamlit as st
import numpy as np
from scipy import stats


# Данни
data1 = [4, 1, 7]
data2 = [4, 2, 4, 3, 2, 2]


# Средна стойност
mean_val = np.mean(data1)
st.write("Средна стойност на", data1, "е", mean_val)


# Медиана
median_val = np.median(data1)
st.write("Медиана на", data1, "е", median_val)


# Мода
mode_val = stats.mode(data2).mode[0]
st.write("Мода на", data2, "е", mode_val)
