"""
Research Scope AI - Export Utilities
Exports research scopes, bibliographies, and landscape intelligence to Markdown, JSON, and text files.
"""
import json
import time
from pathlib import Path
from typing import Dict, Any, Optional
from config import EXPORT_DIR
from scope_generator import ResearchScope

class ExportManager:
    """Manages file exports for research scopes, literature cards, and matrices."""

    def __init__(self, export_dir: Path = EXPORT_DIR):
        self.export_dir = export_dir
        self.export_dir.mkdir(parents=True, exist_ok=True)

    def export_scope_markdown(self, scope: ResearchScope, custom_filename: Optional[str] = None) -> str:
        """Saves research scope as a formatted Markdown file."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        safe_title = "".join(c for c in scope.title[:30] if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
        filename = custom_filename or f"ResearchScope_{safe_title}_{timestamp}.md"
        file_path = self.export_dir / filename

        content = scope.to_markdown()
        file_path.write_text(content, encoding="utf-8")
        return str(file_path)

    def export_scope_json(self, scope: ResearchScope, custom_filename: Optional[str] = None) -> str:
        """Saves research scope as a JSON file."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        safe_title = "".join(c for c in scope.title[:30] if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
        filename = custom_filename or f"ResearchScope_{safe_title}_{timestamp}.json"
        file_path = self.export_dir / filename

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(scope.to_dict(), f, indent=2)
        return str(file_path)

# Global exporter instance
export_manager = ExportManager()
