import subprocess
import sys

def install_requirements():
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("Installing spacy model...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "uk_core_news_sm"])

if __name__ == "__main__":
    install_requirements()
