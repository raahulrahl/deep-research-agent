# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""deep-research-agent - An Bindu Agent."""

from deep_research_agent.__version__ import __version__
from deep_research_agent.main import (
    handler,
    initialize_agent,
    main,
    cleanup,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_agent",
    "main",
    "cleanup",
]