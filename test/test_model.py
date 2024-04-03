import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from model import split_data, train_model, evaluate_model, plot_metrics
import matplotlib.pyplot as plt

# Sample data generation
def generate_sample_data(num_rows=100):
    """Generate a sample DataFrame for testing."""
    data = pd.DataFrame({
        'feature1': np.random.rand(num_rows),
        'feature2': np.random.rand(num_rows),
        'target': np.random.randint(2, size=num_rows)
    })
    return data

# Test split_data function
def test_split_data():
    df = generate_sample_data()
    X_train, X_test, y_train, y_test = split_data(df, 'target')
    assert len(X_train) == len(y_train)  # Check if the split is consistent
    assert len(X_test) == len(y_test)
    assert len(df) == len(X_train) + len(X_test)  # Ensure no data is lost

# Test train_model function
def test_train_model():
    df = generate_sample_data()
    X_train, X_test, y_train, y_test = split_data(df, 'target')
    model = LogisticRegression()
    trained_model = train_model(model, X_train, y_train)
    assert trained_model is not None

# Test evaluate_model function
def test_evaluate_model():
    df = generate_sample_data()
    X_train, X_test, y_train, y_test = split_data(df, 'target')
    model = LogisticRegression().fit(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)
    assert 'accuracy' in metrics
    assert 'precision' in metrics
    assert 'recall' in metrics

# Test plot_metrics function
def test_plot_metrics():
    metrics = {'accuracy': 0.9, 'precision': 0.8, 'recall': 0.85}
    filename = "test_metrics_plot.png"
    directory = "./"
    plot_metrics(metrics, filename, directory)
    assert os.path.exists(os.path.join(directory, filename))
    os.remove(os.path.join(directory, filename))  # Clean up

