
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Markdown('''
    # 見出し1
    ## 見出し2

    - 箇条書き1
    - 箇条書き2
    - 箇条書き3
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)
