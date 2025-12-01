from kedro.pipeline import Pipeline, node, pipeline
from .nodes import clean_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=clean_data,
            inputs=None,          # <--- CHANGED: No input needed from catalog
            outputs="cleaned_data",
            name="clean_data_node",
        ),
    ])