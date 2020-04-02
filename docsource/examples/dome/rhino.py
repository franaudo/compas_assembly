import os
from compas_assembly.datastructures import Assembly
from compas_assembly.rhino import AssemblyArtist


try:
    HERE = os.path.dirname(__file__)
except NameError:
    HERE = os.getcwd()

DATA = os.path.join(HERE, '../../../data')
FILE = os.path.join(DATA, 'wall_equilibrium.json')


# ==============================================================================
# Load assembly from file
# ==============================================================================

assembly = Assembly.from_json(FILE)

# ==============================================================================
# Visualize
# ==============================================================================

artist = AssemblyArtist(assembly, layer="Wall")
artist.clear_layer()
artist.draw_nodes()
artist.draw_edges()
artist.draw_blocks()
artist.draw_interfaces()
artist.draw_forces(scale=1.0)
artist.redraw()
