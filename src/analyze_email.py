import ollama
from pathlib import Path

BASE = Path(__file__).parent.parent

def main(): 

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

    # Ask for user input
    name = input("Enter the email to be analyzed (from 0 - 180):")
    if not name.isdigit():
        print("Please enter a number.")
        exit()
    if int(name) < 0 or int(name) > 180:
        print("Please enter a number between 0 and 180.")
        exit()
    print(f"Chosen email: {name}")

    # Load email
    email_path = BASE / "data" / "golden_dataset" / f"{name}.txt"
    email_text = email_path.read_text(encoding="utf-8")

    # Construct final prompt
    final_prompt = combined_prompt.replace("{{EMAIL}}",email_text)

    # Run LLM
    print("Original mail: " + email_text)
    result = ollama.generate(model='llama3.2', prompt=final_prompt)
    print(">>> LLM classification:")
    print(result['response'])


if __name__ == "__main__":
    main()