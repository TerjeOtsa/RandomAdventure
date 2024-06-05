from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)


# Directory where activity CSV files are stored
activity_dir = 'activities'

def load_activities(city):
    csv_file = os.path.join(activity_dir, f'{city}.csv')
    if not os.path.exists(csv_file):
        return pd.DataFrame(columns=["activity", "time", "intensity"])
    return pd.read_csv(csv_file)

def save_activities(df, city):
    csv_file = os.path.join(activity_dir, f'{city}.csv')
    df.to_csv(csv_file, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/randomize', methods=['POST'])
def randomize():
    data = request.get_json()
    time = int(data['time'])
    intensity = int(data['intensity'])
    city = data['city']

    activities_df = load_activities(city)
    
    # Normalize the time to a scale from 1 to 10
    def normalize_time(x):
        return max(min((9/115) * x + 0.6087, 10), 1)
    
    activities_df['normalized_time'] = activities_df['time'].apply(normalize_time)
    
    # Adjust weights with the normalized time
    activities_df['time_weight'] = activities_df['normalized_time'].apply(lambda x: 1 / abs(x - time) if abs(x - time) != 0 else 1)
    activities_df['intensity_weight'] = activities_df['intensity'].apply(lambda x: 2 / abs(x - intensity) if abs(x - intensity) != 0 else 2)
    activities_df['combined_weight'] = activities_df['time_weight'] * activities_df['intensity_weight']
    activities_df['normalized_weight'] = activities_df['combined_weight'] / activities_df['combined_weight'].sum()

    activity = activities_df.sample(weights=activities_df['normalized_weight']).iloc[0]['activity']
    return jsonify({'activity': activity})

@app.route('/add_activity', methods=['POST'])
def add_activity():
    data = request.get_json()
    activity = data['activity']
    time = int(data['time'])
    intensity = int(data['intensity'])
    city = data['city']

    activities_df = load_activities(city)
    new_activity = pd.DataFrame([[activity, time, intensity]], columns=["activity", "time", "intensity"])
    activities_df = pd.concat([activities_df, new_activity], ignore_index=True)
    save_activities(activities_df, city)
    return jsonify({'message': 'Activity added successfully'})

@app.route('/remove_activity', methods=['POST'])
def remove_activity():
    data = request.get_json()
    activity = data['activity']
    city = data['city']

    activities_df = load_activities(city)
    activities_df = activities_df[activities_df['activity'] != activity]
    save_activities(activities_df, city)
    return jsonify({'message': 'Activity removed successfully'})

@app.route('/suggest_activities', methods=['GET'])
def suggest_activities():
    query = request.args.get('query', '').lower()
    city = request.args.get('city', '').lower()
    activities_df = load_activities(city)
    suggestions = activities_df[activities_df['activity'].str.lower().str.contains(query, na=False)]
    return jsonify(suggestions['activity'].tolist())

@app.route('/load_city_activities', methods=['GET'])
def load_city_activities():
    city = request.args.get('city', '').lower()
    activities_df = load_activities(city)
    return jsonify(activities_df.to_dict(orient='records'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
