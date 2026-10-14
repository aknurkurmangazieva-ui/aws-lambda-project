

import json

def lambda_handler(event, context):
    name = event.get("name", "Әлем")

    result = {
        "message": f"Сәлем, {name}!",
        "status": "success",
        "service": "GitHub Actions"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result, ensure_ascii=False)
    }


if __name__ == "__main__":
    event = {"name": "Студент"}
    response = lambda_handler(event, None)

    print("Бағдарлама іске қосылды!")
    print(json.dumps(response, ensure_ascii=False, indent=2))

