import app.keyboards as key
import asyncio

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext 

from db import add_user, todo_add, get_todo

router = Router()

class TodoData(StatesGroup):
    todo = State()


@router.message(CommandStart())
async def cmd_start(message: Message):

    username = message.from_user.first_name
    res = await add_user(str(message.from_user.id), username, message.from_user.username)

    if res == True:
        await message.answer(f"<b>🫰🏼 Hello {username}!</b>\n\n<i>💭Отправь мне фото ;)</i>",
                             reply_markup=key.main)
    else:
        await message.answer(f'{username}, кажется мне не по себе. Заходи попозже (')


@router.message(F.photo)
async def get_photo(message: Message):
    photo_path = message.photo[-1].file_id
    await message.answer_photo(photo=photo_path, caption=f'{message.from_user.first_name}',
                               reply_markup=key.main)

@router.message(F.voice)
async def get_voice(message: Message):
    voice = message.voice.file_id

    await message.answer_audio(audio=voice, caption=f"<b>{message.from_user.first_name}</b>, твое голосоывое"
                               , reply_markup=key.main)
    
@router.callback_query(F.data == 'add_data')
async def add_data(callback: CallbackQuery, state: FSMContext):
    global msg 

    await state.set_state(TodoData.todo)
    msg = await callback.message.edit_text(f"<b>{callback.from_user.first_name}</b>, напиши что тебе надо сделать или запиши голосовое")

@router.callback_query(F.data == 'data_list')
async def data_list(call: CallbackQuery):
    res = await get_todo(str(call.from_user.id))
    if res != []:
        formatted_tasks = []
        
        for task_text, task_status in res:
            formatted_tasks.append(f"<b>Статус</b>: {'<i>🚫 Не выполнено!</i>' if task_status == 'inProgress' else task_status == 'Done'if '<i>✅ Ты выполнил!</i>' else ''}\n<b>Текст задачи:</b> <i>{task_text}</i>")
        
        await call.message.edit_text(f"<b>{call.from_user.first_name}</b>, твой список задач:\n\n{'\n\n'.join(formatted_tasks)}")
    else:
        await call.message.edit_text(f'<b>{call.from_user.first_name}</b>, твой список пуст!')

@router.message(TodoData.todo)
async def add_todo(message: Message, state: FSMContext):
    await state.update_data(todo=message.text)

    data = await state.get_data()
    user_data = [item for item in data.values()][0]
    res = await todo_add(str(message.from_user.id), user_data)

    await message.delete()
    if res == True:
        await msg.edit_text(text=f"<b>{message.from_user.first_name}</b>, я добавил задачу:\n\n<i>{user_data}</i>", reply_markup=key.main)  
    else:
        await msg.edit_text(text=f"<b>{message.from_user.first_name}</b>, что то пошло не так(((") 

    await state.clear()
