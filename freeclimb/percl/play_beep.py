import enum

class PlayBeep(enum.Enum):
    ALWAYS = "always"
    NEVER = "never"
    ENTRY_ONLY = "entryOnly"
    EXIT_ONLY = "exitOnly"