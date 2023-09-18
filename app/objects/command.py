
from typing import List, Callable
from dataclasses import dataclass
from discord import Member

@dataclass
class Command:
    function: Callable
    triggers: List[str]
    roles: List[str]

    def has_permission(self, member: Member) -> bool:
        """Check if member has permission to execute this command"""
        if not self.roles:
            # Command does not require permissions
            return True

        member_roles = [role.name for role in member.roles]

        return any(role in member_roles for role in self.roles)
