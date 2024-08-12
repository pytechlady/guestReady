


def convert_to_error_message(message: any) -> dict:
    return {
        "status": "failure",
        "message": message,
        "data": "null",
    }
    
    
def convert_to_success_message_with_data(message: str, serialized_data: dict) -> dict:
    return {
        "status": "success",
        "message": message,
        "data": serialized_data,
    }