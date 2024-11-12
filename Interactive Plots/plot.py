# importing pandas and plotly.express
import pandas as pd
import plotly.express as px

# loading the data
file_path = 'Playoffs.csv'
playoffs_data = pd.read_csv(file_path)

# adding the columns for the plot
data_filtered = playoffs_data[['year', 'PLAYER', 'TEAM', 'PTS', 'AST', 'REB']]

data_melted = data_filtered.melt(id_vars=['year', 'PLAYER', 'TEAM'],
                                 value_vars=['PTS', 'AST', 'REB'],
                                 var_name='Metric', value_name='Value')

# making the interactive scatter plot 
fig = px.scatter(data_melted, x='year', y='Value', color='PLAYER',
                 symbol='Metric', facet_row='Metric', hover_name='PLAYER',
                 title='Player Performance Comparison by Season',
                 labels={'year': 'Season Year', 'Value': 'Performance Metrics'})

# adding the layout for the players
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(label="All Players", method="update", args=[{"visible": [True] * len(data_melted['PLAYER'].unique())}]),
                # Add individual player filters here as needed
            ],
            direction="down",
            showactive=True,
            x=0.1,
            y=1.15
        )
    ],
    xaxis=dict(title='Season Year'),
    yaxis=dict(title='Performance Metrics')
)

fig.write_html('plot.html')

# showing the plot
fig.show()

