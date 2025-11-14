thonpython
import json
from pathlib import Path

class Exporter:
    def export_json(self, data, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)