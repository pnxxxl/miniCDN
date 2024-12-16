from flask import Flask, jsonify
import time

app = Flask(__name__)

# Простой словарь для имитации кэша
cache = {}

@app.route('/api/cache/add/<path:key>/<data>', methods=['POST'])
def add_to_cache(key, data):
    cache[key] = {'data': data, 'timestamp': time.time()}
    return jsonify({'message': f'Key "{key}" added to cache'}), 201

@app.route('/api/cache/get/<path:key>')
def get_from_cache(key):
    if key in cache:
        return jsonify({'key': key, 'data': cache[key]['data'], 'timestamp': cache[key]['timestamp']})
    else:
        return jsonify({'message': f'Key "{key}" not found in cache'}), 404


@app.route('/api/cache/info')
def cache_info():
    return jsonify({'cache_size': len(cache), 'items': cache})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) # Заметьте порт 5001


