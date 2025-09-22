from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# --- Load Model and Define Feature Extraction ---
model = joblib.load('phishing_model.pkl')

# IMPORTANT: This must be the EXACT same function as in your training script.
def extract_features(url):
    features = []
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('/'))
    features.append(url.count('-'))
    suspicious_keywords = ['login', 'secure', 'account', 'update', 'verify', 'bank', 'password']
    keyword_count = sum([url.count(keyword) for keyword in suspicious_keywords])
    features.append(keyword_count)
    tld = url.split('.')[-1].split('/')[0]
    risky_tlds = {'xyz': 3, 'top': 3, 'ru': 2, 'tk': 2, 'work': 1}
    features.append(risky_tlds.get(tld, 0))
    misspelled_brands = ['paypa1', 'amaz0n', 'g00gle']
    has_misspelling = 1 if any(brand in url for brand in misspelled_brands) else 0
    features.append(has_misspelling)
    return features

# --- INNOVATIVE API ENDPOINT ---
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    
    # Extract features and predict probability
    features_extracted = np.array(extract_features(url)).reshape(1, -7)
    prediction_proba = model.predict_proba(features_extracted)[0]
    
    phishing_score = int(prediction_proba[1] * 100) # Score from 0 to 100
    
    # Generate a reason for the score
    reason = "URL appears safe."
    if phishing_score > 75:
        reason = "High risk! URL contains multiple suspicious indicators."
    elif phishing_score > 50:
        reason = "Caution! URL has some suspicious characteristics."
    
    result = 'dangerous' if phishing_score > 50 else 'safe'

    return jsonify({
        'result': result,
        'score': phishing_score,
        'reason': reason
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)