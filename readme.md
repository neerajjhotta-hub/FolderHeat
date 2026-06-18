# FolderHeat

I made this simple CLI tool because i always had that one folder on my system (usually Downloads or Desktop) that was eating up like 40GB and i had no idea what type of files were responsible, i would go in manually and try to figure it out which was annoying. so i made this, you just point it at any folder and it tells you exactly which category of files is taking up the most space with a simple bar chart. i know its not a complex tool but it solves a real problem i had so here it is.

---

## Output example

```
folderheat  /home/john/Downloads

  Category      Size         Distribution
  ----------    ----------   --------------------------------
  Videos          18.4 GB   ################################
  ZIP Files        6.2 GB   ###########---------------------
  Images           3.1 GB   #####---------------------------
  Documents      890.3 MB   ##------------------------------
  Audio          412.0 MB   #-------------------------------
  Code            55.7 MB   --------------------------------
  Other           12.1 MB   --------------------------------
  ----------------------------------------------------------
  TOTAL           29.1 GB
```

---

## Requirements

- Python 3.6 or newer
- No third-party packages required, uses only stdlib

---

## Run as a global command (folderheat)

### Linux

```bash
# 1. Move the file to a directory on your PATH
sudo mv folderheat.py /usr/local/bin/folderheat

# 2. Make it executable
sudo chmod +x /usr/local/bin/folderheat

# 3. Make sure the first line of the file is:
#   #!/usr/bin/env python3
# (folderheat.py already has this — nothing to do)

# 4. Verify
folderheat
folderheat ~/Downloads
```

### macOS

```bash
sudo mv folderheat.py /usr/local/bin/folderheat
sudo chmod +x /usr/local/bin/folderheat
folderheat
folderheat ~/Downloads
```

### Windows

```bat
:: 1. Pick a folder that's already on your PATH or create one and add it.

:: 2. Copy folderheat.py to that folder:
copy folderheat.py C:\tools\folderheat.py

:: 3. Create a wrapper folderheat.bat in the same folder:
echo @echo off > C:\tools\folderheat.bat
echo python "%~dp0folderheat.py" %* >> C:\tools\folderheat.bat

:: 4. Make sure C:\tools is in your PATH (one-time setup):
setx PATH "%PATH%;C:\tools"

:: 5. Open a new terminal and verify:
folderheat
folderheat C:\Users\john\Downloads
```