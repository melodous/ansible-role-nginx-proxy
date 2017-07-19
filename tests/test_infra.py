def test_nginx_server_running_and_enabled(Command, Service):
    # Check that docker service is running and enabled
    docker_service = Service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled
    # Check that nginx service is running and enabled
    nginx_service = Service("nginx")
    assert nginx_service.is_running
    assert nginx_service.is_enabled


def test_nginx_start_stop(Command, Service):
    # Check init scripts are working
    Command.run_expect([0], "systemctl stop nginx")
    nginx_service = Service("nginx")
    assert not nginx_service.is_running
    Command.run_expect([0], "systemctl start nginx")
    assert nginx_service.is_running
    Command.run_expect([0], "systemctl restart nginx")
    assert nginx_service.is_running
