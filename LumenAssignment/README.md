````markdown
# Appium + Pytest Test Project

UI test automation using Appium and Pytest on Android.

## ✅ Requirements

- Python 3.9+
- Android emulator (via Android Studio)
- Appium server installed and running
- ADB available in system PATH

## Install Dependencies

First, create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````

Then install required packages:

```bash
pip install -r requirements.txt
```

## ⚙️ Setup

Update the `.env` file with your local emulator and APK path:

```env
DEVICE_NAME=<your_emulator_name>
APP_PATH=C:<\path\to\\your\app-debug.apk>
```

## 🚀 Run Tests

1. Start your Android emulator:

```bash
emulator -avd <your_emulator_name>
```

2. Start the Appium server:

```bash
appium
```

3. Run the tests:

```bash
pytest -v -s
```

