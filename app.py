import streamlit as st
import matplotlib.pyplot as plt
import random

# Генериране на 20 случайни възрасти между 1 и 69
ages = [random.randint(1, 69) for _ in range(20)]

bins = list(range(0, 80, 10))  # 0-10, 11-20, ..., 71-80

# Създаване на хистограма
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=bins, color='skyblue', edgecolor='black')
plt.xlabel('Възрастови групи')
plt.ylabel('Брой хора')
plt.title('Хистограма на възрастта на 20 случайни човека (интервали 10 години)')
plt.xticks(bins)
plt.grid(axis='y', alpha=0.75)

st.pyplot(plt)
