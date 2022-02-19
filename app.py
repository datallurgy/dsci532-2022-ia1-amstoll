from dash import Dash, dcc, html, Input, Output
import altair as alt
from vega_datasets import data

# import data
iris = data.iris()

## Setup app and layout/frontend
app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Dropdown(
            id='xcol', value='sepalLength',
            options=[{'label': i, 'value': i} for i in iris.columns]),
        dcc.RadioItems(
            id='radio_species',
            options=[
                {'label': 'None', 'value': 'blue'},
                {'label': 'Species', 'value': 'species'}],
                value='Species')])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol', 'value'),
    Input('radio_species', 'value'))
def plot_altair(xcol, radio_species):
    chart = alt.Chart(iris).mark_circle().encode(
        x = xcol,
        y = 'sepalWidth',
        color = 'species',
        tooltip='species').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)