from pynput.keyboard import Listener as KeyboardListener, Key
from pynput.mouse import Listener as MouseListener

print("Tracking keyboard and mouse events. Press Esc to stop.")

# Start keyboard listener
keyboard_listener = KeyboardListener(
    on_press=lambda key: print(f"Key pressed: {key.char}" if hasattr(key, 'char') else f"Special key pressed: {key}"),
    on_release=lambda key: False if key == Key.esc else None
)

# Start mouse listener
mouse_listener = MouseListener(
    on_move=lambda x, y: print(f"Mouse moved to: ({x}, {y})"),
    on_click=lambda x, y, button, pressed: print(f"{'Pressed' if pressed else 'Released'} {button} at ({x}, {y})"),
    on_scroll=lambda x, y, dx, dy: print(f"Scrolled at ({x}, {y}) with delta ({dx}, {dy})")
)

# Start both listeners
keyboard_listener.start()
mouse_listener.start()

# Keep the program running
keyboard_listener.join()
mouse_listener.join()
