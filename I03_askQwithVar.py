from dotenv import load_dotenv
load_dotenv()
#model 
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#prompts
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer. Follow the instructions. Write in 20 words"),
    ("user", "{user_ask}")
]) 

input = "how can langchain help with testing?"

chain=prompt | llm
result = chain.invoke({"user_ask": input})
print(result.content)

