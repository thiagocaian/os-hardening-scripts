import platform
import pytest

from src import check_linux, check_windows, check_macos

system = platform.system().lower()

@pytest.mark.skipif(system != "linux", reason="Somente Linux")
def test_linux_shadow():
    ok, msg = check_linux.check_shadow_permissions()
    assert isinstance(ok, bool)
    assert isinstance(msg, str)

@pytest.mark.skipif(system != "windows", reason="Somente Windows")
def test_windows_services():
    ok, msg = check_windows.check_services()
    assert isinstance(ok, bool)
    assert isinstance(msg, str)

@pytest.mark.skipif(system != "darwin", reason="Somente macOS")
def test_macos_filevault():
    ok, msg = check_macos.check_filevault()
    assert isinstance(ok, bool)
    assert isinstance(msg, str)
