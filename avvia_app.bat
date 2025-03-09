@echo off
start /B streamlit run app.py --server.headless=true --server.port=8501
timeout /t 5
start http://localhost:8501
