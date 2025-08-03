from pydantic_settings import BaseSettings, SettingsConfigDict
from app.version import __version__


class _MessageSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"
    )

    START: str = (
        "Welcome to HolderBot 🤖"
    )
    LETS_BACK: str = "Let's back..."
    ITEMS_MENU: str = "Select a item or create a new:"
    ITEMS: str = "Select items"
    MENU: str = "Select a Button"
    ASK_REMARK: str = "Enter remark: [a-z]"
    ASK_JSON: str = "Enter Json file: [*.json]"
    CREATE_WITH_JSON: str = "Create With Json"
    INVALID_JSON: str = "❌ Invalid json."
    WORNG_DOC: str = "❌ Invalid, Just send doc"
    WORNG_JSON: str = "❌ Invalid, Just use [*.json]"
    WRONG_STR: str = "❌ Invalid, Just use [a-z]"
    WRONG_INT: str = "❌ Invalid, Just use [0-9]"
    DUPLICATE: str = "❌ Duplicate, try another."
    ASK_TYPES: str = "Select a type:"
    ASK_MARZ_DATA: str = (
        "<b>Enter Marz Server Credentials:\n</b>"
        "• <code>Username [sudo]</code>\n"
        "• <code>Password [sudo]</code>\n"
        "• <code>Host [https://sub.domain.com:port]</code>\n\n"
        "<b>Example:</b>\n"
        "<code>erfan\nerfan\nhttps://panel.domain.com:443</code>"
    )
    WRONG_PATTERN: str = "❌ Invalid pattern."
    INVALID_DATA: str = "❌ Invalid data."
    SUCCESS: str = "✅ Success."
    FAILED: str = "❌ Failed"
    NOT_FOUND: str = "❌ Not Found."
    NOT_FOUND_CONFIGS: str = "❌ Not Found Any Config."
    ASK_COUNT: str = "Enter count: [0-9]"
    ASK_SUFFIX: str = "Enter Suffix:"
    ASK_DATA_LIMT: str = "Enter DataLimit: [0-9]\n0 for unlimited"
    ASK_DATE_LIMIT: str = "Enter DateLimit: [0-9]"
    ASK_CONFIGS: str = "Select Configs:"
    FAILED_USERNAME: str = "❌ Failed to create {username}."
    RANDOM_USERNAME: str = "Random Username"
    USER_INFO: str = (
        "• <b>Username:</b> <code>{username}</code>\n"
        "• <b>Data Limit:</b> <code>{data_limit}</code>\n"
        "• <b>Date Limit:</b> <code>{expire_strategy}</code>\n"
        "• <b>Sub Url:</b> <code>{subscription_url}</code>\n"
    )
    ASK_SURE: str = "Are your sure?"
    ASK_ADMIN: str = "Select admin:"
    ASK_NOTE: str = "Enter note text:"
    ASK_ADMIN_FROM: str = "Select from admin:"
    ASK_ADMIN_TO: str = "Select to admin:"
    ASK_USERNAME: str = "Enter Username:"
