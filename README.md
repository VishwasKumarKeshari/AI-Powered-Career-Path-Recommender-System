# Career Compass — AI-Powered Career Path Detector

This repository contains a small prototype app that suggests career paths based on structured inputs (degree, branch, skills) and natural-language descriptions.

Contents
- `app.py` — Streamlit app UI (Structured input + Natural Language matcher).
- `api.py` — (optional) FastAPI server example (not included by default).
- `train_model.py` — Trains a scikit-learn Pipeline and saves it to `models/career_classifier.pkl`.
- `nlp_module.py` — NLP matcher using `sentence-transformers`.
- `utils.py` — helper functions used by the training pipeline.
- `data/careers.csv` — small example dataset.
- `resources/resources.json` — learning resources mapped to careers.

Quickstart (local)
1. Create a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Train the pipeline (creates `models/career_classifier.pkl`):

```powershell
python train_model.py
```

4. Run the Streamlit app:

```powershell
streamlit run app.py
```

Notes
- Do NOT commit large binaries (like `models/`) unless you intentionally want to store them in Git LFS. By default `models/` is ignored in `.gitignore`.
- The NLP matcher uses `sentence-transformers` which will download model weights on first run — that may take time and require more disk space.
- This repo uses a small synthetic dataset for demonstration. For real use, expand `data/careers.csv` with more examples.

Deploying
- To deploy on Streamlit Community Cloud: push this repository to GitHub, then create a new app on share.streamlit.io pointing to `app.py` and the branch you pushed.
- If you prefer a backend API, consider using FastAPI and deploy on Render/Railway/Heroku.

Security
- The trained pipeline is pickled with `joblib`. Only load pickles you trust.

License & Credits
- Add your desired license file if you plan to publish this project.
