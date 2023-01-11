
import streamlit as st
import pandas as pd

# Load data into the app
df = pd.read_excel("202212_Mango factories list 2022_English.xlsx")

# Specify the title and logo for the web page.
st.set_page_config(page_title='Mango Supplier List',
                   layout="wide")

# Add social media tags and links to the web page.
#[![Star](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@dniggl)
#[![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dennisniggl)
#[![Follow](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/DennisNiggl)

# Add a title and a markdown
"""
# Mango Supplier List
"""
st.markdown('---')


# Add a sidebar to the web page.
st.sidebar.image('https://download.logo.wine/logo/Mango_(retailer)/Mango_(retailer)-Logo.wine.png', width=200)
st.sidebar.markdown('Mango is a Spanish clothing and accessories retailer founded in 1984. '
                    'Mango operates in more than 110 countries worldwide and has a strong online presence in addition to its physical stores.')
st.sidebar.markdown('Supplier list can be accessed via their website. Accessed: 2022/12.')
st.sidebar.markdown('---')

# Create a select box to filter the DataFrame by Gender
country_filter = st.sidebar.selectbox("Filter by Country:", ["All", "TURKEY", "CHINA"])

# Apply the filter to the DataFrame
if country_filter != "All":
    df = df[df['Country'] == country_filter]

st.sidebar.markdown('---')
st.sidebar.write('Developed by Niclas Musies')
st.sidebar.write('Contact: niclas@zeropath.de')


# Display the Data in the App.
st.subheader('Full Supplier List')
st.dataframe(df)

# Display statistical information on the dataset.
st.subheader('Statistical Info')
st.write(df.describe())