from openai import OpenAI
import os

my_secret = os.environ['OPEN_AI_KEY']

client = OpenAI(api_key=my_secret)

def get_code_problem(level):
  """ Gets a technical problem from Agent (aka OpenAI) 
  with a provided difficutluty level"""
  
  messages = [{
      "role":
      "system",
      "content":
      "You are a helpful engineer interviewer that knows thousands of codeing problems of different difficulty. Provide a random code problem that you haven't provided anyone in the last 5 mins for the user to solve that is {}."
      .format(level)
  }]
  return call_openai(messages)


def get_code_big_o(code_solution, code_big_o):
  """ Evaluates the BigO notion, Agent (aka OpenAI) """
  
  messages = [
      {
          "role": "system",
          "content": "You are a helpful engineer teacher."
      },
      {
          "role":
          "assistant",
          "content":
          """Evaluate the following code and provide feedback on what the user thinks is the Big O notion for this code: {}""".format(
              code_solution)
      },
      {
          "role": "user",
          "content": "{}".format(code_big_o)
      },
  ]
  return call_openai(messages)


def get_code_feedback(problem_prompt, code_solution):
  """ Evaluates and provides feedback on a technical problem 
  and user solution from Agent (aka OpenAI) """
  
  messages = [
      {
          "role": "system",
          "content": "You are a helpful engineer interviewer."
      },
      {
          "role":
          "assistant",
          "content":
          """Evaluate and provide feedback for the following techncial challenge and the user provided code solution: {}"""
          .format(problem_prompt)
      },
      {
          "role": "user",
          "content": "{}".format(code_solution)
      },
  ]
  return call_openai(messages)


def get_hint(problem_prompt, code_solution):
  """ Evaluates and provides a hint on a technical problem 
  and user solution from Agent (aka OpenAI) """
  
  messages = [
      {
          "role": "system",
          "content": "You are a helpful engineer interviewer."
      },
      {
          "role":
          "assistant",
          "content":
          """If the user provides code evaluate it and provide a hint for the following techncial challenge and the user's provided code without providing the complete solution: {}"""
          .format(problem_prompt)
      },
      {
          "role": "user",
          "content": "{}".format(code_solution)
      },
  ]
  return call_openai(messages)


def call_openai(messages):
  """ Calls the OpenAI API to get a response """
  
  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature=0,
  )
  return response.choices[0].message.content
