# Example of using lab manager API's with personal access token

## Setup

1. Create a virtual environment

   ```bash
   python -m venv .venv
   ```

2. Install the required packages

   ```bash
   pip install -r requirements.txt
   ```

3. Copy and rename the environment file:

   ```bash
   cp .env.example .env
   ```

4. Edit the `.env` file and add your personal access token

   Get the access token by clicking the button in...

   https://app.fieldmanager.io/developer

   DO NOT SHARE YOUR ACCESS TOKEN WITH ANYONE

5. Run the script

   ```bash
    python example.py
   ```
