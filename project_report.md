# IPL Ball-by-Ball Project Report

## 1. Project Title
IPL Ball-by-Ball Exploratory Data Analysis (EDA)

## 2. Objective
The goal of this project was to analyze IPL match and ball-by-ball data to understand player performance, bowling effectiveness, and match patterns. The analysis helps identify top performers, trends in scoring, and insights related to game flow.

## 3. Dataset
- Source: PostgreSQL database table `final_table`
- Data includes ball-by-ball records such as:
  - match information
  - batting details
  - bowling details
  - runs, extras, wickets, and match outcomes

## 4. Methodology
The project followed these major steps:
1. Connecting to the database and loading the dataset.
2. Cleaning and preparing data for analysis.
3. Performing batting analysis:
   - top run scorers
   - most fours and sixes
   - balls faced
   - dot balls
   - boundary percentage
4. Performing bowling analysis:
   - extra runs by bowler
   - balls bowled
   - runs conceded
   - economy rate
5. Exploring match flow and game trends.

## 5. Key Analysis Performed

### Batting Analysis
- Top scorers were identified using total runs scored by each batter.
- Players with the highest number of boundaries were analyzed.
- Strike rate and workload-related metrics were reviewed.

### Bowling Analysis
- Bowlers were analyzed based on total balls bowled and runs conceded.
- Economy rate was computed using:
  - economy rate = (runs conceded / balls bowled) × 6
- Bowlers with high bowling volume and better economy were highlighted.

### Match-Level Insights
- Match outcomes and performance trends were explored to understand game patterns.

## 6. Important Observations
- Some players consistently dominate the scoring charts.
- Boundary-heavy batters contribute significantly to match totals.
- Bowlers with a good balance of control and economy are important for team success.
- Match-level trends show that performances vary based on match conditions and team strategy.

## 7. Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- SQLAlchemy
- PostgreSQL
- Jupyter Notebook

## 8. Conclusion
The project successfully explored IPL ball-by-ball data and provided useful insights into batting, bowling, and overall match behavior. The analysis can be extended further with visualizations, player comparisons, season-wise trends, and predictive modeling.

## 9. Future Scope
- Add visual charts for batting and bowling performance.
- Compare seasons and teams.
- Build a dashboard for interactive insights.
- Use machine learning to predict match outcomes.
