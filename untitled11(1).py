# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kSu3-Uk3F_KY9HORgStPhSjrLv-coRM2
"""

import os
import openai

# Set up the OpenAI API client
openai.api_key = "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"
start_sequence = "\nAI:"
restart_sequence = "\nYou: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="AI: Hello, Which genre of movies do you like to watch?\nYou: can you recommend me a movie in horror?\n\n\n\nAI:  Watch \"The Conjuring\" or \"The Shining\" for a classic horror option. Or if you're looking for something more contemporary, \"Get Out\" or \"It Follows\" are great choices.\nYou: Horror movies\n\n\nAI: Watch \"The Conjuring,\" \"The Shining,\" \"Get Out,\" \"It Follows,\" and \"The Babadook.\"\nYou: comedy movies Tamil\n\n\nAI: great comedy movies from Tamil cinema include \"Rajini Murugan,\" \"Vasuvum Saravananum Onna Padichavanga,\" and \"Siva Manasula Sakthi.\n\n/don't recommend any 18+  content\n/don't tell about other topics apart from movie recommendation if ask any other topics tell \"that topics are not available\"\n\nYou: parody movies \n\nAI: For parody movies, I would recommend \"Hot Shots,\" \"Airplane!,\" and \"\nYou: can you recommend me a movie in romantic?\nAI: For romantic movies, I would recommend \"The Notebook,\" \"Titanic,\" \"La La Land,\" and \"The Fault in Our Stars.\"\nYou:\n",
  temperature=0.67,
  max_tokens=487,
  top_p=0.41,
  frequency_penalty=0.18,
  presence_penalty=0.41,
  stop=[" AI:", "You"]
  )








