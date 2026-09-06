def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "Pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "64eec04f7bdbd459dc455d1151105b33957ff61c7118b7f23606e31b92b52b8d"
    elif question == "is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else: 
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)

if __name__ == "__main__":
    debug_question1 = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    debug_question2 = "Are encoding and encryption the same? - Yes/No"
    debug_question3 = "Is it possible to decrypt a message without a key? - Yes/No"
    debug_question4 = "Is it possible to decode a message without a key? - Yes/No"
    debug_question5 = "Is a hashed message supposed to be un-hashed? - Yes/No"
    debug_question6 = "What is the SHA256 hashing value of your NYU email and use the answer in your code - "
    debug_question7 = "is MD5 a secured hashing algorithm? - Yes/No"
    debug_question8 = "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
    debug_question9 = "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"

    print(welcome_assignment_answers(debug_question1))
    print(welcome_assignment_answers(debug_question2))
    print(welcome_assignment_answers(debug_question3))
    print(welcome_assignment_answers(debug_question4))
    print(welcome_assignment_answers(debug_question5))
    print(welcome_assignment_answers(debug_question6))
    print(welcome_assignment_answers(debug_question7))
    print(welcome_assignment_answers(debug_question8))
    print(welcome_assignment_answers(debug_question9))
