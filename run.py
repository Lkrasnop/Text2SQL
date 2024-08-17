#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# run.py

import subprocess
import sys
import os
def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_streamlit_app():
    os.environ['STREAMLIT_EMAIL'] = 'no-reply@example.com'
    subprocess.check_call([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    # Ensure we're in the correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    install_requirements()
    run_streamlit_app()

