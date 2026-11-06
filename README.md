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

## Features
- Top winning teams
- Top run scorers
- Toss impact analysis
- Season-wise trends
- Interactive team filtering

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
