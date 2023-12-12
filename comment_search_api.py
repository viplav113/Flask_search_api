from flask import Flask, jsonify, request
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/search')
def fetch_text_by_criteria():
    try:
        author_name = request.args.get('search_author')
        date_from_str = request.args.get('at_from')
        date_to_str = request.args.get('at_to')
        like_from = int(request.args.get('like_from', 0))
        like_to = int(request.args.get('like_to', 999999))
        reply_from = int(request.args.get('reply_from', 0))
        reply_to = int(request.args.get('reply_to', 999999))
        search_text = request.args.get('search_text')
        
        if not author_name:
            return jsonify({'error': 'Author name not provided'})

        url = 'https://app.ylytic.com/ylytic/test'
        response = requests.get(url)

        if response.status_code == 200:
            comments = response.json()['comments']
            
            filtered_comments = []
            
            for comment in comments:
                if comment['author'].lower().find(author_name.lower()) != -1:
                    date_comment = datetime.strptime(comment['at'], '%a, %d %b %Y %H:%M:%S %Z')
                    
                    if date_from_str and date_to_str:
                        date_from = datetime.strptime(date_from_str, '%d-%m-%Y')
                        date_to = datetime.strptime(date_to_str, '%d-%m-%Y')
                        if not (date_from <= date_comment <= date_to):
                            continue
                    
                    if not (like_from <= comment['like'] <= like_to):
                        continue
                    
                    if not (reply_from <= comment['reply'] <= reply_to):
                        continue
                    
                    if search_text and search_text.lower() not in comment['text'].lower():
                        continue
                    
                    filtered_comments.append(comment['text'])

            return jsonify({'data': filtered_comments})
        
        else:
            return jsonify({'error': f'Failed to fetch data. Status code: {response.status_code}'})

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'})

if __name__ == '__main__':
    port = 5000
    app.run(port=port)
