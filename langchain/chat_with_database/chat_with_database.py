#from langchain.llms import OpenAI
import environ 
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

#Accessing the OpenAPI Key
env = environ.Env();

#Reading the OpenAPI Key
env.read_env();
API_KEY = env('OPENAI_API_KEY');
#print(API_KEY);

# Setup database
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://postgres:{env('DBPASS')}@localhost:5445/{env('DATABASE')}",
)

llm = OpenAI(openai_api_key=API_KEY, temperature=0);

#Setup a DB Chain
db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True, use_query_checker=True)
#print(db_chain.run("How many completed tasks are there?"))

query = """
Given an input question, first create a syntactically correct postgresql query to run, use completion_date column to get completed or finised tasks list. Then look at the results of the query and return the answer.
Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

{question}
"""

def get_prompt():
    print("Type 'Exit' to quit")

    while True : 
        prompt = input("Enter prompt :")

        if prompt.lower() == 'exit':
            print('Exiting....')
            break
        else:
            try:
                question = query.format(question = prompt)
                print(db_chain.run(question))
            except Exception as e:
                print(e)

get_prompt()









