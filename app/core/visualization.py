import plotly.express as px
from plotly.graph_objects import Figure
from app.models.simulation import SimulationMetrics

def create_stability_plot(metrics: SimulationMetrics) -> Figure:
    """Generate interactive stability plot"""
    fig = px.line(
        metrics.df,
        x="timestamp",
        y="stability_score",
        title="Robot Stability Over Time",
        labels={"stability_score": "Stability Score (%)"}
    )
    fig.update_layout(hovermode="x unified")
    return fig