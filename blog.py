
import openai


openai.api_key = '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'


def generateideas1(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Please ask anything?: {}. \n\n 1".format(prompt1),
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']

def generateideas2(prompt1):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt="Enter the ideas you have: {} \n\n 1".format(prompt1),
      temperature=0.6,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def generateideas3(prompt1):
    response = openai.Completion.create(
      engine="text-curie-001",
      prompt="Type your ideas here.{} \n\n 1".format(prompt1),
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']
