#!/usr/bin/env python3
"""Pós-processa os SVGs gerados pelo Pac-Man para aplicar paletas personalizadas."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Dict

from celebration_generator import DEFAULT_THEME, CELEBRATIONS, get_current_celebration
from pacman_themes import (
    BASE_GAME_THEME_COLORS,
    PacmanPalette,
    get_palette_for_theme,
)


REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist"

SVG_TARGETS = (
    ("pacman-contribution-graph.svg", "github"),
    ("pacman-contribution-graph-dark.svg", "github-dark"),
)


def _build_replacements(base_palette: PacmanPalette, target_palette: PacmanPalette) -> Dict[str, str]:
    replacements: Dict[str, str] = {
        base_palette.grid_background: target_palette.grid_background,
        base_palette.text_color: target_palette.text_color,
        base_palette.wall_color: target_palette.wall_color,
    }

    for base_color, target_color in zip(base_palette.intensity_colors, target_palette.intensity_colors):
        replacements[base_color] = target_color

    return replacements


def _replace_case_insensitive(content: str, old: str, new: str) -> str:
    pattern = re.compile(re.escape(old), flags=re.IGNORECASE)
    return pattern.sub(new.lower(), content)


def _apply_palette_to_file(svg_path: Path, base_palette: PacmanPalette, target_palette: PacmanPalette) -> bool:
    if not svg_path.exists():
        return False

    original_content = svg_path.read_text(encoding="utf-8")
    updated_content = original_content
    replacements = _build_replacements(base_palette, target_palette)

    for old_color, new_color in replacements.items():
        updated_content = _replace_case_insensitive(updated_content, old_color, new_color)

    if updated_content != original_content:
        svg_path.write_text(updated_content, encoding="utf-8")
        return True

    return False


def _resolve_active_theme(reference_date: datetime | None = None) -> str:
    celebration = get_current_celebration() if reference_date is None else None

    if reference_date is not None:
        month_day = (reference_date.month, reference_date.day)
        for celebration_data in CELEBRATIONS.values():
            if month_day in celebration_data["dates"]:
                return celebration_data["theme"]

    if celebration:
        return celebration["theme"]

    return DEFAULT_THEME


def main() -> None:
    if not DIST_DIR.exists():
        print("Nenhum diretório dist encontrado, nada a fazer.")
        return

    active_theme = _resolve_active_theme()
    target_palette = get_palette_for_theme(active_theme)

    print(f"Aplicando paleta '{active_theme}' aos SVGs do Pac-Man...")

    for file_name, base_theme in SVG_TARGETS:
        svg_path = DIST_DIR / file_name
        base_palette = BASE_GAME_THEME_COLORS[base_theme]

        if _apply_palette_to_file(svg_path, base_palette, target_palette):
            print(f"  ✔ Cores atualizadas em {svg_path.relative_to(REPO_ROOT)}")
        else:
            if svg_path.exists():
                print(f"  ⚠ Nenhuma substituição aplicada em {svg_path.relative_to(REPO_ROOT)}")
            else:
                print(f"  ↪ Arquivo ausente, ignorando {svg_path.relative_to(REPO_ROOT.parent)}")


if __name__ == "__main__":
    main()


