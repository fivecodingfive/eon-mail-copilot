import ollama
from pathlib import Path
from src.helper import utils
import json
import re   

BASE = Path(__file__).parent.parent.parent

def analyze_mail():
    # load prompts
    system_prompt_path = BASE / "prompts" / "1_system" / "base_system.md"
    system_prompt = system_prompt_path.read_text(encoding="utf-8")

    analyze_prompt_path = BASE / "prompts" / "2_analyze" / "topic_classification.md"
    analyze_prompt = analyze_prompt_path.read_text(encoding="utf-8")

    combined_prompt = (
        system_prompt.strip()
        + "\n\n"
        + analyze_prompt.strip()
    )

      
    # Construct final prompt
    utils.set_current_email()
    email_text = utils.load_email()
    final_prompt = combined_prompt.replace("{{EMAIL}}",email_text)

    # Run LLM
    print("Original mail: " + email_text)
    result = ollama.generate(model='llama3.2', prompt=final_prompt)
    print(">>> LLM classification:")
    llm_response = result['response']
    print(llm_response)    

    # Try to extract JSON from the response
    try:
        # 1) if it’s already pure JSON, this will just work
        return json.loads(llm_response)
    except json.JSONDecodeError:
        pass

    # 2) otherwise, try to find the first {...} block
    match = re.search(r"\{.*\}", llm_response, re.DOTALL)
    if not match:
        print("Failed to find JSON object in LLM response.")
        return None

    json_str = match.group(0)
    try:
        output_dict = json.loads(json_str)
        return output_dict
    except json.JSONDecodeError as e:
        print(f"Failed to decode extracted JSON: {e}")
        return None



if __name__ == "__main__":
    # This block only runs if you execute THIS file directly (python process_llm.py)
    classification = generate_and_get_topic()
    if classification:
        print("\n--- Direct Run Result ---")
        print(f"Original mail: {utils.load_email()}")
        print(f"Topic: {classification['topic']}")
        print(f"Summary: {classification['short_summary']}")