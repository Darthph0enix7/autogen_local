from autogen import AssistantAgent, UserProxyAgent,oai

config_list = [
    {
        "model": "codellama-7b-instruct.Q5_K_M.gguf",
        "api_base": "http://127.0.0.1:8000/v1",
        "api_type": "open_ai",
        "api_key": "NULL",
    }
]

llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 2028,}

# Create assistant agent
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="""Engineer. You follow an approved plan. 
    You write python/shell code to solve tasks. 
    Wrap the code in a code block that specifies the script type. 
    The user can't modify your code. So do not suggest incomplete 
    code which requires others to modify. Don't use a code block 
    if it's not intended to be executed by the executor.
    Don't include multiple code blocks in one response. Do not ask 
    others to copy and paste the result. Check the execution result 
    returned by the executor. If the result indicates there is 
    an error, fix the error and output the code again. Suggest
    the full code instead of partial code or code changes. If
    the error can't be fixed or if the task is not solved even
    after the code is executed successfully, analyze the 
    problem, revisit your assumption, collect additional info
    you need, and think of a different approach to try.
""",
)

# Create user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    llm_config=llm_config,
    code_execution_config={"work_dir": "coding"},)

# Start the conversation
user_proxy.initiate_chat(
    assistant,
    message="""Plot a chart of AMZN, AAPL and INTC stock
 price change YTD.use yfinance,matplotlib,pandas packages 
 and save to stock_price_ytd.png.""",)