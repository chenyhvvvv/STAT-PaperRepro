"""Mock session objects for pipeline testing (no h5ad loading needed)."""
from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Any


@dataclass
class MockSlice:
    """Minimal slice mock for SkillFilter compatibility."""
    slice_id: int
    modality: str
    data_level: str
    n_obs: int = 5000
    n_vars: int = 500
    _has_celltype: bool = False
    celltypes: List[str] = field(default_factory=list)
    tissue_name: str = "tissue"
    image_names: List[str] = field(default_factory=list)
    columns: List[str] = field(default_factory=list)

    @property
    def is_spot_level(self):
        return self.data_level == "spot"

    @property
    def is_cell_level(self):
        return self.data_level == "cell"

    def has_celltype(self):
        return self._has_celltype

    def get_summary(self):
        summary = {
            'slice_id': self.slice_id,
            'modality': self.modality,
            'data_level': self.data_level,
            'data_level_detection': 'mock',
            'n_obs': self.n_obs,
            'n_vars': self.n_vars,
            'has_celltype': self._has_celltype,
            'celltypes': self.celltypes if self._has_celltype else [],
            'has_celltype_colors': False,
            'image_count': len(self.image_names),
            'image_names': self.image_names,
            'image_match': 'mock',
            'tissue_name': self.tissue_name,
        }
        if self.is_spot_level:
            summary['has_deconv_weights'] = False
        return summary


class MockSession:
    """Minimal session mock for SkillFilter and PipelineExecutor compatibility."""

    def __init__(self, name: str, slices: Dict[int, MockSlice]):
        self.name = name
        self.slices = slices
        self.has_data = True

    @property
    def n_slices(self):
        return len(self.slices)

    @property
    def slice_ids(self):
        return sorted(self.slices.keys())

    @property
    def modalities(self):
        return list(set(s.modality for s in self.slices.values()))

    @property
    def data_levels(self):
        return list(set(s.data_level for s in self.slices.values()))

    def get_slice(self, slice_id):
        return self.slices.get(slice_id)

    def get_summary(self):
        return {
            'name': self.name,
            'n_slices': self.n_slices,
            'slice_ids': self.slice_ids,
            'modalities': self.modalities,
            'data_levels': self.data_levels,
            'slices': [s.get_summary() for s in self.slices.values()],
            'n_rois': 0,
            'rois': [],
        }


def build_sessions_from_json(queries_file: Path) -> Dict[str, MockSession]:
    """Build mock sessions from pipeline_test_queries.json definitions."""
    with open(queries_file) as f:
        data = json.load(f)

    sessions = {}
    for session_id, sess_def in data["sessions"].items():
        slices = {}
        for sl in sess_def["slices"]:
            slices[sl["slice_id"]] = MockSlice(
                slice_id=sl["slice_id"],
                modality=sl["modality"],
                data_level=sl["data_level"],
                n_obs=sl.get("n_obs", 5000),
                n_vars=sl.get("n_vars", 500),
                _has_celltype=sl.get("has_celltype", False),
                celltypes=sl.get("celltypes", []),
                tissue_name=sl.get("tissue_name", f"slice_{sl['slice_id']}"),
                image_names=sl.get("image_names", []),
                columns=sl.get("columns", []),
            )
        sessions[session_id] = MockSession(name=session_id, slices=slices)

    return sessions
