from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
from detector.pipeline import process_pcap_upload
from db.alert_store import init_db, get_alerts
import os

app = FastAPI(title="AI NIDS+")

@app.on_event("startup")
async def startup_event():
    init_db()

@app.post('/upload_pcap')
async def upload_pcap(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    contents = await file.read()
    # write to temp file
    path = f"/tmp/{file.filename}"
    with open(path, 'wb') as f:
        f.write(contents)
    background_tasks.add_task(process_pcap_upload, path)
    return JSONResponse({'status': 'accepted', 'file': file.filename})

@app.get('/alerts')
async def list_alerts():
    return get_alerts()

@app.get('/')
async def index():
    # serve static frontend index
    here = os.path.dirname(__file__)
    static_index = os.path.join(here, '..', 'static', 'index.html')
    return FileResponse(static_index, media_type='text/html')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
