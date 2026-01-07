import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_logo(size_px=400):
    # Setup figure
    dpi = 100
    fig_size = size_px / dpi
    fig, ax = plt.subplots(figsize=(fig_size, fig_size), dpi=dpi)
    
    # Set canvas limits (0-100 to match SVG viewbox)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.invert_yaxis() # Match SVG coordinate system (y-down)
    ax.set_aspect('equal')
    ax.axis('off') # Hide axes

    # Color
    teal = '#2dd4bf'

    # 1. Outer Ring (Dashed)
    # SVG: r=40, stroke=8 (centered). So Outer=44, Inner=36.
    # Dasharray 180 (draw), 60 (gap). Circumference ~251.3
    # Angles: Draw 0->258 deg. Gap 258->344 deg. Draw 344->360 deg.
    
    # Segment 1 (Main C shape)
    wedge1 = patches.Wedge((50, 50), 44, 0, 258, width=8, color=teal)
    ax.add_patch(wedge1)
    
    # Segment 2 (Closing bit after gap)
    wedge2 = patches.Wedge((50, 50), 44, 344, 360, width=8, color=teal)
    ax.add_patch(wedge2)

    # 2. Center Nucleus
    nucleus = patches.Circle((50, 50), radius=12, color=teal)
    ax.add_patch(nucleus)

    # 3. Electron Dot (Top Right)
    electron = patches.Circle((75, 25), radius=6, color=teal)
    ax.add_patch(electron)

    # Save
    plt.savefig('chemcore_logo.png', transparent=True, bbox_inches='tight', pad_inches=0)
    print(f"Logo saved as chemcore_logo.png ({size_px}x{size_px})")

if __name__ == "__main__":
    create_logo()