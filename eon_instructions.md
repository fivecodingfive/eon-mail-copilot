# NLP Methods for CCM (Customer Contact Management)
Congratulations on joining a tremendous learning experiment, and thank you for choosing the E.ON Track! We're glad to invite you into the World of Digital Energy Solutions!

Take your seats and fasten the belts. We are starting... 3 -> 2 -> 1!

# Challenges for E.ON
With more than 14 million customers in Germany and 47 million customers 
worldwide, E.ON is one of the top 5 biggest energy suppliers in Europe and 
top 10 worldwide. But with a big customer base comes a big responsibility.
As E.ON we try to give the customer a best-in-class experience. One of the 
biggest touchpoints currently are emails. Every day, E.ON receives thousands 
of emails from customers with questions, complaints, or requests. To handle
this huge amount of emails, E.ON is looking for ways to automate the handling
of these emails.  
Customer Agents (CAs) are spending a lot of time reading and answering these 
emails. To automate this process, E.ON is looking for ways to use NLP 
methods and LLMs to analyze and understand the emails and help CAs to answer 
them more efficiently. Since efficient does not only mean fast, but also 
precise, E.ON wants to create a semi-automated answering system, where
CAs can check and adapt the answers before sending them to the customers. 
Thereby the customer still has the responsibility for the answer, but the
CAs are supported in their daily work.  
Why we do not want to fully automate the answering process may be answered 
in [this article](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know).

## What is the desired process?
For the semi-automated answering process, we envision that the customer sends
an email to E.ON. The email is then analyzed by an LLM or something similar, 
which extracts the case of the customer and then generates a first draft of an
answer. The CA then checks the answer, adapts it if necessary, and has the 
opportunity to select from different tones and styles of the answer. 
Finally, the CA sends the answer to the customer.

If possible, the CA should also be able to type an answer which is then
analyzed by the system to give feedback on the tone and style of the answer 
or even auto-completed by the system.

# Data Sheet

The dataset originally comprised 181 anonymized customer emails. Some of the 
emails are removed due to entailed factual information which cannot be 
disclosed, with 161 emails left. Every email is placed into a separate text 
file without any formatting. All files reside under 
`2025-04-15-golden-dataset`.   
All emails are in German and depict real customer conversations with E.ON 
Energie Deutschland GmbH. A "baseline answer" is not provided.

# Use Cases

The challenge is built around one main NLP task: AI aided answer generation 
for customer emails.

The goal is to create a pipeline to generate response components, so that 
an CA can compile an answer out of these bricks. Thereby E.ON 
can help the CAs to answer the emails more efficiently and with a higher
quality. The generated answers should be factually correct, but also
adaptable in tone and style.  
As an initial step, the email topic should be identified to better generate 
a response and to give the CS a general overview of what the email is about.

Complexity levels:
- Level 0: Identify the topic of the email. (e.g. "Billing issue", 
  "Contract change", "Complaint", etc.) OR summarize the email topic for 
  the CA.
- Level 1: Generate a first draft of an answer to the email. The answer 
  should be factually correct and cover all aspects of the email. The answer 
  should be adaptable in tone and style. (e.g. "formal", "informal", 
  "friendly", "professional", etc.)
- Level 2: Break the email down into different components (e.g. 
  "Greeting", "Main part", "Closing", etc.) and generate a response for 
  each component. The CA should be able to select and adapt the components 
  to compile the final answer.
- Level 4: Think of a way to evaluate the quality of the generated answers. 
  Create a framework to evaluate the answers based on different criteria 
  (e.g. "factual correctness", "tone", "style", "completeness", etc.) and 
  use it to evaluate the generated answers.
- Bonus Level: Create an online app e.g. using streamlit or similar, where 
  the CA can upload or paste the email, see the generated components, 
  select and adapt them to compile the final answer. The app should also 
  have the option to select the tone and style of the answer.

The participants are expected to provide a solution at one level at least, 
starting with Level 0 since the latter tasks are based on the former. It is 
up to the participants if they want to define a wider or deeper scope for 
their task.

A "solution" can be a running software solution or a kind of 
proof-of-concept run manually in the form of a Jupyter Notebook.

# References
Here are some base courses you can have a look at if you are looking for 
some inspiration:

NLP Courses:
- https://course.spacy.io/en/
- https://huggingface.co/learn/nlp-course/

Tutorials:
- https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html
- https://towardsdatascience.com/building-sentiment-classifier-using-spacy-3-0-transformers-c744bfc767b
- https://towardsdatascience.com/topic-modeling-with-bert-779f7db187e6

Evaluation:
- https://cookbook.openai.com/examples/evaluation/how_to_eval_abstractive_summarization
- https://soletlab.asu.edu/coh-metrix/
- https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0
- https://github.com/mcao516/EntFA
- https://github.com/ThomasScialom/QuestEval
- https://github.com/salesforce/factCC

Frameworks:
- https://ollama.com/
- https://docs.chainlit.io/

Fine-tuning:
- https://www.philschmid.de/fsdp-qlora-llama3
- https://github.com/teticio/llama-squad
- https://www.answer.ai/posts/2024-03-14-fsdp-qlora-deep-dive
- https://arxiv.org/abs/2305.14314

Models:
- https://github.com/jzhang38/TinyLlama
- https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- https://huggingface.co/models
- https://chat.lmsys.org/?leaderboard

# Our expectations

We expect the participants to stay in touch with the mentors during the 
whole term. Please do spend time on the tasks and not hope to tackle 
everything at the last minute. We are open to your questions and hope to 
provide as much support as possible to you given your motivation and 
dedication to the challenge topic. And you'll experience that even bigger 
elephants can get swallowed in small pieces by chewing them carefully over 
a longer time :)  
Have fun and happy hacking!
