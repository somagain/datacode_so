import streamlit as st
import pandas as pd
import math
from pathlib import Path
from PIL import Image    
import numpy as np
import plotly.figure_factory as ff






# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Data-code Solutions',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

img = Image.open("Dclogo.png")
st.sidebar.image("Dclogo.png")

st.sidebar.button("Learn More")
st.sidebar.write('''Data-Code Solutions, a leading IT firm in Abuja
                    specializes in Data science and Data Analytics training.
                    AI,ML web application development as well as IT consultancy.
                 ''')
st.sidebar.write('''### Address 
                 ''')
st.sidebar.write(''' Visit us@ Suite 19 Muneerat Plaza, Opp Lincoln College. Kurudu Phase 5 Abuja''')




@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# FSL Data-Code Solutions
### Data Science Specializations: Global Pay-Rate dashboard
Browse data from [Kaggle Open Data](https://365datascience.com/career-advice/data-science-salaries-around-the-world/).
Data science is a core component in the global tech space, driving innovation 
and informed decision-making across industries. The integration of data-driven
insights has transformed operational efficiency, product development, and 
customer experiences.


'''

# Add some spacing
''
''

min_value = gdp_df['Year'].min()
max_value = gdp_df['Year'].max()

from_year, to_year = st.slider(
    'Which years are you interested in?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

countries = gdp_df['Country Code'].unique()

if not len(countries):
    st.warning("Select at least one country")

selected_countries = st.multiselect(
    'Which countries would you like to view?',
    countries,
    ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

''
''
''

# Filter the data
filtered_gdp_df = gdp_df[
    (gdp_df['Country Code'].isin(selected_countries))
    & (gdp_df['Year'] <= to_year)
    & (from_year <= gdp_df['Year'])
]

st.header('GDP over time', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]
 
    with col:
        first_gdp = first_year[gdp_df['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[gdp_df['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'{country} GDP',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )


img = Image.open("eda_pic.gif")
st.image("eda_pic.gif")

img = Image.open("bmigif.gif")
st.sidebar.image("bmigif.gif")

st.write('''## About us
         ''')
st.write(''' With a team of expert professionals, we provide
          comprehensive solutions to businesses and individuals
          seeking to harness the power of data and AI. Our expertise
          spans data visualization, predictive modeling, machine learning, 
         and more. By leveraging cutting-edge technology and innovative approaches,
          Data-Code Solutions empowers clients to make informed decisions, drive 
         growth, and stay ahead of the competition. 
         ''')

st.write('''## Mission
         ''')
st.write(''' Our mission is to democratize data science and AI expertise.
         ''')

st.write('''## Our Programs''')
st.write('''### Data Science Masterclass(Three Months)''')
st.write('''        What you'll Learn: 
         How to profer comprehensive solutions to businesses and individuals 
         seeking to harness the power of data and AI. Throught the implementation of viz expertise: 
         Data Wrangling, Exploratory data analysis, data visualization,
            predictive modeling, machine learning, Deeplearning, AI application development''')

st.write('''### Data Analytics and BI Masterclass(5 weeks) ''')
st.write('''        What you'll Learn:
         How to profer comprehensive solutions to businesses and individuals 
         seeking to harness the power of data and AI. Throught the implementation of viz expertise: 
         nocode Data Wrangling, Exploratory data analysis, data visualization,
         storytelling, PowerBI dashboard building, Excel Dashboard Building, Dax functions''')


img = Image.open("young.jfif")
st.image("young.jfif")

   

st.write('''## Our Services''')
st.write('''    
         
         Business Intelligence Reporting\n
         Predictive Data Modelling\n
         AI and ML application development\n
         Tech Trainings\n
         Professional Internships\n
         IT consultancy
               
        ''')








    