# VRC-OSCStuff
VRC-OSCStuff is a Python script that integrates with VRChat using the OSC protocol to automate stuff based on the text content of bible.txt. The project interprets the text and triggers various actions such as movement and chatbox input.

## Features
- Dynamic Text Reading: Reads the bible.txt file and processes its content.
- Chatbox Interaction: Sends messages to the chatbox with the extracted content.
- Character-based Movement: Uses occurrences of specific letters (W, A, S, D) to determine movement duration in respective directions.
- Smooth Eye Movements: Smoothly interpolates between values to simulate eye-closing based on text content.
## Dependencies
- python-osc
## Setup & Usage
1. Clone the repository:
```bash
git clone https://github.com/Luois45/VRC-OSCStuff.git
cd VRC-OSCStuff
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Run the script:
```bash
python holy-moving-chatbox.py
```
4. Follow the on-screen prompts to enable/disable chatbox, movements, and eye functionalities.
## License
This project is licensed under the AGPL-3.0 License. For more details, please refer to the [LICENSE](LICENSE) file.
