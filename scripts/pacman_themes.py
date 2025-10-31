"""Definições de paletas de cores para o Pac-Man contribution graph."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class PacmanPalette:
    grid_background: str
    text_color: str
    wall_color: str
    intensity_colors: List[str]


DEFAULT_PACMAN_THEME = "tokyonight"


PACMAN_THEME_PALETTES: Dict[str, PacmanPalette] = {
    "tokyonight": PacmanPalette(
        grid_background="#1a1b27",
        text_color="#c8d3f5",
        wall_color="#ff79c6",
        intensity_colors=["#1f2335", "#283457", "#3e5c86", "#82aaff", "#b4e0ff"],
    ),
    "halloween": PacmanPalette(
        grid_background="#140f07",
        text_color="#f8c784",
        wall_color="#ff7518",
        intensity_colors=["#1f1205", "#5c1e0a", "#8b330f", "#c65f1a", "#ff9d4d"],
    ),
    "nord": PacmanPalette(
        grid_background="#2e3440",
        text_color="#d8dee9",
        wall_color="#88c0d0",
        intensity_colors=["#3b4252", "#4c566a", "#5e81ac", "#81a1c1", "#88c0d0"],
    ),
    "radical": PacmanPalette(
        grid_background="#1d0c3b",
        text_color="#ffb3f7",
        wall_color="#ff5f5f",
        intensity_colors=["#2f164b", "#7b1fa2", "#c2185b", "#ff4081", "#ff80ab"],
    ),
    "synthwave": PacmanPalette(
        grid_background="#210b2c",
        text_color="#f9f871",
        wall_color="#f92672",
        intensity_colors=["#2d1243", "#4f2a93", "#7b3bff", "#ff6ff2", "#ffd1ff"],
    ),
    "chartreuse-dark": PacmanPalette(
        grid_background="#0a1f0a",
        text_color="#d4ff80",
        wall_color="#76ff03",
        intensity_colors=["#112b11", "#1d411d", "#2a5c2a", "#4caf50", "#aeea00"],
    ),
    "solarized-dark": PacmanPalette(
        grid_background="#002b36",
        text_color="#93a1a1",
        wall_color="#eee8d5",
        intensity_colors=["#073642", "#0b4b5a", "#116978", "#268bd2", "#2aa198"],
    ),
    "midnight-purple": PacmanPalette(
        grid_background="#1a103d",
        text_color="#d6c4ff",
        wall_color="#a68aff",
        intensity_colors=["#22134d", "#35256d", "#4c3b8f", "#7053c4", "#9a7bff"],
    ),
    "algolia": PacmanPalette(
        grid_background="#050f2c",
        text_color="#b4c6ff",
        wall_color="#00aeff",
        intensity_colors=["#0b1a40", "#102a66", "#1b3f8c", "#2c5ccf", "#4f86ff"],
    ),
    "onedark": PacmanPalette(
        grid_background="#1e222a",
        text_color="#abb2bf",
        wall_color="#61afef",
        intensity_colors=["#282c34", "#2c323c", "#3e4451", "#4c566a", "#98c379"],
    ),
    "dracula": PacmanPalette(
        grid_background="#282a36",
        text_color="#f8f8f2",
        wall_color="#ff79c6",
        intensity_colors=["#343746", "#44475a", "#6272a4", "#bd93f9", "#ff79c6"],
    ),
    "buefy": PacmanPalette(
        grid_background="#ffffff",
        text_color="#363636",
        wall_color="#7957d5",
        intensity_colors=["#edf2ff", "#b8c5ff", "#7f95ff", "#4c6ef5", "#364fc7"],
    ),
    "cobalt": PacmanPalette(
        grid_background="#002240",
        text_color="#d8e9ff",
        wall_color="#ff9800",
        intensity_colors=["#012f62", "#02468d", "#0360c0", "#0486ff", "#34b3ff"],
    ),
    "apprentice": PacmanPalette(
        grid_background="#262626",
        text_color="#fce8c3",
        wall_color="#ff8700",
        intensity_colors=["#32302f", "#3c3836", "#504945", "#665c54", "#fbf1c7"],
    ),
}


BASE_GAME_THEME_COLORS: Dict[str, PacmanPalette] = {
    "github": PacmanPalette(
        grid_background="#ffffff",
        text_color="#57606a",
        wall_color="#000000",
        intensity_colors=["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"],
    ),
    "github-dark": PacmanPalette(
        grid_background="#0d1117",
        text_color="#8b949e",
        wall_color="#ffffff",
        intensity_colors=["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"],
    ),
}


def get_palette_for_theme(theme: str) -> PacmanPalette:
    """Retorna a paleta desejada, usando o tema padrão quando necessário."""

    return PACMAN_THEME_PALETTES.get(theme, PACMAN_THEME_PALETTES[DEFAULT_PACMAN_THEME])


def get_base_theme_palette(theme: str) -> PacmanPalette:
    """Retorna a paleta base de onde partimos para o replace (github ou github-dark)."""

    return BASE_GAME_THEME_COLORS[theme]


