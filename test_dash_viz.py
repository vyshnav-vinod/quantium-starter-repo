import dash

from dash_viz import app

def test_001_header_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#header-text").text == "Pink Morsel Sales"

def test_002_viz_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#line-graph") != None

def test_003_region_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#radio-region") != None