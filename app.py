# [Your Streamlit code here - or just run the cells you already have]
import streamlit as st
st.title("Predictive Maintenance")

%%writefile requirements.txt
streamlit
pandas
scikit-learn
joblib

%%writefile Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]

# 2. Re-Sync the Pipeline (The Bridge)
import os
os.makedirs('.github/workflows', exist_ok=True)
with open('.github/workflows/pipeline.yml', 'w') as f:
    f.write("""
name: Sync to Hugging Face Spaces
on: [push]
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: {fetch-depth: 0, lfs: true}
      - name: Push to hub
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          git remote add hf https://krishna8787:${{ env.HF_TOKEN }}@huggingface.co/spaces/krishna8787/PredictiveMaintenance
          git push --force hf HEAD:main
""")

# 3. The Final Push (The 9-Symmetry Strike)
!git add app.py requirements.txt Dockerfile .github/ .gitignore
!git commit -m "FinalPush"
!git push origin main --force
