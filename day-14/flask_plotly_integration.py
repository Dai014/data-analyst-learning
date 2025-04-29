from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load your dataset here
    df = pd.read_csv('your_dataset.csv')  # Replace with your actual dataset path
    fig = px.density_heatmap(df, x='x_column', y='y_column', z='z_column')  # Replace with your actual column names
    graph_html = fig.to_html(full_html=False)
    return render_template('heatmap.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)