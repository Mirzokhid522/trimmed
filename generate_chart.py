import pandas as pd
import plotly.graph_objects as go

# 1. Load your data
# We use skipinitialspace=True to handle spaces after commas
df = pd.read_csv('Australia CPI.csv', index_col=0, skipinitialspace=True)

# --- DEBUGGING LINE ---
print("Detected column headers:", df.columns.tolist())
# ----------------------

# 2. Define the Dark Theme Aesthetics
bg_black = '#000000'
text_white = '#ffffff'
grid_dark = '#333333'

fig = go.Figure()

# 3. Add traces
# We use the columns detected by the print statement above
fig.add_trace(go.Bar(
    x=df.index, 
    y=df.iloc[:, 0], # Using iloc ensures we grab the first column regardless of its name
    name='Change from previous month',
    marker_color='#1f77b4'
))

fig.add_trace(go.Scatter(
    x=df.index, 
    y=df.iloc[:, 1], # Using iloc ensures we grab the second column regardless of its name
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

# 5. Export for Notion
fig.write_html("index.html")
print("Chart generated successfully as index.html")