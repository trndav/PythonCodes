# Create shortcut to public desktop

import os
import winshell

def create_shortcut():
    # Path to the app
    target_path = r"d:\test.bat"
    
    # Path to public desktop
    public_desktop = os.path.join(os.environ["PUBLIC"], "Desktop")
    
    # Path for the shortcut
    shortcut_path = os.path.join(public_desktop, "Test Shortcut.lnk")
    
    # Create the shortcut
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = target_path
        shortcut.description = "Shortcut to Test App"
    
    print(f"Shortcut created: {shortcut_path}")

# Run the function
create_shortcut()
