import settings


WORLD_LOCATION = settings.WORLD_LOCATION
BOT_LOG_LOCATION = settings.BOT_LOG_LOCATION
SERVER_LOG_ON = settings.SERVER_LOG_ON
SERVER_LOG_LOCATION = settings.SERVER_LOG_LOCATION

def get_file(get_command: str) -> str:
    file_type: str = get_command[5:].lower()
    match file_type:
        case "world":
            return WORLD_LOCATION, file_type.title()

        case "bot log":
            return BOT_LOG_LOCATION, file_type.title()

        case "server log":
            if SERVER_LOG_ON:
                return SERVER_LOG_LOCATION, file_type.title()
            else:
                return "Server log access is not activated", "Server log off"  

        case _:
            return f"{file_type} is invalid $get command", "Unknow File Type"
