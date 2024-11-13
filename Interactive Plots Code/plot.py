# importing pandas and plotly.express
import pandas as pd
import plotly.express as px

# loading the data
file_path = 'data/Playoffs.csv'
playoffs_data = pd.read_csv(file_path)

# adding the columns for the plot
data_filtered = playoffs_data[['year', 'PLAYER', 'TEAM', 'PTS', 'AST', 'REB']]

data_filtered['year'] = pd.Categorical(data_filtered['year'], ordered=True, categories=sorted(data_filtered['year'].unique()))

# putting the data into one column
data_melted = data_filtered.melt(id_vars=['year', 'PLAYER', 'TEAM'],
                                 value_vars=['PTS', 'AST', 'REB'],
                                 var_name='Metric', value_name='Value')

# making the plot using plotly
fig = px.scatter(data_melted, x='year', y='Value', color='PLAYER',
                 symbol='Metric', facet_row='Metric', hover_name='PLAYER',
                 title='Player Performance Comparison by Season',
                 labels={'year': 'Season Year', 'Value': 'Performance Metrics'})

# adding the layout for the players

fig.update_layout(
    xaxis=dict(title='Season Year', categoryorder='category ascending'),  # Ensure years appear in order
    yaxis=dict(title='Performance Metrics')
)

# Save fig as html
fig.write_html('charts/plot.html')

# showing the plot
fig.show()