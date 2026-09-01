from dataclasses import asdict, dataclass, field
from datetime import datetime

@dataclass
class ReflectionEntry:
    """
    Reflection class: holds one entry; adapter between storage and system

    Args:
        timestamp
        focused: Was user focused?
        doing: What was user about to do?
        know_next_step: Did user know the next step?
    """

    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    focused: bool = None
    doing: str = None
    know_next_step: bool = None

    def to_dict(self):
        return asdict(self)