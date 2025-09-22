import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier # Using a more powerful model
import joblib
import numpy as np
import re # For advanced text matching

# --- INNOVATIVE FEATURE EXTRACTION ---
def extract_features(url):
    features = []
    
    # Basic Features
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('/'))
    features.append(url.count('-'))
    
    # Keyword Features - Looks for suspicious words
    suspicious_keywords = ['login', 'secure', 'account', 'update', 'verify', 'bank', 'password']
    keyword_count = sum([url.count(keyword) for keyword in suspicious_keywords])
    features.append(keyword_count)
    
    # TLD Risk Feature - Assigns risk score to Top-Level Domains
    tld = url.split('.')[-1].split('/')[0]
    risky_tlds = {'xyz': 3, 'top': 3, 'ru': 2, 'tk': 2, 'work': 1}
    features.append(risky_tlds.get(tld, 0)) # Assigns score, or 0 if not in our list
    
    # Brand Name Misspelling (simple version)
    misspelled_brands = ['paypa1', 'amaz0n', 'g00gle']
    has_misspelling = 1 if any(brand in url for brand in misspelled_brands) else 0
    features.append(has_misspelling)
    
    return features

# --- Main Training Logic ---
print("🚀 Starting model training...")
try:
    # Use a slightly bigger dummy dataset for better training
    data_dict = {
        'URL': [
            'google.com', 'facebook.com/home', 'youtube.com', 'en.wikipedia.org',
            'secure-login-mybank.com/update', 'verify-your-amaz0n-account.xyz/password',
            'paypal.com.confirm-login.ru', 'apple-support-service.tk/verify',
            '192.168.1.1/admin', 'myuniversity.edu/portal'
        ],
        'label': [0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
    }
    data = pd.DataFrame(data_dict)
    data.to_csv('phishing_data.csv', index=False)
    print("Created 'phishing_data.csv' with sample data.")
except Exception as e:
    print(f"Could not create dummy data: {e}")

X = np.array([extract_features(url) for url in data['URL']])
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Using RandomForest for better accuracy
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print(f"Model Accuracy: {model.score(X_test, y_test) * 100:.2f}%")

joblib.dump(model, 'phishing_model.pkl')
print("✅ Innovative model saved successfully as 'phishing_model.pkl'")