

with open("Names.txt") as name_file:
    names = name_file.readlines()

with open("DefaultMail.txt") as message_file:
    message = message_file.read()

def make_new_messages():
    for name in names:
        new_message = message.replace("[name]", name.strip())
        with open(f"ready_to_send\\Letter_for_{name.strip()}.docx", "w") as mail_to_send:
            mail_to_send.write(new_message)

make_new_messages()