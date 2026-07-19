import pandas as pd
import plotly.graph_objects as go

# 1. Load your data
df = pd.read_csv('Australia CPI.csv', index_col=0, skipinitialspace=True)

# 2. Define the Dark Theme Aesthetics
bg_black = '#000000'
text_white = '#ffffff'
grid_dark = '#333333'

fig = go.Figure()

# 3. Add traces
fig.add_trace(go.Bar(
    x=df.index, 
    y=df.iloc[:, 0],
    name='Change from previous month',
    marker_color='#1f77b4'
))

fig.add_trace(go.Scatter(
    x=df.index, 
    y=df.iloc[:, 1], 
    name='Annual change', 
    mode='lines+markers',
    line=dict(width=3, color='#aec7e8')
))

# 4. Apply Dark Mode Layout
fig.update_layout(
    plot_bgcolor=bg_black,
    paper_bgcolor=bg_black,
    font=dict(color=text_white, family='Arial'),
    xaxis=dict(showgrid=False, linecolor=text_white, tickfont=dict(color=text_white)),
    yaxis=dict(showgrid=True, gridcolor=grid_dark, zerolinecolor=text_white, tickfont=dict(color=text_white)),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1, font=dict(color=text_white)),
    margin=dict(l=40, r=40, t=80, b=40)
)

# 5. Export for Notion with full-page black background
html_content = fig.to_html(full_html=True, include_plotlyjs='cdn')

# Inject CSS to make the entire browser background black
full_html = html_content.replace(
    '<body', 
    '<body style="background-color: #000000; margin: 0; padding: 0;"'
)

with open("index.html", "w") as f:
    f.write(full_html)

print("Chart generated successfully as index.html with black page background")