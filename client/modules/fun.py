import subprocess

def ascii_live(name):
        try:
                subprocess.run(["curl", f"ascii.live/{name}"])
        except KeyboardInterrupt:
                pass
