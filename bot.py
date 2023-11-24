import pyautogui
import time
import random


time.sleep(5)


pyautogui.hotkey('winleft')


pyautogui.write("Microsoft Edge")
time.sleep(3)  


pyautogui.press("enter")


time.sleep(5)


queries = [
    "Python programming",
    "Web development",
    "Machine learning",
    "Data science",
    "Artificial intelligence",
    "Computer graphics",
    "Game development",
    "Mobile app development",
    "Cybersecurity",
    "Blockchain technology",
    "Cloud computing",
    "Internet of Things",
    "Natural language processing",
    "Robotics",
    "Virtual reality",
    "Augmented reality",
    "Quantum computing",
    "Big data",
    "Database management",
    "Network security",
    "Software engineering",
    "Frontend development",
    "Backend development",
    "Responsive web design",
    "User experience (UX) design",
    "UI/UX prototyping",
    "Agile methodology",
    "DevOps practices",
    "Open-source development",
    "Git version control",
    "Linux operating system",
    "Windows operating system",
    "MacOS operating system",
    "Computer hardware",
    "Computer networking",
    "Computer architecture",
    "Artificial neural networks",
    "Deep learning",
    "Reinforcement learning",
    "Computer vision",
    "Natural language understanding",
    "Cybersecurity best practices",
    "Ethical hacking",
    "Penetration testing",
    "Cryptography",
    "Data encryption",
    "Web application security",
]


num_queries = 50


for _ in range(num_queries):
   
    random_query = random.choice(queries)

   
    time.sleep(5)

    pyautogui.hotkey('ctrl', 'e')  
    pyautogui.press("backspace", presses=100)  

    
    pyautogui.typewrite(random_query, interval=0.3)


    pyautogui.press("enter")

    
    time.sleep(5)


