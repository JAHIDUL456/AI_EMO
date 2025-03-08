import sys
import os

# Get the path of the script's directory
script_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

# Specify the path to the GIF folder
gif_folder_path = os.path.join(script_dir, 'gif')

# Access a specific GIF file within the folder
gif_path = os.path.join(gif_folder_path, 'two.gif')
