# MBOX to PST Converter

This Python project allows you to convert MBOX files to PST files using the `readpst` tool (part of `libpst`). The script is suitable for Windows users and can be run with Python 3.x.

## Requirements

- **Operating System**: Windows
- **Python**: Version 3.x
- **readpst**: `readpst` is a tool that converts MBOX files to PST format. You can either install `readpst` via Windows Subsystem for Linux (WSL) or find a Windows-compatible version.
  
## Installation

1. Install `readpst`:
   - On **Windows** via **WSL**: Install WSL if you haven't already, and use the following command to install `readpst`:
     ```bash
     sudo apt-get install pst-utils
     ```
   - For a native **Windows** version, look for `readpst` binaries compatible with Windows and add them to your system's PATH.

2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mbox-to-pst-converter.git
   cd mbox-to-pst-converter
