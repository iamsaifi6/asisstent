# Personal AI Assistant — Windows MVP

This is a local-first starter assistant for Windows. It accepts text commands and can safely perform a small set of PC actions.

## Included
- Open applications and websites
- Open folders
- Lock, sleep, restart, and shutdown (with confirmation)
- Type a text into the active window
- Get current time/date
- Basic command routing without giving an AI model unrestricted shell access

## Requirements
- Windows 10/11
- Python 3.11+
- Optional: an OpenAI API key for natural-language intent parsing

## Setup

Open PowerShell in this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and add your API key if you want AI parsing.

Run:

```powershell
python main.py
```

If you do not add an API key, the built-in command parser still supports the examples below.

## Example commands

- `open chrome`
- `open notepad`
- `open youtube`
- `open downloads`
- `type hello world`
- `what time is it`
- `lock computer`
- `sleep computer`
- `restart computer`
- `shutdown computer`
- `exit`

Destructive/system-power actions require confirmation.

## Safety

This MVP deliberately does NOT expose arbitrary shell commands to the AI. Add capabilities one by one through explicit tools and permission checks. For actions involving messages, purchases, deleting files, credentials, or account changes, add explicit confirmation before execution.
