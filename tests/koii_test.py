from koii import Koii


def test_fake():
    assert True


def test_koii__normalize_routes(flask_app):
    normalized_routes = Koii._normalize_routes(flask_app.url_map)

    assert len(normalized_routes) == 4


def test_koii__generate_routes(flask_app):
    route = Koii._generate_routes(flask_app.url_map._rules[0])

    assert len(route) == 1
    assert len(route[0]) == 2
    assert 'GET' in route[0][0]
    assert 'filename' in route[0][1]


def test_koii__style_routes(flask_app):
    normalized_routes = Koii._normalize_routes(flask_app.url_map)
    styled_routes = Koii._style_routes(normalized_routes)

    assert 'METHOD' in styled_routes
    assert 'PATH' in styled_routes
    assert '/proton' in styled_routes
    assert 'PATCH' in styled_routes
    assert 'GET' in styled_routes
