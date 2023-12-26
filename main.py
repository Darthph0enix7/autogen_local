import autogen

config_list = [
    {
        "model": "codellama-7b-instruct.Q5_K_M.gguf",
        "api_base": "http://127.0.0.1:8000/v1",
        "api_type": "open_ai",
        "api_key": "NULL",  # Placeholder
    }
]

coding_mentor = autogen.AssistantAgent(
    name="CodingMentor",
    llm_config={
        "seed": 42,
        "config_list": config_list,
        "temperature": 0.7,
        "request_timeout": 1200,
    },
    system_message="""Coding Mentor here! I
     can guide you through implementing 
     sorting algorithms in Python.""",
)

algorithm_expert = autogen.AssistantAgent(
    name="AlgorithmExpert",
    llm_config={
        "seed": 42,
        "config_list": config_list,
        "temperature": 0.7,
        "request_timeout": 1200,
    },
    system_message="""Algorithm Expert. I 
    specialize in algorithms. Let's work 
    on implementing a sorting algorithm 
    together.""",
)

student = autogen.UserProxyAgent(
    name="Student",
    human_input_mode="ALWAYS",
    code_execution_config={"work_dir":"node"},
)

student.initiate_chat(
    coding_mentor,
    message="""What are you?""",
)