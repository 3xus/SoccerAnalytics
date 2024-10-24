# Librerias
from statsbombpy import sb
import pandas as pd
from mplsoccer import VerticalPitch, Pitch
from highlight_text import ax_text, fig_text
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import seaborn as sns
import numpy as np

# Verificamos competencias
sb.competitions()['competition_name'].unique()

# Tomamos la Copa America 2024
copaAmerica = sb.matches(competition_id=223, season_id = 282)
copaAmerica.head()