from dash import Dash, dcc, html, Input, Output, callback
from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
import plotly.graph_objects as go

#app = Dash(__name__)
d_app = Dash(__name__)
dapp = Blueprint('dapp', __name__)

def make_dash(app):
    d_app = Dash(__name__, server=app, url_base_pathname='/1212yuyu2u216612bnbdash/')
    
    d_app.layout = html.Div([
        html.H4('Interactive color selection with simple Dash example'),
        html.P("Select color:"),
        dcc.Dropdown(
            id="getting-started-x-dropdown",
            options=['Gold', 'MediumTurquoise', 'LightGreen'],
            value='Gold',
            clearable=False,
        ),
        dcc.Graph(id="getting-started-x-graph"),
    ])
    
    @callback(
    Output("getting-started-x-graph", "figure"), 
    Input("getting-started-x-dropdown", "value"))
    def display_color(color):
        fig = go.Figure(
            data=go.Bar(y=[2, 3, 1], # replace with your own data source
                        marker_color=color))
        return fig

@dapp.route('/plot_dash') 
@login_required
def index():    
#    dapp.layout = html.Div([
#        html.H4('Interactive color selection with simple Dash example'),
#        html.P("Select color:"),
#        dcc.Dropdown(
#            id="getting-started-x-dropdown",
#            options=['Gold', 'MediumTurquoise', 'LightGreen'],
#            value='Gold',
#            clearable=False,
#        ),
#        dcc.Graph(id="getting-started-x-graph"),
#    ])
    return render_template('dash.html', iframe='/1212yuyu2u216612bnbdash')
    #return redirect("/dash")
    #return d_app.redirect('/dash')
    

@d_app.callback(
    Output("getting-started-x-graph", "figure"), 
    Input("getting-started-x-dropdown", "value"))
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], # replace with your own data source
                    marker_color=color))
    return fig


#if __name__ == "__main__":
 #   app.run_server(debug=True)
