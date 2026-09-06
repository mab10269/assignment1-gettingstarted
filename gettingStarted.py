def check_answer(question, student_answer):

    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        correct_answer = "Pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        correct_answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        correct_answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        correct_answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        correct_answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        correct_answer = "64eec04f7bdbd459dc455d1151105b33957ff61c7118b7f23606e31b92b52b8d"
    elif question == "is MD5 a secured hashing algorithm? - Yes/No":
        correct_answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        correct_answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        correct_answer = 3
    else:
        return "This is not the way stranger... answer is incorrect"
    if student_answer == correct_answer:
        return "Correct"
    else:
        return "This is not the way stranger... answer is incorrect"

if __name__ == "__main__":
    questions = [
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?",
        "Are encoding and encryption the same? - Yes/No",
        "Is it possible to decrypt a message without a key? - Yes/No",
        "Is it possible to decode a message without a key? - Yes/No",
        "Is a hashed message supposed to be un-hashed? - Yes/No",
        "What is the SHA256 hashing value of your NYU email and use the answer in your code - ",
        "is MD5 a secured hashing algorithm? - Yes/No",
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number",
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    ]

    for question in questions:
        print(question)
        student_answer = input("Your answer: ")

        result = check_answer(question, student_answer)

        print(result)
        print()
