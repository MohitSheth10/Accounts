# 🏧 ATM Simulation Program

A lightweight **Python ATM simulator** that lets users create accounts, set secure 6-digit PINs, and log in using local file-based storage.
Built with a focus on simplicity, input validation, and basic security logic.

---

## ⚙️ Features

- 🆕 **Account Creation** — Create a new account under your name
- 🔐 **PIN Verification** — 6-digit numeric PIN, entered twice to confirm
- 🔄 **PIN Reset** — Option to change your PIN after a wrong attempt
- 🚪 **Attempt Limit** — Logs you out after 3 incorrect PIN attempts
- 💾 **Local File Storage** — Each account is saved as its own `.txt` file, right next to the script (works on any computer, no setup)
- ⚠️ **Error Handling** — Uses `try` / `except` to reject non-numeric input and wrong-length PINs

---

## 🔁 How It Works

1. Enter your name.
2. **If an account with that name exists**, enter your PIN.
   - Wrong PIN → choose to **retry** or **change your PIN**.
   - After 3 wrong attempts you're logged out.
3. **If no account exists**, you're asked whether to create one. You then set and confirm a 6-digit PIN, which is saved to `<YourName>.txt` in the same folder as the script.

---

## ▶️ How to Run

1. Install Python 3 (no extra libraries needed).
2. Download `account.py` and put it in its own folder.
3. Run it:
   ```bash
   python account.py
   ```

---

## 🧠 Planned Improvements

- 💰 Balance, deposit and withdrawal options
- 🔒 Store PINs hashed instead of as plain text

> ⚠️ This is a learning project. PINs are stored as plain text, so don't use a real PIN.
