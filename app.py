from flask import Flask, render_template, request
import pickle
import numpy as np

# Load pre-processed data and models
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_rating'].values)
    )

@app.route('/recommend')
def recommend_ui():
    # Pass book names to populate the dropdown dynamically
    book_titles = list(popular_df['Book-Title'].values)
    return render_template('recommend.html', book_titles=book_titles)

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    try:
        # Find the index of the user-inputted book
        index = np.where(pt.index == user_input)[0][0]

        # Get similar books based on similarity scores
        similar_items = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:9]

        # Prepare the data for rendering
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)

        return render_template('recommend.html', data=data)

    except IndexError:
        # Handle the case when the book is not found
        error_message = (
            "Oops! The book you entered is not found. "
            "Please try searching for another book from the suggestions, "
            "or check for any typos in the book title."
        )
        return render_template('recommend.html', error_message=error_message)

    except Exception as e:
        # Handle unexpected errors
        error_message = (
            "Sorry, something went wrong while processing your request. "
            "Please try again later or contact support if the issue persists."
        )
        return render_template('recommend.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
