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

## Dataset Architecture & Overview

The analytical pipeline is powered by two complementary tabular datasets stored in CSV format, capturing both high-level match outcomes and atomic delivery events:

1. **`matches.csv` (Match-Level Records):** Encapsulates macro match-level metadata across every fixture, including season edition, participating teams, toss decisions, venue locations, and match winners.
2. **`deliveries.csv` (Ball-by-Ball Records):** Provides granular micro-level event logging for each delivery bowled in the tournament, recording bowler actions, batsman runs scored, extra runs, and wicket dismissals.

### Dataset Source & Provenance

- **Origin:** Curated and published on Kaggle by Patrick B ([IPL Complete Dataset (2008-2020)](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)).
- **Primary Lineage:** Aggregated from official BCCI match scorecards, Cricsheet ball-by-ball logs, and historical sports statistics archives.
- **Licensing & Usage:** Freely accessible under open data licensing for educational and non-commercial sports data analytics research.
- **File Pairing:** Designed to be loaded side-by-side in the repository root directory as `matches.csv` and `deliveries.csv`.

### Historical Coverage & Scope

- **Temporal Range:** Covers 13 consecutive seasons from the inaugural tournament in 2008 through the 2020 tournament edition.
- **Match Universe:** Comprises over 800 sanctioned T20 matches played across Indian stadiums and neutral overseas venues (including South Africa in 2009 and the UAE in 2014 & 2020).
- **Delivery Universe:** Exceeds 193,000 recorded delivery events, capturing runs scored, extras, and individual player actions.
- **Franchise Evolution:** Encompasses both foundation franchises (e.g., MI, CSK, KKR, RCB, RR, KXIP, DC) and historical transient franchises (e.g., Deccan Chargers, Pune Warriors, Gujarat Lions, Rising Pune Supergiant, Kochi Tuskers Kerala, and Sunrisers Hyderabad).

### Schema & Primary Feature Columns

The dashboard specifically references the following critical attributes across the two data files:

| Dataset | Column Name | Data Type | Analytical Usage in Project |
| :--- | :--- | :--- | :--- |
| `matches.csv` | `season` | `int64` / `object` | Chronological aggregation for season-wise match counts. |
| `matches.csv` | `winner` | `object` | Computing franchise win counts and driving team filter options. |
| `matches.csv` | `venue` | `object` | Displayed in match detail tables for selected teams. |
| `matches.csv` | `toss_winner` | `object` | Evaluated against `winner` for toss victory correlation. |
| `deliveries.csv` | `batter` | `object` | Grouping key for career run sums and six-hitting leaderboards. |
| `deliveries.csv` | `batsman_runs` | `int64` | Aggregated for total runs and filtered (`== 6`) for six-hitters. |

## Data Preprocessing Pipeline

Raw sports tracking datasets often feature missing values, abandoned matches (no results), and varying string naming formats. The preprocessing architecture in `app.py` ensures reliable runtime execution through the following pipeline:

- **Ingestion & In-Memory Loading:** Datasets are read at runtime via `pd.read_csv("matches.csv")` and `pd.read_csv("deliveries.csv")`.
- **Targeted Subsetting:** Specific features required for analytical views are isolated dynamically rather than duplicated in memory.
- **Dataset Partitioning:** Queries on team results and season trends reference `matches`, while player-level performance metrics reference `deliveries`.

### Data Cleaning & Handling Missing Values

- **Handling Null Match Winners:** Weather disruptions or abandoned games leave `winner` blank (`NaN`). In `app.py`, calling `matches['winner'].dropna().unique()` prevents null values from entering the team selection widget.
- **Exclusion of Non-Result Matches:** Aggregations with `.value_counts()` automatically ignore missing values, ensuring win statistics are accurately representative of completed matches.
- **Exact Boundary Filtering:** Power-hitting analytics rigorously filter deliveries where `deliveries['batsman_runs'] == 6`, guaranteeing that extra runs (e.g., overthrows or leg-byes) do not inflate individual boundary statistics.

### Pandas Analytical Computation Workflow

The dashboard leverages core Pandas primitives to perform complex transformations with high computational efficiency:

1. **Vectorized Boolean Masking:** Used in filtering matches by selected team (`matches[matches['winner'] == selected_team]`), toss correlation (`matches['toss_winner'] == matches['winner']`), and boundary filtering (`deliveries['batsman_runs'] == 6`).
2. **Frequency Distribution Computation:** `value_counts()` executes fast, single-pass hash-based counting for categorical franchise victories.
3. **Split-Apply-Combine Aggregation:** `deliveries.groupby('batter')['batsman_runs'].sum()` groups ball records by batsman name, aggregates numeric run tallies, and sorts outputs via `.sort_values(ascending=False)`.
4. **Index Sorting for Time Series:** `.sort_index()` maintains sequential order when counting occurrences across chronological tournament years.

### Calculation Methodology: Winning Teams

The calculation of winning teams in `app.py` is implemented concisely and efficiently:

```python
team_wins = matches['winner'].value_counts()
```

- **Mechanism:** Pandas constructs an internal hash table over the `winner` column, tabulating occurrences while skipping `NaN` entries.
- **Output Structure:** Yields a Pandas `Series` where `team_wins.index` holds franchise identifiers and `team_wins.values` represents total historical wins.
- **Automatic Ranking:** Because `.value_counts()` sorts in descending order by default, the most victorious teams appear first, allowing direct plotting without additional sorting steps.

### Calculation Methodology: Top Run Scorers & Boundary Hitters

Player scoring metrics are derived via two targeted multi-stage Pandas operations:

```python
# 1. Total Career Runs
top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)

# 2. Total Career Sixes
sixes = deliveries[deliveries['batsman_runs'] == 6]
top_six_hitters = sixes.groupby('batter').size().sort_values(ascending=False).head(10)
```

- **Batter Aggregation:** The dataset partitions records by unique batter tokens, summing solely `batsman_runs` so extras (wides, no-balls, leg-byes) are excluded from the player's personal score.
- **Boundary Subsetting:** `sixes` isolates all rows where the batsman hit a 6, then `.size()` groups by `batter` to count total boundary clearances before sorting and truncating to the top 10.

### Calculation Methodology: Toss Decision Correlation

The dashboard evaluates whether winning the coin toss translates into winning the cricket match:

```python
toss_match_win = matches[matches['toss_winner'] == matches['winner']]
percentage = (len(toss_match_win) / len(matches)) * 100
st.success(f"Teams winning the toss also won the match {percentage:.2f}% of the time.")
```

- **Vectorized Equality Evaluation:** `matches['toss_winner'] == matches['winner']` performs an element-wise row comparison between toss winners and match winners.
- **Cardinality Ratio:** `len(toss_match_win)` captures the count of matches where the condition holds true, divided by `len(matches)` representing all recorded tournament encounters.
- **Metric Presentation:** Scaled to a percentage and formatted to two decimal precision, outputting an empirical rate (~52%) illustrating that the toss grants only a marginal advantage in IPL T20 history.

### Calculation Methodology: Season-Wise Match Progression

The dashboard analyzes tournament edition volume across time:

```python
matches_per_season = matches['season'].value_counts().sort_index()
```

- **Edition Frequency Count:** `matches['season'].value_counts()` computes total matches played per season.
- **Index Reordering:** `.sort_index()` sorts entries in chronological sequence by year rather than descending match counts.
- **Coordinates:** `matches_per_season.index` maps to season years (x-axis) and `matches_per_season.values` maps to match totals (y-axis), feeding directly into the time-series line chart.

## Data Visualization Architecture

The dashboard visualizes complex statistical aggregates into accessible, presentation-ready charts through integration with Streamlit:

- **Component Encapsulation:** Every visual artifact is instantiated as a distinct Matplotlib Figure (`fig, ax = plt.subplots(...)`) to avoid state pollution between visualizations.
- **Direct Web Mounting:** Visualizations are injected into Streamlit's web DOM using `st.pyplot(fig)`.
- **Responsive Dimensions:** Proportions (`figsize=(10,5)` and `figsize=(12,6)`) are calibrated to ensure clarity on diverse display screens.
- **Layout Optimization:** Calls to `plt.tight_layout()` ensure axis titles and rotated tick marks are never clipped by viewport margins.

### Matplotlib Implementation & Configuration

Matplotlib (`matplotlib.pyplot`) serves as the foundational rendering backend across all figures:

- **Figure & Subplot Instantiation:** Using `plt.subplots(figsize=(10,5))` and `plt.subplots(figsize=(12,6))` isolates canvas contexts, preventing chart overlapping during Streamlit reruns.
- **Axis Labeling:** Explicitly configures readable labels (`plt.ylabel("Wins")`, `plt.ylabel("Runs")`, `plt.ylabel("Matches")`, `plt.ylabel("Number of Sixes")`, `plt.xlabel("Teams")`).
- **Rotated Tick Labels:** `plt.xticks(rotation=45, ha='right')` aligns long franchise and player names at a 45-degree slant to maintain clean spacing.
- **Padding Control:** `plt.tight_layout()` automatically adjusts spacing around subplot perimeters.

### Seaborn Statistical Theming & Plot Types

Seaborn (`seaborn as sns`) delivers polished, publication-ready aesthetics atop Matplotlib:

- **Categorical Bar Plots (`sns.barplot`):** Applied to visualize franchise wins (`x=team_wins.index, y=team_wins.values`), top run scorers (`x=top_batsmen.index, y=top_batsmen.values`), and boundary leaders (`x=top_six_hitters.index, y=top_six_hitters.values`).
- **Time-Series Progression (`sns.lineplot`):** Deployed for matches per season (`x=matches_per_season.index, y=matches_per_season.values, marker='o'`), highlighting year-over-year tournament schedule shifts.
- **Axes Targeting:** Passing `ax=ax` explicitly binds Seaborn's high-level statistical plotting routines into the active Matplotlib Axes instance.

## Streamlit Dashboard Architecture

The dashboard is built on Streamlit's declarative, reactive application framework:

- **Reactive Execution Cycle:** Every widget event (such as selecting a new team in the sidebar) triggers an immediate top-to-bottom re-execution of `app.py`, dynamically refreshing filtered match tables and views while preserving fast runtime speed.
- **Layout Partitioning:** 
  - **Sidebar Region (`st.sidebar`):** Dedicated control area hosting the interactive franchise selector (`st.sidebar.selectbox`).
  - **Main Content Region:** Sequentially lays out introductory commentary, tabular drilldowns, statistical banners (`st.success`), and Matplotlib figure canvases (`st.pyplot`).
- **Zero Frontend Overhead:** Does not require HTML templates, CSS builds, or JavaScript client-server synchronization, enabling pure Python full-stack sports analytics.

## Tech Stack

The application leverages Python's scientific and analytical ecosystem:

| Technology | Category | Purpose in Project |
| :--- | :--- | :--- |
| **Python** | Core Language | Runtime language providing the execution environment for data structures and scripts. |
| **Pandas** | Data Wrangling | Ingestion of CSV files, DataFrame filtering, grouping (`groupby`), and aggregation (`sum`, `size`, `value_counts`). |
| **Streamlit** | Web Application Framework | Interactive UI rendering, sidebar selectbox widget controls, success callout banners, and reactive dashboard state management. |
| **Matplotlib** | Visualization Backend | Figure and canvas lifecycle management (`plt.subplots`), custom axis titles, tick rotation, and margin adjustments (`tight_layout`). |
| **Seaborn** | Statistical Data Visualization | High-level aesthetic charts including categorical bar plots (`sns.barplot`) and chronological line plots (`sns.lineplot`). |
| **NumPy** | Numerical Computing | Vectorized array operations and numerical support underlying Pandas Series calculations. |

## Project Directory Structure

The repository maintains a clean, minimal file layout:

```text
IPL-Data-Analytics/
├── .gitignore               # Excludes raw CSV datasets and Python bytecode
├── README.md                # Comprehensive project documentation and guides
├── requirements.txt         # Runtime Python package dependencies
├── app.py                   # Main Streamlit application and analytics pipeline
├── Screenshots/             # Application preview captures and charts
│   ├── Screenshot 2026-05-17 195209.png
│   ├── Screenshot 2026-05-17 195233.png
│   ├── Screenshot 2026-05-17 195311.png
│   ├── Screenshot 2026-05-17 195340.png
│   └── Screenshot 2026-05-17 195357.png
└── [Data Files - External / Downloaded]
    ├── matches.csv          # Match metadata (downloaded separately)
    └── deliveries.csv       # Ball-by-ball records (downloaded separately)
```

## Installation & Setup Guide

### System Prerequisites & Python Requirements

Prior to running the dashboard locally, ensure your environment meets the following requirements:

- **Python Version:** Python 3.8 or higher (tested on Python 3.8, 3.9, 3.10, and 3.11).
- **Package Manager:** `pip` (Python package installer) up to date.
- **Operating System:** Platform-independent (fully functional on Windows 10/11, macOS, and Linux distributions).
- **Hardware Resources:** Minimum 2 GB RAM recommended to process and cache the 190,000+ delivery rows smoothly.

### Virtual Environment Setup

Isolating dependencies within a dedicated virtual environment prevents version collisions:

```bash
# 1. Create a virtual environment named 'venv'
python -m venv venv
```

Activate the environment based on your operating system:

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
- **macOS / Linux (Bash / Zsh):**
  ```bash
  source venv/bin/activate
  ```

### Dependency Installation

Install all required third-party libraries using the project's pinned manifest:

```bash
# Upgrade pip to latest version
python -m pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

Verify that all dependencies were installed properly:

```bash
python -c "import streamlit, pandas, matplotlib, seaborn, numpy; print('All dependencies imported successfully!')"
```

### Dataset Placement & Local Preparation

The application relies on two CSV files loaded from the current working directory:

1. Download the dataset files from Kaggle: [IPL Complete Dataset (2008-2020)](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020).
2. Unpack and place `matches.csv` and `deliveries.csv` directly in the project root directory alongside `app.py`:
   ```bash
   # Confirm files are present in the project root
   # Windows (PowerShell):
   Test-Path matches.csv, deliveries.csv
   
   # macOS / Linux:
   ls matches.csv deliveries.csv
   ```
3. Because both files are listed in `.gitignore`, Git will protect them from being committed into repository version control.

## Run Locally

Launch the application using Streamlit's command-line interface:

```bash
streamlit run app.py
```

Upon successful startup, Streamlit provides local and network network URLs in your terminal:

```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### Custom Startup Options

- **Specify Custom Port:**
  ```bash
  streamlit run app.py --server.port 8080
  ```
- **Run in Headless Mode (e.g., remote server or Docker container):**
  ```bash
  streamlit run app.py --server.headless true
  ```

## User Guide & Dashboard Navigation

When the dashboard opens in your browser (`http://localhost:8501`), users encounter a structured analytical interface:

1. **Header & Context:** Introduces the scope of the exploratory dashboard.
2. **Interactive Sidebar:** Located on the left pane, allowing instant filtering by IPL franchise.
3. **Filtered Matches Record:** Displays tabular data containing the season, winner, and venue for the selected team's matches.
4. **All-Time Franchise Wins Chart:** Visualizes cumulative win totals across all IPL franchises in descending order.
5. **Top Run Scorers Leaderboard:** Visualizes the top 10 batsmen with highest aggregate runs scored.
6. **Toss Outcome Metric Banner:** Features the empirical percentage of toss winners winning matches.
7. **Matches Per Season Timeline:** Depicts the volume trajectory of matches over time.
8. **Top Six Hitters Leaderboard:** Highlights the top 10 boundary clearers in tournament history.

### Step-by-Step Instructions for Using Team Filters

1. **Access the Sidebar:** Click the sidebar area titled **"Filter"** on the left side of the screen (or tap the `>` arrow icon if collapsed on smaller screens).
2. **Select a Franchise:** Click the **"Select Team"** dropdown menu to reveal the full list of historical IPL franchises.
3. **Trigger Reactive Filtering:** Select any team (e.g., *Mumbai Indians*, *Chennai Super Kings*, or *Kolkata Knight Riders*). Streamlit will instantly re-filter the DataFrame.
4. **Review Match Outing Details:** Examine the rendered table under **"Matches Won by [Team]"**, which details the season, winner confirmation, and host venue for the first 10 recorded victories.
5. **Switch Between Teams:** Choose any other franchise at any time to immediately update the drilldown table without a full browser refresh.

## Troubleshooting & FAQs

| Issue / Error | Potential Cause | Verified Resolution |
| :--- | :--- | :--- |
| `FileNotFoundError: matches.csv` or `deliveries.csv` | Dataset files are not located in the current working directory from where `streamlit run` was launched. | Download datasets from Kaggle and ensure `matches.csv` and `deliveries.csv` are in the same folder as `app.py`. |
| `ModuleNotFoundError: No module named 'streamlit'` | Virtual environment is inactive or packages have not yet been installed. | Activate your virtual environment and run `pip install -r requirements.txt`. |
| `Port 8501 is already in use` | Another local Streamlit application instance is already executing on port 8501. | Launch on a different port using `streamlit run app.py --server.port 8502`. |
| PowerShell Execution Policy error on `Activate.ps1` | Windows PowerShell restricts running third-party activation scripts by default. | Execute `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell. |
| High RAM consumption on startup | Loading 190,000+ ball rows simultaneously. | Ensure machine has at least 2 GB free memory; close background processes if running in low-resource environments. |
