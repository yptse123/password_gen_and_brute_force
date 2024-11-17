# Backend with Python
# 1. Password Generator
import random
import string
import time
import itertools
from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
import multiprocessing

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
characters = string.ascii_lowercase + string.digits

# Function to generate a random password with a given length
def generate_password(length):
    return ''.join(random.choice(characters) for _ in range(length))

# API endpoint to generate passwords
@app.route('/generate_passwords', methods=['GET'])
def generate_passwords():
    passwords = {}
    for length in range(1, 7):
        passwords[length] = [generate_password(length) for _ in range(10)]
    return jsonify(passwords)

# Function to brute force a password
def brute_force_crack(password, result_dict, index):
    start_time = time.time()
    print(f"Starting brute force for password: {password}")
    for length in range(1, len(password) + 1):
        for attempt in itertools.product(characters, repeat=length):
            if ''.join(attempt) == password:
                end_time = time.time() - start_time
                print(f"Password {password} cracked in {end_time} seconds")
                result_dict[index] = end_time
                return
    result_dict[index] = None

# API endpoint to perform brute force cracking
@app.route('/crack_passwords', methods=['POST'])
def crack_passwords():
    passwords = request.json.get('passwords', {})
    crack_times = {}
    threads = []
    # as threads amount will affect the accuracy, we limit the amount of threads
    max_threads = multiprocessing.cpu_count()
    result_dict = {}
    
    for length, pw_list in passwords.items():
        length = int(length)
        crack_times[length] = []
        for i, password in enumerate(pw_list):
            print(f"Attempting to crack password of length {length}: {password}")
            while threading.active_count() > max_threads:
                time.sleep(0.5)
            thread = threading.Thread(target=brute_force_crack, args=(password, result_dict, f"{length}_{i}"))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Collect results
    for length, pw_list in passwords.items():
        length = int(length)
        for i in range(len(pw_list)):
            crack_times[length].append({'password': pw_list[i], 'time': result_dict.get(f"{length}_{i}")})
    
    return jsonify(crack_times)

if __name__ == '__main__':
    app.run(debug=True)
