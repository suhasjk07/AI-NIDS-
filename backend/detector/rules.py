def run_rules_on_flow(flow):
    if flow.get('packets',0) > 1000 and flow.get('bytes',0)/max(flow.get('packets',1),1) < 60:
        return {'type':'possible_flood','severity':'high','flow':flow,'msg':'possible flood or small-payload attack'}
    # placeholder for port-scan/failures (stateful logic would be required)
    return None
