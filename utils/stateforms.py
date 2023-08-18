from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_user_token = State()
