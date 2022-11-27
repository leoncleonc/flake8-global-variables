import subprocess


def test_correct_module(absolute_path):
    filename = absolute_path('fixtures', 'correct.py')
    process = subprocess.Popen(
        [
            'flake8',
            '--isolated',
            '--select',
            'GV4',
            filename,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = process.communicate()

    assert len(stdout) == 0, stdout


def test_incorrect_fixture(absolute_path):
    filename = absolute_path('fixtures', 'incorrect.py')
    process = subprocess.Popen(
        [
            'flake8',
            '--isolated',
            '--select',
            'GV4',
            filename,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = process.communicate()

    assert stdout.count(b'GV400') == 2
