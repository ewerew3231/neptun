import csv
from io import StringIO
import json

def export_tracks_to_csv():
    """
    Экспортирует все треки (messages.json) в формате CSV.
    """
    try:
        with open('messages.json', encoding='utf-8') as f:
            tracks = json.load(f)
    except Exception:
        tracks = []
        
    if not tracks:
        return ('No data', 204)
    
    # Определяем все возможные ключи
    all_keys = set()
    for track in tracks:
        all_keys.update(track.keys())
    all_keys = sorted(all_keys)
    
    # Создаем CSV в памяти
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=all_keys, extrasaction='ignore')
    writer.writeheader()
    
    for track in tracks:
        writer.writerow(track)
    
    csv_data = output.getvalue()
    output.close()
    
    headers = {
        'Content-Type': 'text/csv; charset=utf-8',
        'Content-Disposition': 'attachment; filename=tracks.csv'
    }
    return csv_data, 200, headers
