# AI NIDS+ — Hybrid Network Intrusion Detection (Demo)

**AI NIDS+** is a compact, demo-ready hybrid Network Intrusion Detection System that combines explainable rule-based detection with unsupervised ML anomaly detection. It's designed to be interview-friendly: easy to run, demo live, and extend.

## Highlights
- PCAP ingestion (upload via web UI)
- Rule-based detectors (high-confidence alerts)
- Unsupervised ML (IsolationForest) for stealthy anomalies
- Lightweight React dashboard for live demo
- Dockerfile and docker-compose for quick local deploy

## Demo goals
Build something you can demo in 3–5 minutes:
1. Upload a PCAP (port-scan or flood sample)
2. Show alert appear in the dashboard
3. Inspect alert detail and explain why it fired

## Quickstart (local)
```bash
git clone <your-repo-url>
cd ai_nids_plus_repo
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
python backend/app/main.py
```
Then open http://localhost:8000 and upload a PCAP.

## Polished README & LICENSE included
This package includes a ready-to-run demo and helper scripts to publish the repo to GitHub (see `publish_repo.sh`).

## Contributing
- Add better flow extraction (biflow, timestamps)
- Replace IsolationForest with PyTorch autoencoder
- Add authentication and secure file upload

## License
MIT — see LICENSE file
