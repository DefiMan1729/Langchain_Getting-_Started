from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate,ChatMessagePromptTemplate,HumanMessagePromptTemplate
from langchain.chains import LLMChain

#OPENAI_API_KEY has been set as an environment variable

def writeStory(_idea):
    # function body
    human_prompt = HumanMessagePromptTemplate.from_template('write a very short story with {_idea}') 
    chat_prompt_template= ChatPromptTemplate.from_messages([human_prompt])
    chat = ChatOpenAI()
    chain = LLMChain(llm=chat,prompt=chat_prompt_template)
    result = chain.run(_idea = _idea)
    print (result)

writeStory("about a boy")
print("--------***-------")
writeStory("about a girl")
