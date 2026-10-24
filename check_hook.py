import json, os
s = json.load(open(os.path.expanduser("~/.claude/settings.json")))
found = any("check_voice" in h.get("command", "") for e in s.get("hooks", {}).get("PreToolUse", []) for h in e.get("hooks", []))
print("voice guard hook found" if found else "hook NOT found, check step 4 again")
