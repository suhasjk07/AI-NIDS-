import os, joblib, numpy as np
from sklearn.ensemble import IsolationForest
from .train import generate_synthetic_flows

MODEL_PATH = '/tmp/nids_model.joblib'

class AnomalyDetector:
    def __init__(self, model):
        self.model = model

    @classmethod
    def load_or_train(cls):
        if os.path.exists(MODEL_PATH):
            m = joblib.load(MODEL_PATH)
            return cls(m)
        X = generate_synthetic_flows(2000)
        m = IsolationForest(contamination=0.01, random_state=42)
        m.fit(X)
        joblib.dump(m, MODEL_PATH)
        return cls(m)

    def predict_flow(self, flow):
        x = np.array([[flow.get('bytes',0), flow.get('packets',0), flow.get('duration',1.0), flow.get('bytes',0)/max(flow.get('packets',1),1)]])
        score = float(self.model.decision_function(x)[0])
        is_anom = int(self.model.predict(x)[0]) == -1
        return score, bool(is_anom)
