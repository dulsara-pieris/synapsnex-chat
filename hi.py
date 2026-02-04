import subprocess

def run_ascii_live(name):
    try:
        # Run curl like in terminal
        subprocess.run(["curl", f"ascii.live/{name}"])
    except KeyboardInterrupt:
        continue

# Example usage
print("Starting Rick ASCII animation. Press Ctrl+C to stop anytime.")
run_ascii_live("rick")

# Continue with other Python code
print("Now we continue with other lines...")
for i in range(5):
    print(f"Line {i+1}")
