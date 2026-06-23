##Project Title
I made a  IPL data project to explore ball-by-ball data and try simple predictions.

##Overview
This is a  project with EDA and basic models to learn from IPL match data.

##Problem
I looked at ball-by-ball data to find which things affect match results.

##
Dataset
- Ball-by-ball IPL data (CSV) — update with source and date range.

##Tools
- n8n for AI aotumations
- Python, pandas, matplotlib/seaborn
- scikit-learn (simple models), Jupyter Notebook

##What I did
- Cleaned data and made simple features
- Plotted key charts for trends
- Built a basic model and checked scores

##Main findings (short)
- Top features: (e.g., runs in last 6 balls, wickets)
- Some teams/players show consistent patterns

##Outputs
- Notebooks: `EDA_ballbyball.ipynb`
- Model files (if saved): put in `models/` folder

##AI Agent (Chatbot)
I also made a simple AI chatbot that answers questions about the IPL data. It connects to the project database (example: `db/data.db` or a Postgres instance) and fetches facts or summaries from cleaned data.

Files (example): `agent/agent.py`, `agent/README.md`, `db/` (database files)

Run agent (example):

```powershell
# make sure database is available, then:
python agent\agent.py
```

Conclusion
This project is a learning exercise. Results are simple but show useful patterns using AI chatbot. 

Author & Contact
-vansh kumar — vk165278@gmail.com

