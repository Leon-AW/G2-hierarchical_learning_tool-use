import pickle

# Path to your .pickle file within the experiment_logs directory
pickle_file = 'experiment_logs/42-none-full-True-RMB-200000-interests_evolution.pickle'

with open(pickle_file, 'rb') as file:
    data = pickle.load(file)
    # Check if data is iterable (e.g., list, dict, etc.) but not a string
    if hasattr(data, '__iter__') and not isinstance(data, str):
        # Print first 100 items/lines
        for i, item in enumerate(data):
            if i >= 100:  # Stop after 100 items
                break
            print(item)
    else:
        print(data)  # If data is not iterable or is a simple data type, print it directly