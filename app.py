from flask import Flask, render_template, request, redirect, url_for
from supabase_py import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='templates')
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)

@app.route('/')
def index():
    response = supabase.table("times").select("*").execute()
    return render_template('index.html', times=response['data'])

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name').title()
    time = request.form.get('time')  # This time will be submitted with the form
    response = supabase.table("times").insert([{"name": name, "time": time }]).execute()
    return redirect(url_for("index"))

@app.route('/remove_user/<string:name>')
def remove_user(name):
    try:
        # Attempt to delete the user from Supabase
        response = supabase.table("times").delete().eq("name", name).execute()

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
