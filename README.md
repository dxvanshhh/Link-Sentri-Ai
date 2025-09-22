# Link-Sentri-Ai
# 🛡️ LinkSentry AI: Proactive Phishing Threat Neutralization

**Team Name:** DCoderZ
**Team Members:** 1.Devansh Raizada
                  2.Aabir Das 
                  3. Lakshya Goyal
                  4. Niyati Saxena
**Deviathon 2025**

## 💡 The Problem

Phishing attacks are the #1 cause of data breaches. Traditional blacklist-based defenses are reactive and fail to protect users from new, "zero-day" phishing websites. Our project solves this by proactively detecting threats before they can cause harm.

## ✨ Our Solution

LinkSentry AI is a smart browser extension that uses a Machine Learning model to analyze URLs in real-time. It provides an instant risk score, a clear reason for its verdict, and automatically blocks dangerous sites.

### Key Features
- **AI-Powered Prediction:** Detects new threats by analyzing URL characteristics, not just blacklists.
- **Real-time Risk Score:** Provides a 0-100% phishing probability score.
- **Dynamic Icon Feedback:** Toolbar icon changes color (Green/Red/Yellow) to show the current page's safety status.
- **Rich Notifications:** Professional, non-intrusive desktop notifications for high-risk alerts.
- **Automatic Blocking:** Seamlessly redirects users away from confirmed phishing sites.

## ⚙️ How to Run

### Backend
1. Navigate to the `backend` folder: `cd backend`
2. Install dependencies: `pip install pandas scikit-learn flask joblib`
3. Train the model (run once): `python train_model.py`
4. Start the server: `python app.py`

### Frontend
1. Open Google Chrome and go to `chrome://extensions`.
2. Enable "Developer mode".
3. Click "Load unpacked" and select the `extension` folder.

## 🛠️ Tech Stack
- **Backend:** Python, Flask, Scikit-learn
- **Frontend:** JavaScript (Chrome Extension APIs)
- **AI Model:** RandomForestClassifier
