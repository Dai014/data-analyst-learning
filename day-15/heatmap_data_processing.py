def create_heatmap_data(data):
    """
    Process the input data to create x, y, z coordinates for the heatmap.

    Parameters:
    data (list of dict): Input data containing time series information.

    Returns:
    tuple: Three lists representing x, y, z coordinates for the heatmap.
    """
    x = []
    y = []
    z = []

    for entry in data:
        # Assuming 'time' is a key in the entry dict for x-axis
        x.append(entry['time'])
        # Assuming 'category' is a key in the entry dict for y-axis
        y.append(entry['category'])
        # Assuming 'value' is a key in the entry dict for z-axis
        z.append(entry['value'])

    return x, y, z

def filter_data(data, condition):
    """
    Filter the input data based on a given condition.

    Parameters:
    data (list of dict): Input data to be filtered.
    condition (function): A function that defines the filtering condition.

    Returns:
    list: Filtered data.
    """
    return [entry for entry in data if condition(entry)]