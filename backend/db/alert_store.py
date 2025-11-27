import sqlite3, json
DB='/tmp/nids_alerts.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY AUTOINCREMENT, ts DATETIME DEFAULT CURRENT_TIMESTAMP, type TEXT, severity TEXT, data TEXT)''')
    conn.commit(); conn.close()

def save_alert(alert: dict):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    severity = alert.get('severity','medium')
    c.execute('INSERT INTO alerts (type,severity,data) VALUES (?,?,?)', (alert.get('type'), severity, json.dumps(alert)))
    conn.commit(); conn.close()

def get_alerts():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT id,ts,type,severity,data FROM alerts ORDER BY ts DESC LIMIT 200')
    rows = c.fetchall(); conn.close()
    out = []
    for r in rows:
        out.append({'id':r[0],'ts':r[1],'type':r[2],'severity':r[3],'data':r[4]})
    return out
