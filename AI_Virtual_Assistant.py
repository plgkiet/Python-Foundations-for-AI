import wolframalpha

# Taking input from user
question = input('Question: ')

# App id obtained by registering on Wolfram Alpha developer portal
app_id = 'U5HXGG-79KT69H58Q'

# Instance of Wolfram Alpha client class
client = wolframalpha.Client(app_id)

# Query Wolfram Alpha with the user's question
res = client.query(question)

# Extract the text from the response
answer = next(res.results).text

# Print the answer
print(answer)
