from fastapi.testclient import TestClient

from app.core.config import settings


def test_markdown(
    client: TestClient, superuser_token_headers: dict,
) -> None:
    data = {'data':"# Header one \n"}
    r = client.post(
        f"{settings.API_V1_STR}/markdown/",
        headers=superuser_token_headers,
        json=data
    )
    assert r.json() == "<h1>Header one</h1>"