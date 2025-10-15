import streamlit as st
import matplotlib.pyplot as plt
import random

# Генериране на 20 случайни възрасти между 1 и 69
ages = [random.randint(1, 69) for _ in range(20)]

st.write("Възрасти на 20 човека:", ages)

# Създаване на хистограма
plt.figure(figsize=(12, 6))
plt.hist(ages, bins=range(1, 71), color='skyblue', edgecolor='black')
plt.xlabel('Възраст')
plt.ylabel('Брой хора')
plt.title('Хистограма на възрастта на 20 случайни човека')
plt.xticks(range(0, 71, 5))
plt.grid(axis='y', alpha=0.75)

st.pyplot(plt)
