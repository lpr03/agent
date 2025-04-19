import cohere
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(api_key)

def generate_code_for_task(task_description):
    try:
        response = co.generate(
            model="command",  
            prompt=f"Generate Python code for the following task: {task_description}. Only provide the Python code, no extra text or markdown.",
            max_tokens=1000,  
        )
        generated_code = response.generations[0].text.strip()
        cleaned_code = generated_code.replace("```python", "").replace("```", "").strip()
        return cleaned_code  
    except Exception as e:
        print(f"Error generating code: {e}")
        return None

def execute_python_script(script_code):
    """Creates a Python file, writes the script, and executes it."""
    script_name = "generated_script.py"
    try:
        with open(script_name, "w") as file:
            file.write(script_code)

        result = subprocess.run(
            ["python", script_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return result.stdout.decode(), result.stderr.decode()  # Capture output and error
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode()}", ""
    except Exception as e:
        return f"General Error: {str(e)}", ""

def main():
    print("Welcome to the AI Task Agent!")
    task_description = input("Enter the task description: ")
    
    print("Generating...")
    code = generate_code_for_task(task_description)

    if code:
        print("Python Code Generated:")
        print(code)

        approval = input("Do you approve this task plan? (yes/no): ").strip().lower()
        if approval == 'yes':
            print("Executing the Python script...")
            output, error = execute_python_script(code)
            if error:
                print(f"Error: {error}")
            else:
                print(f"Task Output: {output}")
                print("Task completed successfully!")
        else:
            print("Task not approved. Exiting.")
    else:
        print("Failed to generate the Python code.")

if __name__ == "__main__":
    main()
