from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.keys import BotKeys, PageCB, Pages, Actions
from app.db import crud
from app.settings.language import MessageTexts
from app.models.server import ServerModify
from app.settings.track import tracker

router = Router(name="server_data")


@router.callback_query(
    PageCB.filter((F.page.is_(Pages.SERVERS)) & (F.action.is_(Actions.INFO)))
)
async def data(callback: CallbackQuery, callback_data: PageCB):
    server = await crud.get_server(callback_data.panel)
    if not server:
        track = await callback.message.edit_text(
            text=MessageTexts.NOT_FOUND, reply_markup=BotKeys.cancel()
        )
        return await tracker.add(track)

    # Define buttons based on sudo status
    buttons = [
        ServerModify.REMARK,
        ServerModify.DATA,
        ServerModify.EXPIRED_STATS,
        ServerModify.REMOVE,
    ]
    
    # Add monitoring buttons only for sudo users
    if server.is_sudo:
        buttons.append(ServerModify.NODE_MONITORING)
        buttons.append(ServerModify.NODE_AUTORESTART)

    return await callback.message.edit_text(
        text=server.format_data,
        reply_markup=BotKeys.modify(
            dataid=server.id,
            datatypes=buttons,
            page=Pages.SERVERS,
            panel=server.id,
            server_back=server.id,
        ),
    )
