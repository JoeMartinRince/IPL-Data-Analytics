# IPL Data Analytics Dashboard

> An interactive, data-driven web application designed to analyze, visualize, and extract historical insights from Indian Premier League (IPL) cricket matches spanning 2008 to 2020. Built with **Python**, **Pandas**, **Streamlit**, **Matplotlib**, and **Seaborn**.

The **IPL Data Analytics Dashboard** provides cricket analysts, enthusiasts, and developers with an intuitive interface to explore franchise win statistics, all-time batting milestones, toss decision impacts, and longitudinal season trends across over a decade of high-octane T20 cricket.

## Project Overview

The Indian Premier League (IPL) is among the most competitive and widely followed T20 cricket leagues globally. Over the course of twelve-plus editions, teams, players, and match conditions have produced extensive datasets capturing match outcomes, individual milestones, venue dynamics, and tactical decisions.

This project delivers an interactive analytical dashboard that transforms multi-season match records and delivery-level ball-by-ball event data into clear, actionable visual summaries. By bridging raw sports data with exploratory data analysis (EDA) techniques, users can quickly identify dominant franchises, evaluate scoring masterclasses, investigate the tactical advantage of winning the toss, and track how match schedules evolved from the inaugural 2008 season through 2020.

## Purpose of IPL Data Analytics

Modern cricket has evolved from purely intuitive decision-making into an evidence-based discipline heavily reliant on data analytics. In a tournament format as dynamic and high-stakes as the IPL, statistical exploration serves multiple critical functions:

- **Performance Benchmarking:** Quantifies franchise consistency and individual player output across different tournament eras and venues.
- **Strategic Validation:** Empirically tests widespread cricketing axioms, such as whether winning the coin toss provides a decisive statistical advantage.
- **Talent & Impact Evaluation:** Highlights batting run-accumulation leaders and power hitters who reliably convert scoring opportunities into boundaries.
- **Accessible Insights:** Translates dense tabular records containing thousands of delivery events into clean, interpretable visual representations for analysts, coaches, and sports enthusiasts alike.

## Project Objectives

The project is structured around five core engineering and analytical objectives:

1. **Structured Data Ingestion:** Seamlessly process match-level and ball-by-ball delivery records from CSV format into optimized Pandas DataFrames.
2. **Automated Metric Computation:** Programmatically calculate key tournament metrics including cumulative franchise wins, top ten batting run aggregates, toss win-to-match win correlation percentages, and individual boundary tallies.
3. **Interactive User Filtering:** Enable dynamic slicing of match history through a sidebar dropdown filter to examine team-specific victories, seasons, and host venues.
4. **Intuitive Visual Presentation:** Render clear, labeled, and styled charts using Seaborn and Matplotlib integrated directly into Streamlit's reactive web framework.
5. **Reproducible Local Deployment:** Maintain a streamlined, reproducible environment executable with standard Python virtual environment tooling.

## Key Highlights

- **Dynamic Sidebar Filtering:** Real-time dropdown selection of IPL teams dynamically filters match results with venue and season context.
- **Franchise Dominance Breakdown:** Bar charts visually ranking cumulative match wins across all franchises throughout IPL history.
- **Elite Batting Leaderboards:** Granular aggregation revealing the top 10 all-time run scorers and top 10 six hitters.
- **Empirical Toss Correlation:** Instant statistical banner displaying the win percentage of teams that won the coin toss.
- **Season Match Progression:** Visual timeline charting the expansion and variations in total match counts per season.
- **Streamlined Architecture:** Pure Python stack with zero heavy database overhead, executing directly in the local browser.

## Features

The dashboard encompasses six core analytical features designed to provide deep visual and numerical perspectives on IPL history:

- **Interactive Team-Specific Match Inspector:** Allows users to filter matches won by any franchise from the sidebar dropdown, presenting historical records including season, winner, and venue.
- **Franchise Victory Analytics:** Generates frequency-sorted bar plots showing cumulative victories for all participating IPL teams.
- **All-Time Top Run Scorers:** Computes cumulative runs across all tournament deliveries to rank the top 10 batting leaders in IPL history.
- **Toss Impact Analysis:** Evaluates the tactical significance of winning the coin toss by computing the exact win-rate percentage of toss-winning teams.
- **Season Match Progression Trends:** Charts chronological changes in the number of matches conducted in each tournament edition from 2008 to 2020.
- **Power-Hitting & Boundary Analysis:** Aggregates delivery data where `batsman_runs == 6` to identify and rank the top 10 six-hitting batsmen.

### Top Winning Teams Analysis

The dashboard analyzes cumulative match outcomes across all tournament seasons to rank franchises by total victories:
- **Data Source:** Extracted from the `winner` attribute in `matches.csv`.
- **Computation:** Employs Pandas frequency counting (`matches['winner'].value_counts()`) to aggregate and sort match victories in descending order.
- **Visualization:** Rendered as a Seaborn bar chart (`sns.barplot`), clearly illustrating the historical dominance of perennial powerhouses like Mumbai Indians, Chennai Super Kings, and Kolkata Knight Riders.
- **Readability:** Team names are rotated along the x-axis to prevent label overlap and ensure crisp rendering across varying screen resolutions.

### Top Run Scorers Analysis

Player scoring achievements are analyzed across tens of thousands of delivery events:
- **Data Source:** Ingested from `deliveries.csv` utilizing `batter` and `batsman_runs` columns.
- **Computation:** Grouped by batter using `deliveries.groupby('batter')['batsman_runs'].sum()`, sorted in descending order, and filtered using `.head(10)`.
- **Insights:** Highlights premier batting stalwarts across IPL history (e.g., Virat Kohli, Suresh Raina, Rohit Sharma, David Warner, and Shikhar Dhawan).
- **Visualization:** Displayed through a dedicated Seaborn bar chart with 45-degree tick label rotation and labeled run totals.

### Toss Impact on Match Results

A central debate in cricket strategy revolves around the importance of winning the coin toss:
- **Theoretical Context:** Toss-winning captains frequently elect to field first or bat first according to ground dew factors, pitch deterioration, and target-chasing dynamics.
- **Analytical Method:** Filters matches where the toss winner coincides with the match winner (`matches['toss_winner'] == matches['winner']`).
- **Mathematical Formulation:** 
  $$\text{Toss Win Conversion Rate (\%)} = \left(\frac{\text{Matches won by toss winner}}{\text{Total matches played}}\right) \times 100$$
- **UI Presentation:** Rendered prominently as a styled Streamlit success banner (`st.success`), highlighting that toss winners converted to match winners approximately 52% of the time, debunking assumptions of overwhelming toss bias.

### Season-Wise Match Trends

The annual volume of IPL fixtures reflects tournament expansion, franchise inclusions, and scheduling format changes:
- **Chronological Sorting:** Uses `matches['season'].value_counts().sort_index()` to track total matches conducted during each edition.
- **Visual Encoding:** Plotted using a connected Seaborn line plot (`sns.lineplot`) with explicit point markers (`marker='o'`).
- **Observations:** Clearly visualizes peak seasons (e.g., 2011–2013 with 70+ fixtures during franchise expansion) versus standard 8-team 60-match formats.

### Interactive Team Filtering & Match Drilldown

The dashboard features an interactive sidebar designed for focused franchise inquiry:
- **Sidebar Selection:** Built using `st.sidebar.selectbox` populated with unique winning team names: `matches['winner'].dropna().unique()`.
- **Dynamic Data Filtering:** Filters match records where `matches['winner'] == selected_team`.
- **Match Table Drilldown:** Renders the first 10 match victories with key attributes (`season`, `winner`, `venue`) directly in the main interface.
- **Boundary Power-Hitters Complement:** Accompanied by a dedicated analysis of the top 10 six-hitting batsmen (`deliveries[deliveries['batsman_runs'] == 6]`), highlighting power hitters like Chris Gayle, AB de Villiers, and Rohit Sharma.

## Tech Stack
- Python
- Pandas
- Streamlit
- Matplotlib
- Seaborn

## Dataset
Dataset used:
https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020

## Run Locally

```bash
streamlit run app.py
```
