#!/usr/bin/env python3

import json
import sys
from os.path import expanduser

try:
    with open(expanduser("~/.kube_alias")) as f:
        config = json.loads(f.read())

except FileNotFoundError as e:
    print(" ".join(sys.argv[1:]))
    sys.exit(0)

command_aliases = config.get("command", {})
object_aliases = config.get("object", {})

args = sys.argv[1:]
if len(args) == 0:
    sys.exit(0)

# replace command if there is any
replace = command_aliases.get(args[0]) or [args[0]]
args = replace + args[1:]

if args[0] in { "get", "edit", "delete", "explain" }:
    # if there is a get/edit/delete, we will replace the args[1]
    args[1] = object_aliases.get(args[1]) or args[1]

print(" ".join(args))
sys.exit(0)
