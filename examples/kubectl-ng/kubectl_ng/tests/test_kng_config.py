# SPDX-FileCopyrightText: Copyright (c) 2024, Kr8s Developers (See LICENSE for list)
# SPDX-License-Identifier: BSD 3-Clause License
from kubectl_ng.cli import app
from typer.testing import CliRunner

import kr8s

runner = CliRunner()


def test_current_context():
    current_context = kr8s.api().auth.kubeconfig.current_context
    result = runner.invoke(app, ["config", "current-context"])
    assert result.exit_code == 0
    assert current_context in result.stdout


def test_get_clusters(k8s_cluster):
    result = runner.invoke(app, ["config", "get-clusters"])
    assert result.exit_code == 0
    assert k8s_cluster.name in result.stdout


def test_get_users(k8s_cluster):
    result = runner.invoke(app, ["config", "get-users"])
    assert result.exit_code == 0
    assert k8s_cluster.name in result.stdout
