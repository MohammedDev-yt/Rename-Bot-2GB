# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import time
import os

#---------- BYTE CONVERTER ----------#

def humanbytes(size):

    if not size:
        return "0 B"

    power = 2**10
    n = 0

    Dic_powerN = {
        0: 'B',
        1: 'KB',
        2: 'MB',
        3: 'GB',
        4: 'TB'
    }

    while size >= power and n < 4:
        size /= power
        n += 1

    return str(round(size, 2)) + " " + Dic_powerN[n]

#---------- TIME FORMAT ----------#

def time_formatter(seconds):

    seconds = int(seconds)

    if seconds <= 0:
        return "0s"

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    if h > 0:
        return f"{h}h {m}m {s}s"

    elif m > 0:
        return f"{m}m {s}s"

    else:
        return f"{s}s"

#---------- PROGRESS BAR ----------#

def progress_bar(current, total):

    if total == 0:
        return "[⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡] 0%"

    percent = (current / total) * 100

    filled = int(percent // 10)

    bar = "⬢" * filled + "⬡" * (10 - filled)

    return f"[{bar}] {round(percent, 2)}%"

#---------- FULL PROGRESS ----------#

def format_progress(
    current,
    total,
    speed,
    eta,
    process="Downloading"
):

    icon = "📥" if process == "Downloading" else "📤"

    return (
        f"<blockquote>"
        f"{icon} <b>{process}...</b>\n\n"
        f"[{'⬢' * int((current / total) * 10) if total else '⬡' * 10}"
        f"{'⬡' * (10 - int((current / total) * 10)) if total else ''}] "
        f"{round((current / total) * 100, 2) if total else 0}%\n\n"
        f"📦 <b>Sɪᴢᴇ:</b> "
        f"{humanbytes(current)} / {humanbytes(total)}\n"
        f"⚡ <b>Sᴘᴇᴇᴅ:</b> "
        f"{humanbytes(speed)}/s\n"
        f"⏳ <b>Eᴛᴀ:</b> "
        f"{time_formatter(eta)}"
        f"</blockquote>"
    )

#-------------------------#

# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29

#-------------------------#