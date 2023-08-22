# VRC-OSCStuff

VRC-OSCStuff is are Python scripts that integrate with VRChat using the OSC protocol to automate stuff.

## Features

-   [holy-moving-chatbox.py](holy-moving-chatbox.py)
    -   Send the bible.txt into the chatbox
    -   Uses occurrences of specific letters (W, A, S, D) to determine movement duration in respective directions
    -   Smoothly interpolates between values to simulate eye-closing
-   [high-chatbox.py](high-chatbox.py)
    -   Send a custom text into a very high chatbox

## Dependencies

-   python-osc
-   psutil

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
python name_of_the_script.py
```

4. Follow the on-screen prompts to enable/disable chatbox, movements, and eye functionalities.

## License

This project is licensed under the AGPL-3.0 License. For more details, please refer to the [LICENSE](LICENSE) file.
