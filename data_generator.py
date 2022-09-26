from email import message
import random
import string

user_id_list = list(range(1, 101))
recipient_id_list = list(range(1, 101))


def generate_message():
    user_id = random.randint(0, 101)
    recipient_id_list_copy = recipient_id_list.copy()
    recipient_id_list_copy.remove(user_id)
    recipient_id = random.choice(recipient_id_list)

    message = ''.join(random.choices(string.ascii_letters, k=32))

    data_dict = {
        "user_id": user_id,
        "recipient_id": recipient_id,
        "message": message
    }

    return data_dict


if __name__ == "__main__":
    generate_message()
