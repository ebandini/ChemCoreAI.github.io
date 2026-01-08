import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_hex_logo(size_px=512):
    """
    Generates the ChemCoreAI Hexagonal 'Benzene' Core logo.
    Matches the SVG used in the website favicon.
    """
    # Setup figure
    dpi = 100
    fig_size = size_px / dpi
    fig, ax = plt.subplots(figsize=(fig_size, fig_size), dpi=dpi)
    
    # Set canvas limits (0-100 scale)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.invert_yaxis()  # Match SVG coordinate system (y-down)
    ax.set_aspect('equal')
    ax.axis('off')

    # ChemCoreAI Signature Teal
    teal = '#2dd4bf'

    # 1. Calculate Hexagon Vertices (Benzene Ring)
    # Center (50, 50), Radius ~40
    center_x, center_y = 50, 50
    radius = 40
    # Angles for a vertical hexagon (flat top/bottom is 30, 90, 150...)
    # We want the pointy top version to match the L 50 10 path
    angles = np.deg2rad([270, 330, 30, 90, 150, 210])
    
    vertices = []
    for angle in angles:
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        vertices.append((x, y))

    # 2. Add Hexagon Path
    # Using a Polygon patch with a thick stroke and no fill
    hexagon = patches.Polygon(
        vertices, 
        closed=True, 
        edgecolor=teal, 
        facecolor='none', 
        linewidth=12,  # Thick stroke for modern look
        joinstyle='round',
        capstyle='round'
    )
    ax.add_patch(hexagon)

    # 3. Add Center Nucleus (The "Core")
    nucleus = patches.Circle((50, 50), radius=12, color=teal, lw=0)
    ax.add_patch(nucleus)

    # Save with high quality and transparency
    plt.savefig(
        'chemcore_hex_logo.png', 
        transparent=True, 
        bbox_inches='tight', 
        pad_inches=0.1,
        dpi=300
    )
    plt.close()
    print(f"Success: New Hexagonal logo saved as 'chemcore_hex_logo.png'")

if __name__ == "__main__":
    create_hex_logo()