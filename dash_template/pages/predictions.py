# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        html.H2('Contraception Use', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Uplifted'), 
        dcc.Slider(
            id='effect_uplifted', 
            min=16, 
            max=50, 
            step=1, 
            value=16, 
            marks={n: str(n) for n in range(16,50,2)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Happy'), 
        dcc.Dropdown(
            id='effect_happy', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
            ], 
            value = 0, 
            className='mb-5', 
        ),  
        dcc.Markdown('#### Relaxed'), 
        dcc.Slider(
            id='effect_relaxed', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Energetic'), 
        dcc.Dropdown(
            id='effect_energetic', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Creative'), 
        dcc.Dropdown(
            id='effective_creative', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Focused'), 
        dcc.Dropdown(
            id='effect_focused', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Talkative'), 
        dcc.Dropdown(
            id='effect_talkative', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
 
            ], 
            value = 2, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Euphoric'), 
        dcc.Dropdown(
            id='effect_euphoric', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Giggly'), 
        dcc.Dropdown(
            id='effect_giggly', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Hungry'), 
        dcc.Dropdown(
            id='effect_hungry', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Aroused'), 
        dcc.Dropdown(
            id='effect_aroused', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Tingly'), 
        dcc.Dropdown(
            id='effect_tingly', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
 
            ], 
            value = 0, 
            className='mb-5', 
        ), 

        """Possibly leave this one out?"""
        dcc.Markdown('#### None'), 
        dcc.Dropdown(
            id='effect_none', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
 
            ], 
            value = 0, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Sleepy'), 
        dcc.Dropdown(
            id='effect_none', 
            options = [
                {'label': 'No', 'value': 0}, 
                {'label': 'Yes', 'value': 1}, 
 
            ], 
            value = 0, 
            className='mb-5', 
        ), 

    ],
        md=4,
)

layout = dbc.Row([column1, column2])