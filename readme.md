# Password Cracking Demo

This project is a demonstration of a password generator and a brute-force password cracking tool implemented using Python. It includes a backend built with Flask, which provides APIs for generating passwords and cracking them using multithreading.

## Features

1. **Password Generator**: Generates random passwords of lengths ranging from 1 to 6 characters.
2. **Brute Force Cracking**: Uses multithreading to efficiently crack passwords by attempting all possible combinations of characters.
3. **REST API**: Provides two endpoints to generate passwords and crack them using a brute-force method.

## Technologies Used

- **Python**: Backend development.
- **Flask**: Web framework for creating REST API endpoints.
- **Flask-CORS**: To handle Cross-Origin Resource Sharing (CORS) issues.
- **Threading**: Multithreading for concurrent password cracking.

## Endpoints

### 1. Generate Passwords

**URL**: `/generate_passwords`  
**Method**: `GET`  
**Description**: Generates random passwords of lengths from 1 to 6, with 10 passwords per length.

**Response**:
```json
{
  "1": ["k", "C", "<", "H", "b", "t", "'", ")", "y", "1"],
  "2": ["<s", "bW", "XB", ...],
  ...
}
```

### 2. Crack Passwords

**URL**: `/crack_passwords`  
**Method**: `POST`  
**Description**: Takes a list of passwords and uses brute force to crack each one. Uses multithreading to speed up the cracking process.

**Request Body**:
```json
{
  "passwords": {
    "1": ["k", "C", "<", ...],
    "2": ["<s", "bW", "XB", ...],
    ...
  }
}
```

**Response**:
```json
{
  "1": [
    {"password": "k", "time": 0.0012},
    {"password": "C", "time": 0.0010},
    ...
  ],
  "2": [
    {"password": "<s", "time": 0.0054},
    ...
  ],
  ...
}
```

## Running the Application

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Install the required packages:
   ```bash
   pip install flask flask-cors
   ```

3. **Run the Server**:
   ```bash
   python <script_name>.py
   ```
   The server will start at `http://127.0.0.1:5000`.

## Usage

- **Generate Passwords**: Use a tool like Postman or simply open your browser and navigate to `http://127.0.0.1:5000/generate_passwords` to generate passwords.
- **Crack Passwords**: Use Postman or any REST client to send a `POST` request to `http://127.0.0.1:5000/crack_passwords` with the generated passwords to crack them.

## Example Output

- Password generation and cracking times will be displayed in the console, as well as returned in the response JSON for easy understanding.

## Notes

- The brute-force cracking process uses multithreading to improve performance, but cracking even short passwords can take considerable time depending on the complexity.
- This project is for educational purposes only and should not be used for any malicious activities.

## License

This project is open-source and available under the MIT License.

