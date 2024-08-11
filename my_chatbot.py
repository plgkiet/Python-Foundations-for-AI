# importing the required modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# creating a chatbot
myBot = ChatBot(
    name='Siya',
    read_only=True,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ]
)

# training the chatbot
small_convo = [
    'Hi there!',
    'Hi',
    'How do you do?',
    'How are you?',
    'I\'m cool.',
    'Always cool.',
    'I\'m Okay',
    'Glad to hear that.',
    'I\'m fine',
    'I feel awesome',
    'Excellent, glad to hear that.',
    'Not so good',
    'Sorry to hear that.',
    'What\'s your name?',
    'I\'m Siya. Ask me a math question, please.'
]

math_convo_1 = [
    'Pythagorean theorem',
    'a squared plus b squared equals c squared.'
]

math_convo_2 = [
    'Law of Cosines',
    'c**2 = a**2 + b**2 - 2*a*b*cos(gamma)'
]

# using the ListTrainer class
list_trainee = ListTrainer(myBot)
for convo in (small_convo, math_convo_1, math_convo_2):
    list_trainee.train(convo)

# starting a conversation
print(myBot.get_response("Hi, there!"))
print(myBot.get_response("What's your name?"))
print(myBot.get_response("Do you know Pythagorean theorem"))
print(myBot.get_response("Tell me the formula of law of cosines"))
