

---

# Timer App ⏱️

A web application to manage and display time records, allowing users to add and delete time entries seamlessly. Built with **Flask**, **Bootstrap**, and integrated with **Supabase** for database operations.

## Features

- Add a user and their corresponding time record.
- View all time records in a structured format.
- Delete a specific time record by name and time.
- Responsive design using **Bootstrap**.

## Technologies Used

- **Flask**: For backend application logic.
- **Supabase**: For managing and storing data in a PostgreSQL database.
- **Bootstrap**: For responsive and modern UI design.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/timer-app.git
   cd timer-app
   ```

2. **Set up the environment:**
   - Install dependencies:
     ```bash
     pip install flask python-dotenv supabase-py
     ```
   - Create a `.env` file and add your Supabase credentials:
     ```
     SUPABASE_URL=your_supabase_url
     SUPABASE_KEY=your_supabase_key
     ```

3. **Run the app:**
   ```bash
   python app.py
   ```

4. **Access the app:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. **Add a Time Record:**
   - Enter the name and time in the provided form.
   - Click "Submit" to save the entry.

2. **Delete a Time Record:**
   - Click the "Delete" button next to the specific time record.

## File Structure

```
timer-app/
├── templates/
│   └── index.html      # HTML template for the app
├── app.py              # Main Flask application file
├── .env                # Supabase credentials
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

