import streamlit as st
import pandas as pd
import math
from pathlib import Path
from PIL import Image    
import numpy as np
import plotly.figure_factory as ff
import time
import os
from itertools import cycle






# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Data-code Solutions',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)



#Interractive pic start

# Interractive pics end
# -----------------------------------------------------------------------------
# Declare some useful functions.
img = Image.open("Dclogo4.png")
st.sidebar.image("Dclogo4.png", width=230)

st.sidebar.button("Learn More")
st.sidebar.write('''Data-Code Solutions, a leading IT firm in Abuja
                    specializes in Data science and Data Analytics training.
                    AI,ML web application development as well as IT consultancy.
                 ''')
st.sidebar.write('''### Address 
                 ''')
st.sidebar.write(''' Visit us@ Suite 19 Muneerat Plaza, Opp Lincoln College. Kurudu Phase 5 Abuja''')




@st.cache_data



@st.cache_data
def get_pay_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    
    
    DATA_FILENAME = Path(__file__).parent/'new1_ds.csv'
    raw_ds_df = pd.read_csv(DATA_FILENAME)
    
    
    MIN_YEAR = 2005
    MAX_YEAR = 2024
    
    
  
    # Melting the DataFrame
    melted_df = pd.melt(raw_ds_df, id_vars=['Abbreviation','Data Science Discipline', 'Annual Pay Package (USD)'], var_name='Year', 
                        value_name='Score')
    print("\nMelted DataFrame:")
    
    
    # The data above has columns like:
    # - Data Science Discipline
    # - Abreviation
    # - ANnual Package
    # - Pay for 2005
    # - ---
    # - Pay for 2024
    # - ...
    # - 
    #
    # ...but I want this instead:
    # - Data Science Discipline
    # - Abbreviation
    # - Year
    # - Pay
    #
    # So let's pivot all those year-columns into two: Year and GDP
    try:
        melted_df['Year'] = melted_df['Year'].astype(int)
    except ValueError:
        st.error("Error: Could not convert 'Year' column to integers. Check the format of your CSV file.")
        return None

    return melted_df


    



# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
## Data Code Solutions :ng::snowboarder:
With a team of expert professionals, we provide
comprehensive solutions to businesses and individuals
seeking to harness the power of data and AI. Our expertise
spans data visualization, predictive modeling, machine learning, 
and more. By leveraging cutting-edge technology and innovative approaches,
Data-Code Solutions empowers clients to make informed decisions, drive 
growth, and stay ahead of the competition. Our training and Internship programs
Provides new techies the edge the need to break into the global tech space.
'''

filteredImages = ['image_folder/1739462223398.jpg', 'image_folder/1739462223389.jpg' , 
          'image_folder/1739462223407.jpg'
          ]



caption = ['Innovation and Creativity', 'Excellence', 'Passion'] # your caption here
cols = cycle(st.columns(3)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(filteredImages):
    next(cols).image(filteredImage, width=230,  caption=caption[idx])

'''
### Why Learn Data Science? :chart:
The Demand for Data Science and AI specialty is currently the fastest growing in the globally IT market
(World Economic Forum, 2025).Browse data from [Kaggle Open Data](https://365datascience.com/career-advice/data-science-salaries-around-the-world/).
Data science is a core component in the global tech space, driving innovation 
and informed decision-making across industries. The integration of data-driven
insights has transformed operational efficiency, product development, and 
customer experiences.Below is a global view of Data Science earning in various fields such as 
Machine Learning (ML),Data Analytics (DA), Data Engineering (DE) etc.
#### Data Science Specializations: Global Pay-Rate dashboard:dollar::money_with_wings::euro:



'''


# Add some spacing
''
''

ds_df = get_pay_data()

if ds_df is not None:
    min_value = int(ds_df['Year'].min())  # Cast to int
    max_value = int(ds_df['Year'].max())  # Cast to int

    from_year, to_year = st.slider(
        'Which years are you interested in?',
        min_value=min_value,
        max_value=max_value,
        value=[min_value, max_value]
    )

Abbreviate = ds_df['Abbreviation'].unique()

if not len(Abbreviate):
    st.warning("Select at least one Discipline")

selected_discipline = st.multiselect(
    'Which Track would you like to view?',
    Abbreviate,
    ['DS', 'MLE', 'DE', 'RS', 'AID', 'RE'])

''
''
''




# Filter the data
filtered_ds_df = ds_df[
    (ds_df['Abbreviation'].isin(selected_discipline))
    & (ds_df['Year'] <= to_year)
    & (from_year <= ds_df['Year'])
]

st.header('Pay Range over time :dollar:', divider='gray')

''

st.line_chart(
    filtered_ds_df,
    x='Year',
    y='Score',
    color='Abbreviation',
)

''
''

if ds_df is not None and filtered_ds_df is not None:  # Make sure DataFrames exist
    st.header(f'Global Average(G20 Nations) Salaries in {to_year}', divider='gray')

    cols = st.columns(4)

    for i, discipline in enumerate(selected_discipline):
        col = cols[i % len(cols)]

        with col:
            first_year_discipline = ds_df[ds_df['Abbreviation'] == discipline]
            last_year_discipline = ds_df[ds_df['Abbreviation'] == discipline]

            first_pay = first_year_discipline['Score'].iloc[0] / 1000 if not first_year_discipline.empty else np.nan
            last_pay = last_year_discipline['Score'].iloc[0] / 1000 if not last_year_discipline.empty else np.nan

            if math.isnan(first_pay) or math.isnan(last_pay):
                growth = 'n/a'
                delta_color = 'off'
            elif first_pay == 0:
                growth = 'n/a'  # Or some other appropriate value
                delta_color = 'off'
            else:
                growth = f'{last_pay / first_pay:,.2f}x'
                delta_color = 'normal'

            st.metric(
                label=f'{discipline} SALARY',
                value=f'{last_pay:,.0f}k$' if not math.isnan(last_pay) else 'n/a',  # Handle NaN value
                delta=growth,
                delta_color=delta_color
            )
#first_year = ds_df[ds_df['Year'] == from_year]
#last_year = ds_df[ds_df['Year'] == to_year]


img = Image.open("eda_pic.gif")
st.image("eda_pic.gif")

img = Image.open("bmigif.gif")
st.sidebar.image("bmigif.gif")

st.write('''## About us
         ''')
st.write('''  Our expertise
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


