import pandas as pd
import plotly.express as px

def create_heatmap(data):
    fig = px.imshow(data, 
                    labels=dict(x="X Axis", y="Y Axis", color="Value"),
                    x=data.columns,
                    y=data.index)
    fig.update_layout(title="Heatmap Visualization")
    fig.show()

if __name__ == "__main__":
    # Sample data for demonstration
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }, index=['Row 1', 'Row 2', 'Row 3'])
    
    create_heatmap(data)