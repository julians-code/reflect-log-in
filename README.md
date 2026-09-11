# Reflect-Log-In

Pop-up window prompting you to reflect on your mood and productivity.

## Features

### Questions
- Are you being productive right now? (y/n)
- What are you about to do?
- Do you know what your next step is? (y/n)

### Timer
Pressing one of the (customizable) buttons on the bottom causes 
the window to close and reopen after the duration of the timer has passed.

### Storage
The inputted answers of the user get saved to a JSON file. 
Closing the window without inputting any data will also create an entry
(to collect data on in which situation no data is collected).

### Automatic Startup on Computer Unlock

The unlock watcher can automatically launch every time you unlock your computer. 
This guide covers setting that up on **Linux Mint 22.2 Cinnamon** (based on Ubuntu 24.04) with Python 3 installed. 
Other distributions may work similarly, but steps can vary. 
If you don't know how to set this up I recommend using search engines or your favorite LLM to find a solution.

> **Note:** The exact file paths and environment names may differ on your machine. Adjust accordingly.

---

#### Setup Steps

1. **Configure Paths**  
   Open `config.py` and update the following variables with your actual file paths:
   ```python
   APP_DIR = "/your/path/to/reflect-log-in"
   VENV_PYTHON = "/your/path/to/venv/bin/python3"  # if using a virtual environment
   ```

2. **Create an Autostart Entry**  
   Navigate to your autostart directory:
   ```bash
   cd $HOME/.config/autostart
   ```

   Create a new `.desktop` file, for example:
   ```bash
   nano reflect-log-in-watcher.desktop
   ```

3. **Add the Autostart Configuration**  
   Paste the following into the file, replacing the `Exec` path with your actual `unlock_watcher.py` location:
   ```text
   #!/usr/bin/env xdg-open

   [Desktop Entry]
   Type=Application
   Name=Reflect Log-In Unlock Watcher
   Exec=/usr/bin/python3 /home/you/projects/reflect-log-in/unlock_watcher.py
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   ```

4. **Set Execute Permissions**  
   Right-click the `.desktop` file → **Properties** → **Permissions**, and enable **Allow executing file as program**.  
   Alternatively, from the terminal:
   ```bash
   chmod +x reflect-log-in-watcher.desktop
   ```

5. **Test the Setup**  
   Double-click the `.desktop` file to run it once. If successful, the watcher should now be active and listening for unlock events.