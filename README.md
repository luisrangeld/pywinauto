# Pywinauto Automation – Notepad UWP Example

This project demonstrates how to use [Pywinauto](https://pywinauto.readthedocs.io/en/latest/) to automate Windows applications.  
One of the examples provided here automates the **Windows 10/11 Notepad (UWP)** app, but the same approach can be adapted for WPF and Win32 apps.

## 📋 Features
- Launch Notepad (UWP)
- Connect to the window using UI Automation (UIA backend)
- Write text in the editor
- Interact with the menu bar ("Editar" → "Fecha y hora")

## 🛠 Requirements
- **Windows 10 or 11**
- **Python 3.8+**
- Pip packages from `requirements.txt`
- Windows SDK tools (optional, for `Inspect.exe`)

## 📦 Installation

1. **Clone this repository**:
    ```powershell
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME
    ```

2. **Create and activate a virtual environment**:
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3. **Install dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

The file `config.json` contains:
- Target application (`app_exe`)
- Window title pattern (`title_re`)
- Menu items to interact with

You can edit `config.json` to automate a different app.

## 🚀 Usage

Run the main automation script:
```powershell
python test01.py

