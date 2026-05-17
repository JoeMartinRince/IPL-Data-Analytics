import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load datasets
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# Title
st.title("IPL Data Analytics Dashboard")
st.write("""
This dashboard analyzes IPL match and player statistics using data visualization and interactive filtering.
""")

st.write("## IPL Match Insights Dashboard")
st.write("Explore team performance, player statistics, and match trends across IPL seasons.")

st.sidebar.title("Filter")

selected_team = st.sidebar.selectbox(
    "Select Team",
    matches['winner'].dropna().unique()
)

filtered_matches = matches[matches['winner'] == selected_team]

st.write(f"## Matches Won by {selected_team}")

st.write(filtered_matches[['season', 'winner', 'venue']].head(10))

# Top winning teams
st.write("## Top Winning Teams")

team_wins = matches['winner'].value_counts()

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=team_wins.index, y=team_wins.values, ax=ax)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.xticks(rotation=90)
plt.ylabel("Wins")
plt.xlabel("Teams")

st.pyplot(fig)

# Top batsmen
st.write("## Top Run Scorers")

top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=top_batsmen.index, y=top_batsmen.values, ax=ax)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.xticks(rotation=45)
plt.ylabel("Runs")

st.pyplot(fig)
st.write("## Toss Impact on Match Results")

toss_match_win = matches[matches['toss_winner'] == matches['winner']]

percentage = (len(toss_match_win) / len(matches)) * 100

st.success(f"Teams winning the toss also won the match {percentage:.2f}% of the time.")

st.write("## Matches Played Per Season")

matches_per_season = matches['season'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(10,5))

sns.lineplot(
    x=matches_per_season.index,
    y=matches_per_season.values,
    marker='o',
    ax=ax
)

plt.xticks(rotation=45)
plt.ylabel("Matches")

st.pyplot(fig)

st.write("## Top Six Hitters")

sixes = deliveries[deliveries['batsman_runs'] == 6]

top_six_hitters = sixes.groupby('batter').size().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12,6))

sns.barplot(
    x=top_six_hitters.index,
    y=top_six_hitters.values,
    ax=ax
)

plt.xticks(rotation=45, ha='right')
plt.ylabel("Number of Sixes")

st.pyplot(fig)
