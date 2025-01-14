# app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Get environment from env var, default to 'development'
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

@app.route('/')
def hello():
    return jsonify({
        'message': f'Hello from {ENVIRONMENT}!',
        'status': 'ok'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'environment': ENVIRONMENT,
        'version': os.getenv('APP_VERSION', 'unknown')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
