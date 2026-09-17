import os
import subprocess
import webbrowser
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from assistant.router import route_command
from assistant.tools import TOOLS

load_dotenv()

BANNER = """
=========================================
 Personal AI Assistant - Windows MVP
=========================================
Type a command. Examples:
  open chrome
  open youtube
  open downloads
  type hello world
  what time is it
  lock computer
  sleep computer
  restart computer
  shutdown computer
  exit
=========================================
"""


def main():
    print(BANNER)
    while True:
        try:
            text = input("\nYou > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye.")
            break

        if not text:
            continue

        if text.lower() in {"exit", "quit", "bye"}:
            print("Assistant > Goodbye.")
            break

        action = route_command(text)

        if not action:
            print("Assistant > I don't know how to do that yet.")
            continue

        name = action["tool"]
        args = action.get("args", {})

        tool = TOOLS.get(name)
        if not tool:
            print("Assistant > That capability is not enabled.")
            continue

        if tool.get("requires_confirmation"):
            answer = input(f"Assistant > Confirm '{name}'? [y/N]: ").strip().lower()
            if answer not in {"y", "yes"}:
                print("Assistant > Cancelled.")
                continue

        try:
            result = tool["run"](**args)
            print(f"Assistant > {result}")
        except Exception as exc:
            print(f"Assistant > Error: {exc}")


if __name__ == "__main__":
    main()
