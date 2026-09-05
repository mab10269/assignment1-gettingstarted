### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

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
        answer = "These are not the answers you are looking for."
    return(answer)
    
#Questions & Answers:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": pcap
#"Are encoding and encryption the same? - Yes/No": No
#"Is it possible to decrypt a message without a key? - Yes/No": No
#"Is it possible to decode a message without a key? - Yes/No": Yes
#"Is a hashed message supposed to be un-hashed? - Yes/No": No
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":64eec04f7bdbd459dc455d1151105b33957ff61c7118b7f23606e31b92b52b8d
#"Is MD5 a secured hashing algorithm? - Yes/No": No
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number": 5
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": 3
