from bot.handlers.handler import Handler
from bot.handlers.update_database_logger import DatabaseLogger
from bot.handlers.ensure_user_exists import EnsureUserExists
from bot.handlers.message_start import MessageStart
from bot.handlers.pizza_selection import PizzaSelectionHander
from bot.handlers.pizza_size import SizeSelectionHandler
from bot.handlers.pizza_drink import DrinkSelectionHander
from bot.handlers.pizza_order import ApproveOrderHander


def get_handlers() -> list[Handler]:
    return [
        DatabaseLogger(),
        EnsureUserExists(),
        MessageStart(),
        PizzaSelectionHander(),
        SizeSelectionHandler(),
        DrinkSelectionHander(),
        ApproveOrderHander(),
    ]
