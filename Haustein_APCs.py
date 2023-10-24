# Data visualizations based on Haustein et al (2023), The Oligopoly's Shift to Open Access
# Data https://zenodo.org/records/7086420
# preprint https://zenodo.org/records/8322555

# Eric Schares
# Oct. 24, 2023

import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Oligopoly APCs')

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
                 title='Total APCs collected and number of articles, by journal, 2015-2018', opacity=0.4,
                hover_name = 'journal_name',
                hover_data = ['oa_status', 'apc'],
                color_discrete_sequence=px.colors.qualitative.Plotly)

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

fig.update_layout(height=600, width=800)

fig.update_xaxes(showgrid=True)

st.plotly_chart(fig)



fig3 = px.scatter(result, x='n_dois', y='apc_total', log_x = True, log_y = True, color='parent_publisher', #symbol='parent_publisher',
                 title='Total APCs collected and number of articles, by publisher, 2015-2018', opacity=0.4,
                hover_name = 'journal_name',
                hover_data = ['oa_status', 'apc'],
                color_discrete_sequence=px.colors.qualitative.Plotly)

fig3.update_layout(height=600, width=800)

fig3.update_xaxes(showgrid=True)

st.plotly_chart(fig3)



fig2 = px.scatter(result, x='n_dois', y='apc_total', log_x = True, log_y = True, color='oa_status', 
                 facet_col='parent_publisher', facet_col_wrap=2,
                 title='Total APCs collected and number of articles, by journal and publisher, 2015-2018', opacity=0.4,
                hover_name = 'journal_name',
                hover_data = ['oa_status', 'apc'],
                color_discrete_sequence=px.colors.qualitative.Plotly)

# fig2.add_shape(type="line",
#     x0=1, y0=3000, x1=100000, y1=300000000,
#     line=dict(color="RoyalBlue", width=1, dash="dot"))

fig2.update_layout(height=800, width=800)

fig2.update_xaxes(showgrid=True)

st.plotly_chart(fig2)#, use_container_width=True)



st.header('By OA Mode')
by_oamode = pd.read_csv('byoamode.csv')
by_oamode

fig4 = px.bar(by_oamode, x='parent_publisher', y='apc_total', color='oa_status', color_discrete_sequence=px.colors.qualitative.Plotly)

fig4.update_layout(height=600, width=800)
st.plotly_chart(fig4)



fig5 = px.scatter(by_oamode, x='n_dois_percent', y='apc_total_percent', color='oa_status', symbol='parent_publisher',
                  color_discrete_sequence=px.colors.qualitative.Plotly)

fig5.add_shape(type="line",
    x0=.2, y0=.2, x1=.8, y1=.8,
    line=dict(color="Red", width=1, dash="dot"))

fig5.update_xaxes(nticks=10, showgrid=True)

st.plotly_chart(fig5)