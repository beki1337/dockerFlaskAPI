import docker
import pytest

from app import terminal


cwd = "/"

@pytest.fixture(scope="module")
def docker_client():
    client = docker.from_env()
    return client


@pytest.fixture(scope="module")
def docker_container(docker_client):
    container = docker_client.containers.run(
        "git-image",
        "sleep infinity",
        detach=True,
        name="git-container",
    )
    yield container
    container.stop()


def test_terminal(docker_container):
    cwd = "/"
    command = "ls"
    output, new_cwd = terminal(command, cwd,docker_container)
    assert output.strip() == "bin\ndev\netc\nhome\nlib\nlib64\nmedia\nmnt\nopt\nproc\nroot\nrun\nsbin\nsrv\nsys\ntmp\nusr\nvar"
    assert new_cwd == "/"

