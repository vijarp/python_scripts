import pygal

# Create a Pygal chart object (assuming 'SVG' chart type for this example)
chart = pygal.Circle()

# Add nodes (modify labels and values as needed)
chart.add('Data Analytics with Python', [
    ('Data Manipulation', 2),
    ('Statistical Analysis', 3),
    ('Machine Learning', 5),
    ('Natural Language Processing', 2),
    ('Time Series Analysis', 1),
    ('Database Operations', 4)
])

# Customize individual node properties
chart.nodes['Data Manipulation'].stroke = 'blue'  # Set stroke color for 'Data Manipulation'
chart.nodes['Statistical Analysis'].fill_color = 'green'  # Set fill color for 'Statistical Analysis'
chart.nodes['Machine Learning'].stroke = 'coral'  # Set stroke color for 'Machine Learning'
chart.nodes['Natural Language Processing'].fill_color = 'pink'  # Set fill color for 'NLP'
chart.nodes['Time Series Analysis'].fill_color = 'yellow'  # Set fill color for 'Time Series'
chart.nodes['Database Operations'].stroke = 'goldenrod'  # Set stroke color for 'DB Operations'

# Subcategories within nodes (using nested charts)
chart.nodes['Data Manipulation'].add('Data Visualization', 1)
chart.nodes['Data Manipulation'].add('Web Scraping', 1)

chart.nodes['Machine Learning'].add('Scikit-learn', 1)
chart.nodes['Machine Learning'].add('TensorFlow', 1)
chart.nodes['Machine Learning'].add('PyTorch', 1)
chart.nodes['Machine Learning'].add('XGBoost', 1)

chart.nodes['Natural Language Processing'].add('NLTK', 1)
chart.nodes['Natural Language Processing'].add('spaCy', 1)

# You can add more subcategories within nodes following this pattern

# Render the chart
chart.render_to_file('data_analytics_with_python.svg')