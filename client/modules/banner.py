console = Console()
columns = shutil.get_terminal_size().columns

f = Figlet(font='slant')
banner = f.renderText("NEXUS    CHAT")

def glitch(text):
        chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
        return ''.join(c if random.random() > 0.2 else random.choice(chars) for c in text)

for line in banner.split("\n"):
        print(BOLD + GREEN + line.center(columns) + RESET)
        time.sleep(0.02)


time.sleep(1)
boot = [
        "Initializing System...",
        "Loading Modules...",
        "Connecting to Network...",
        "Verifying Security...",
        "All Systems Online!"
]

for msg in boot:
        for _ in range(2):
                console.print(glitch(msg).center(columns), style="bold cyan")
                time.sleep(0.1)

        console.print(msg.center(columns), style="bold green")
        time.sleep(0.3)

console.print("\n" + "Streaming Data...".center(columns) + "\n", style="bold magenta")
neon_colors = ["#ff00ff", "#00ffff", "#ff9900", "#00ff00"]

for _ in range(100):
        line = "".join(random.choice("01") for _ in range(columns))
        color = random.choice(neon_colors)
        console.print(line, style=f"bold {color}")
        time.sleep(0.003)

console.print("\n" + "SYSTEM READY ⚡".center(columns), style="bold yellow")