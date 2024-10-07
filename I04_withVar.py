from dotenv import load_dotenv
load_dotenv()
#model 
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#prompts
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer. Follow the instructions.{instructions}"),
    ("user", "{user_ask}")
]) 

#Output Parser
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

input = "how can langchain help with testing?"
instruct = "Write in 20 words"
chain=prompt | llm | output_parser

# chain = prompt
result = chain.invoke({"user_ask": input,"instructions":instruct})
print(result)
