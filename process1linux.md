Yes — you’re seeing something like:

source venv/bin/activate

This is not a different type of virtual environment. It is mainly the activation command used on Linux/macOS.

Windows vs Linux/macOS
System	Activation command
Windows PowerShell	venv\Scripts\Activate.ps1
Windows CMD	venv\Scripts\activate.bat
Linux/macOS	source venv/bin/activate
What does source mean?

On Linux/macOS, this:

source venv/bin/activate

means:

"Run the activate script in my current terminal session."

The activation script changes things like your PATH so that when you type:

python

your terminal uses the Python inside:

venv/bin/python

instead of the system Python.

Why is Windows different?

Windows virtual environments have a different folder structure:

venv/
└── Scripts/
    ├── activate.bat
    ├── Activate.ps1
    └── python.exe

Linux/macOS uses:

venv/
└── bin/
    ├── activate
    └── python

So for your Windows PowerShell, use:

venv\Scripts\Activate.ps1

After activation, you should see:

(venv) PS C:\Users\thito\OneDrive\Documents\django>

That's equivalent to seeing something like:

(venv) user@computer:~/django$

on Linux.