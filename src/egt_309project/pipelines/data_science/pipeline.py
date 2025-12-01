"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, train_rf_model, evaluate_model, train_xgb_model, train_mlpclassifier_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs="cleaned_data",
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node",
        ),
        node(
            func=train_rf_model,
            inputs=["X_train", "y_train"],
            outputs="rf_model",
            name="train_rf_node",
        ),
        node(
            func=evaluate_model,
            inputs=["rf_model", "X_test", "y_test"],
            outputs=None,
            name="evaluate_rf_model_node",
        ),
        node(
            func=train_xgb_model,
            inputs=["X_train", "y_train"],
            outputs="xgb_model",
            name="train_xgb_node",
        ),
        node(
            func=evaluate_model,
            inputs=["xgb_model", "X_test", "y_test"],
            outputs=None,
            name="evaluate_xgb_model_node",
        ),
        node(
            func=train_mlpclassifier_model,
            inputs=["X_train", "y_train"],
            outputs="mlp_model",
            name="train_mlp_node",
        ),
        node(
            func=evaluate_model,
            inputs=["mlp_model", "X_test", "y_test"],
            outputs=None,
            name="evaluate_mlp_model_node",
        ),
    ])