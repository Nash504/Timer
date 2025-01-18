from flask import Flask, render_template, request, redirect, url_for, session
from supabase_py import create_client
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv('FLASK_SECRET_KEY')  # Set a secret key for sessions

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)

@app.route('/')
def index():
    # Check if session ID exists, else create one
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())  # Create a unique session ID

    # Retrieve only the entries associated with the session ID
    response = supabase.table("times").select("*").eq("session_id", session['session_id']).order("category").execute()
    return render_template('index.html', times=response['data'])

@app.route('/add_user', methods=['POST'])
def add_user():
    # Retrieve data from the form
    name = request.form.get('name').title()
    time = request.form.get('time')
    category = request.form.get('category').title()

    # Get the session ID
    session_id = session.get('session_id')

    # Insert user data along with session ID to ensure uniqueness
    response = supabase.table("times").insert([{"name": name, "time": time, "category": category, "session_id": session_id}]).execute()
    return redirect(url_for("index"))

@app.route('/remove_user/<string:name>')
def remove_user(name):
    try:
        # Get the session ID
        session_id = session.get('session_id')

        # Delete the entry associated with both name and session ID
        response = supabase.table("times").delete().eq("name", name).eq("session_id", session_id).execute()

        # Check if the delete operation was successful
        if response.status_code == 200:
            return redirect(url_for("index"))
        else:
            raise Exception("Failed to delete user")
    except Exception as e:
        # Log the error if there's an issue
        print(f"Error removing user: {e}")
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
