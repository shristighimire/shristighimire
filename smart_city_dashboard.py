# -*- coding: utf-8 -*-
"""Smart City Dashboard

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tRdaBJlTynQ2A9Kv4rogtvmOd_Ect3-j
"""

!pip install streamlit pyngrok --quiet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import numpy as np
# 
# # Simulated Smart City Data
# np.random.seed(42)
# data = pd.DataFrame({
#     "Time": pd.date_range(start="2024-01-01", periods=100, freq="H"),
#     "Energy_Usage": np.random.randint(50, 150, 100),
#     "Traffic_Count": np.random.randint(200, 1000, 100),
#     "Weather_Temperature": np.random.uniform(20, 35, 100),
# })
# 
# # Streamlit Dashboard
# st.title("Smart City Dashboard")
# st.sidebar.title("Filters")
# 
# # Filter by time
# time_range = st.sidebar.slider("Select Time Range:", 0, len(data) - 1, (0, len(data) - 1))
# filtered_data = data.iloc[time_range[0]:time_range[1]]
# 
# # Charts
# st.line_chart(filtered_data.set_index("Time"))
# 
# st.markdown("### Key Statistics")
# st.write(filtered_data.describe())
#

!ngrok authtoken 2qQETu3SGuYTIRpNI5h2PJf63Q6_iUbzkAoo4dcQG8dMXhzz

from pyngrok import ngrok
import os

# Start the Streamlit server
os.system("streamlit run app.py &")

# Expose the Streamlit server to the web using ngrok
# Pass the port within the 'addr' parameter
public_url = ngrok.connect(addr="8501")
print(f"Streamlit app is running on {public_url}")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
#     import streamlit as st
#     import pandas as pd
#     import numpy as np
# 
#     # ... (Your existing code for data generation and other widgets) ...
# 
#     st.bar_chart(filtered_data[['Energy_Usage', 'Traffic_Count']]) # Add this line to app.py

import requests

def get_weather_data():
    api_key = "YOUR_API_KEY"
    city = "Your City"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

import streamlit as st # Import streamlit at the beginning of the cell

@st.cache
def load_data():
    return pd.read_csv("large_dataset.csv")

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# Simulated Smart City Data
np.random.seed(42)
data = pd.DataFrame({
    "Time": pd.date_range(start="2024-01-01", periods=100, freq="H"),
    "Energy_Usage": np.random.randint(50, 150, 100),
    "Traffic_Count": np.random.randint(200, 1000, 100),
    "Weather_Temperature": np.random.uniform(20, 35, 100),
})

# Example: Predict traffic count based on energy usage
model = LinearRegression()
X = data[['Energy_Usage']]  # Input feature
y = data['Traffic_Count']  # Target variable
model.fit(X, y)
predictions = model.predict(X)

# Assuming 'st' refers to streamlit, make sure it's imported
import streamlit as st
st.write("Predictions:", predictions)