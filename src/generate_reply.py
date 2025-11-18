import ollama
from pathlib import Path
import helper
import analyze_email

BASE = Path(__file__).parent.parent

def main(): 

    # load prompts
    system_prompt_path = BASE / "prompts" / "1_base_system.md"
    system_prompt = system_prompt_path.read_text(encoding="utf-8")

    component_prompt_path = BASE / "prompts" / "3_component_generation.md"
    component_prompt = component_prompt_path.read_text(encoding="utf-8")

    combined_prompt = (
        system_prompt.strip()
        + "\n\n"
        + component_prompt.strip()
    )

      
    # mail text
    email_text = helper.load_email()
    
    # Data from first analysis step
    try:
        analysis_data = analyze_email.analyze_mail()
    except Exception as e:
        print(f"Error during LLM analysis: {e}")
        return
    
    topic = analysis_data.get('topic', 'NA')
    missing_info = analysis_data.get('missing_info', 'None specified')
    tone = analysis_data.get('tone', 'None found')

    # Construct final prompt
    final_prompt = combined_prompt\
        .replace("{{EMAIL}}",email_text)\
        .replace("{{TOPIC}}",topic)\
        .replace("{{MISSING_INFO}}",missing_info)\
        .replace("{{TONE}}",tone)    

    result = ollama.generate(model='llama3.2', prompt=final_prompt)
    print(">>> LLM classification:")
    print(result['response'])


if __name__ == "__main__":
    main()