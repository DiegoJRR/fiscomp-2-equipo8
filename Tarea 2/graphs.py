import plotly.graph_objects as go

def graph_3d(x, y, z):
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                    mode='markers', marker=dict(
            size=6,
            colorscale='Viridis',
            opacity=0.8
        ))])
    fig.show()

def graph_2d(x, y, title, ax):
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.plot(x[0], y[0], markersize=12, marker='o', color='green')
    ax.plot(x[-1], y[-1], markersize=10, marker='o', color='red')

    ax.legend(["Caminata", "Inicio", "Fin"])
    ax.set_title(title)
