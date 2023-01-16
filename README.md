# Dalamud-Repo-Updater

Backend code for updating the [Dalamud-Repo](https://github.com/Zi-SH/Dalamud-Repo). If you're looking for the link to add to your game, click the previous link. 

Written in Python 3.10, licenced in MIT.

Crontab used:
`*/30	*	*	*	*	/usr/bin/env bash -c 'cd /bot/Dalamud-Repo-Updater && source /bot/Dalamud-Repo-Updater/venv/bin/activate && ./Louisoix.py'`
`*/10	*	*	*	*	/usr/bin/env bash -c 'cd /bot/Dalamud-Repo-Updater && source /bot/Dalamud-Repo-Updater/venv/bin/activate && ./Alphinaud.py'`
`0	0	*	*	*	/usr/bin/env bash -c 'cd /bot/Dalamud-Repo-Updater && source /bot/Dalamud-Repo-Updater/venv/bin/activate && ./Alisaie.py'`
