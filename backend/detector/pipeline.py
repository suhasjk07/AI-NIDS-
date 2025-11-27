from .rules import run_rules_on_flow
from .ml_model import AnomalyDetector
from db.alert_store import save_alert
from extractor import extract_flows_from_pcap

model = AnomalyDetector.load_or_train()

def process_pcap_upload(pcap_path: str):
    flows = extract_flows_from_pcap(pcap_path)
    for flow in flows:
        rule_alert = run_rules_on_flow(flow)
        if rule_alert:
            save_alert(rule_alert)
            continue
        score, is_anom = model.predict_flow(flow)
        if is_anom:
            alert = {
                'type': 'anomaly',
                'severity': 'medium',
                'score': float(score),
                'flow': flow,
                'msg': 'anomalous flow detected by model'
            }
            save_alert(alert)
