# from pynput import mouse
# import datetime
# import pygetwindow as gw
# import mouse

# mouseClickLogs = "mouseClickLogs.txt"

# def on_click(x, y, button, pressed):
#     if pressed:
#         print("pressed")



# if __name__ == "__main__":
#     with mouse.Listener(on_click=on_click) as listener:
#         listener.join()


# import mouse
# import datetime
# import pygetwindow as gw

# mouseClickLogs = "mouseClickLogs.txt"

# def log_clicks(event):
#     if event.event_type == 'down':  
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         active_window = gw.getActiveWindow()
#         window_name = active_window.title if active_window else "Unknown Window"
#         print(f"{timestamp} - Button: {event.button} - Window: {window_name}")

# mouse.hook(log_clicks)
# print("Tracking mouse clicks... Press Ctrl+C to stop.")
# mouse.wait()


