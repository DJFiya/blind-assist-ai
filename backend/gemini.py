#Gemini agent for live Q&A with the user

MOCK = True

def mock_answer_question(scene_description: str, question: str) -> str:
    """Return a mocked response that mimics what Gemini might say."""
    return (
        f"[MOCK] Based on the scene '{scene_description}', "
        f"in response to your question '{question}', "
        "it appears safe to proceed."
    )

def answer_question(scene_description: str, question: str) -> str:
    """Main entrypoint for Q&A. Returns Gemini’s answer (or mock)."""
    if MOCK:
        return mock_answer_question(scene_description, question)

    # --- real integration goes here ---
    # from openai import OpenAI
    # client = OpenAI(api_key=...)
    # prompt = build_prompt(scene_description, question)
    # resp = client.chat.create(model="gemini-1", messages=[{"role":"user","content":prompt}])
    # return resp.choices[0].message.content

    raise RuntimeError("Real Gemini integration not implemented yet")
