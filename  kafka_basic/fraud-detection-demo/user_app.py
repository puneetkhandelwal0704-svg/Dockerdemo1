from kafka import KafkaConsumer
import json

def user_login_and_listen():

    print("=== Fraud Alert System ===")

    try:
        user_id = int(input("Enter User ID: "))
    except ValueError:
        print("Invalid User ID")
        return

    print(f"Listening for alerts for User {user_id}...\n")

    consumer = KafkaConsumer(
        "fraud-notification",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="latest",
        value_deserializer=lambda x: json.loads(
            x.decode("utf-8")
        )
    )

    for message in consumer:

        alert = message.value

        if alert.get("userId") == user_id:

            print("\n========== FRAUD ALERT ==========")
            print(f"User : {alert.get('name')}")
            print(f"Tx ID : {alert.get('tx_id')}")
            print(f"Amount : ${alert.get('amount')}")
            print("=================================\n")

if __name__ == "__main__":
    user_login_and_listen()