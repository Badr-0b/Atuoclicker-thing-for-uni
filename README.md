# Atuoclicker-thing-for-uni
made this ages ago to spam click buttons on my uni page to register for some courses, practically useless to me now but oh well, probably worth sharing

OVERVIEW:
This Python application provides GUI-based mouse automation with recording/playback capabilities. It allows users to:

- Record mouse click positions
- Play back recorded actions (single-run or looped)
- Stop operations with keyboard shortcuts
- Control everything via a simple GUI interface

KEY FEATURES:
1. Recording System
- Click "Record" to start capturing left-click positions
- Press H key to stop recording
- Stores coordinates in memory during recording session

2. Playback Modes
- Play: Execute recorded clicks once (1 second between actions)
- Loop: Continuously repeat recorded clicks (3-second cooldown between loops)
- Press G key to stop any playback

USAGE:
Install dependencies:

```pip install pynput```

Run the program:

```python mouse_controller.py```

CONTROL FLOW:

1. Record -> Click "Record", perform clicks, press H when done
2. Play -> Click "Play" after recording
3. Loop -> Click "Loop" after recording
4. Emergency stop -> Press G anytime

IMPLEMENTATION NOTES:
- Coordinate storage uses screen coordinates
- Left mouse button clicks are hardcoded
- Delay timing (1s/3s) can be modified in code
- Requires window focus for keyboard shortcuts
- May need admin privileges depending on OS
