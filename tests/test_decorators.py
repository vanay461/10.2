import pytest
import os
import logging
from src.decorators import log


@log()
def add(x, y):
    return x + y


@log(filename="test_log.txt")
def divide(x, y):
    return x / y


@log()
def error_func():
    raise ValueError("Test error")


def test_log_console(caplog):
    add(2, 3)
    assert "add ok" in caplog.text


def test_log_file():
    log_file = "test_log.txt"

    # Удаляем файл перед тестом, чтобы избежать остатков старых логов
    if os.path.exists(log_file):
        os.remove(log_file)

    # Вызываем функцию, которая должна записывать лог в файл
    divide(10, 2)

    # Проверяем, что файл действительно создан
    assert os.path.exists(log_file), "Лог-файл не был создан!"

    # Читаем содержимое лога
    with open(log_file, "r", encoding="utf-8") as f:
        log_contents = f.read()

    assert "divide ok" in log_contents  # Проверяем, что запись есть

    # Очищаем логгер
    logger = logging.getLogger("divide")
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()


def test_log_exception(caplog, capsys):
    with pytest.raises(ValueError, match="Test error"):
        error_func()

    assert "error_func error: Test error" in caplog.text  # Проверяем в caplog

    captured = capsys.readouterr()
    assert "error_func error: Test error" in captured.err  # Проверяем stderr

