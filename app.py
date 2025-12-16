import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk
from data import get_championship_data

# Page config
st.set_page_config(page_title="Campeonato Brasileiro 2006-2025", layout="wide")

# Load Data
df = get_championship_data()

# Title
st.title("🏆 Campeonato Brasileiro: Estatísticas dos Campeões (2006-2025)")
st.markdown("Uma visualização interativa dos campeões brasileiros na era dos pontos corridos (recorte 2006-2025).")

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Títulos Analisados", len(df))
with col2:
    st.metric("Maior Pontuação", f"{df['Points'].max()} (Flamengo 2019)")
with col3:
    st.metric("Maior Saldo de Gols", f"+{df['GoalDiff'].max()} (Flamengo 2025)")

# 1. Top Champions (Bar Chart)
st.subheader("🥇 Maiores Campeões no Período")
titles_count = df['Champion'].value_counts().reset_index()
titles_count.columns = ['Time', 'Títulos']

chart_titles = alt.Chart(titles_count).mark_bar().encode(
    x=alt.X('Títulos', axis=alt.Axis(tickMinStep=1)),
    y=alt.Y('Time', sort='-x'),
    color=alt.Color('Time', legend=None),
    tooltip=['Time', 'Títulos']
).properties(height=400)
st.altair_chart(chart_titles, use_container_width=True)

# 2. Points Over Time (Line Chart)
st.subheader("📈 Pontos dos Campeões ao Longo dos Anos")
chart_points = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('Year:O', title='Ano'),
    y=alt.Y('Points', scale=alt.Scale(domain=[60, 95]), title='Pontos'),
    tooltip=['Year', 'Champion', 'Points']
).properties(height=400)
st.altair_chart(chart_points, use_container_width=True)

# 3. Goal Difference (Bar Chart)
st.subheader("⚽ Saldo de Gols dos Campeões")
chart_goals = alt.Chart(df).mark_bar().encode(
    x=alt.X('Year:O', title='Ano'),
    y=alt.Y('GoalDiff', title='Saldo de Gols'),
    color=alt.condition(
        alt.datum.GoalDiff == df['GoalDiff'].max(),
        alt.value('orange'),  # Highlight the max value
        alt.value('steelblue')
    ),
    tooltip=['Year', 'Champion', 'GoalDiff']
).properties(height=400)
st.altair_chart(chart_goals, use_container_width=True)

# 4. Map of Champions (Pydeck)
st.subheader("🗺️ Mapa dos Campeões (Por Estado)")

# Prepare data for map: Aggregate titles per state
map_data = df.groupby(['State', 'Lat', 'Lon']).size().reset_index(name='Titles')

# Define colors for states (RGB)
state_colors = {
    'SP': [0, 128, 0, 200],   # Green
    'RJ': [0, 0, 255, 200],   # Blue
    'MG': [255, 0, 0, 200],   # Red
    'RS': [255, 255, 0, 200]  # Yellow (if needed in future)
}

map_data['color'] = map_data['State'].apply(lambda x: state_colors.get(x, [128, 128, 128, 200]))

layer = pdk.Layer(
    "ScatterplotLayer",
    map_data,
    get_position=['Lon', 'Lat'],
    get_color='color',
    get_radius=30000,  # 30km radius points
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=1,
    radius_min_pixels=10,
    radius_max_pixels=100,
)

view_state = pdk.ViewState(
    latitude=-20.0,
    longitude=-45.0,
    zoom=4,
    pitch=0,
)

tooltip = {
    "html": "<b>Estado:</b> {State}<br/><b>Títulos:</b> {Titles}",
    "style": {
        "backgroundColor": "steelblue",
        "color": "white"
    }
}

r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip
)

st.pydeck_chart(r)
