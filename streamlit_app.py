import streamlit as st
import pandas as pd
import numpy as np

st.title('numpy.random distributions with different parameter values')

N = 10_000
st.subheader(f"N set to {N} globally")

st.subheader('np.random.pareto(a, size=N)')
a = st.slider('Parameter: a', 0, 10, 1)  # min: 0, max: 10, default: 1
pareto = np.random.pareto(a, N)
pareto[::-1].sort()
st.line_chart(pareto)

st.subheader("np.random.exponential(scale, size=N)")
scale = st.slider('Parameter: scale', 0, 10, 1)  # min: 0, max: 10, default: 1
exponential = np.random.exponential(scale, N)
exponential[::-1].sort()
st.line_chart(exponential)

