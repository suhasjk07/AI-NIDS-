# AI NIDS+ (Demo Repo)

This repository contains a runnable demo of AI NIDS+ — a hybrid network intrusion detection system.

Quick start (local):

1. Create a python venv and install requirements:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```
2. Run the backend:

   ```bash
   python backend/app/main.py
   ```

3. Open http://localhost:8000 in your browser, upload a PCAP and watch alerts.

Notes:
- This is a demo-ready repo. For production, add authentication, better flow extraction,
  and a more sophisticated ML model (e.g., PyTorch autoencoder).
