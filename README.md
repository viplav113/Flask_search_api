# Flask YouTube Comment Search API

This Flask-based REST API interacts with the YouTube comment fetching API to perform various searches on comments based on different criteria.

## Requirements
- Python 3.6+
- Flask
- Requests

## Installation
1. Clone this repository: `git clone <repository_link>`
2. Navigate to the project directory: `cd flask-youtube-comment-api`
3. Create a virtual environment:
   - Windows: `python -m venv venv`
   - MacOS/Linux: `python3 -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - MacOS/Linux: `source venv/bin/activate`
5. Install required libraries: `pip install -r requirements.txt`

## Running the API
1. Ensure you are in the project directory.
2. Run the Flask application:
python name_of_file.py
3. 3. The application will start running on `http://127.0.0.1:5000/`.

## API Endpoints
### Search by Criteria
- **Endpoint**: `/search`
- **Methods**: `GET`
- **Parameters**:
- `search_author`: Author name to search comments for.
- `at_from`, `at_to`: Date range (from and to) for comment posting.
- `like_from`, `like_to`: Like count range.
- `reply_from`, `reply_to`: Reply count range.
- `search_text`: Text string to search within comments.

### Example Usage
1. Search by author, date, likes, replies, and text:
<base-url>/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&search_text=economic
2. Search by author only:
<base-url>/search?search_author=Fredrick

## How to Use
- Replace `<base-url>` with the server's URL or `http://127.0.0.1:5000/` if running locally.
- Use the different parameters in the endpoint to search for comments based on your criteria.

Feel free to explore different combinations of parameters to search for specific comments.
