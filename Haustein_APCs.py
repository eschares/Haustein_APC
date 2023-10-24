# Data visualizations based on Haustein et al (2023), The Oligopoly's Shift to Open Access
# Data https://zenodo.org/records/7086420
# preprint https://zenodo.org/records/8322555

# Eric Schares
# Oct. 24, 2023

import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('oecd.csv')

# Groupby journal and calculate Average APC
result = df.groupby(['source_id', 'journal_name', 'parent_publisher', 'oa_status'])[['n_dois','apc_total']].sum().reset_index()
result['apc'] = result['apc_total'] / result['n_dois']
result = result.sort_values(by=['apc_total'], ascending=False)

# Remove Diamond OA (APC=0) entries
result = result[result['oa_status']!='diamond (gold APC=0)']
result


# Scatter plot by journal
fig = px.scatter(result, x='n_dois', y='apc_total', log_x = True, log_y = True, color='oa_status', #symbol='parent_publisher',
                 title='Total APCs collected and number of articles, by journal, 2015-2018', opacity=0.5,
                hover_name = 'journal_name',
                hover_data = ['oa_status', 'apc'],
                color_continuous_scale=px.colors.sequential.Viridis)

# APC lines
fig.add_shape(type="line",
    x0=1, y0=500, x1=100000, y1=50000000,
    line=dict(color="Purple", width=1, dash="dot"))

fig.add_annotation(x=4.5, y=7,
            text="APC $500",
            showarrow=False,
            arrowhead=0,
            #bordercolor="Purple",
            textangle=-25)

fig.add_shape(type="line",
    x0=1, y0=1000, x1=100000, y1=100000000,
    line=dict(color="Green", width=1, dash="dot"))

fig.add_annotation(x=4.5, y=7.35,
            text="$1000",
            showarrow=False,
            arrowhead=0,
            textangle=-25)

fig.add_shape(type="line",
    x0=1, y0=2000, x1=100000, y1=200000000,
    line=dict(color="Black", width=1, dash="dot"))

fig.add_annotation(x=4.5, y=7.7,
            text="$2000",
            showarrow=False,
            arrowhead=0,
            textangle=-25)

fig.add_shape(type="line",
    x0=1, y0=3000, x1=100000, y1=300000000,
    line=dict(color="RoyalBlue", width=1, dash="dot"))

fig.add_annotation(x=4.5, y=8.1,
            text="$3000",
            showarrow=False,
            arrowhead=0,
            textangle=-25)

fig.add_shape(type="line",
    x0=1, y0=5000, x1=100000, y1=500000000,
    line=dict(color="Red", width=1, dash="dot"))

fig.add_annotation(x=4.5, y=8.4,
            text="$5000",
            showarrow=False,
            arrowhead=0,
            textangle=-25)

fig.update_layout(height=500, width=1500)

st.plotly_chart(fig, use_container_width=True)