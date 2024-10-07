from dotenv import load_dotenv
load_dotenv()

#model 
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system","You are good with summarizing text. Follow these instructions: {instructions}"),
    ("user","{text}")
])


#Output Parser
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

result = chain.invoke({"question":"What is langchain","instructions": "Tell in 5 sentences"})

print(result)





