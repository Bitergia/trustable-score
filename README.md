# Trustable score

Trustable score is a Django application that provides a simple and efficient way
to calculate and provide scores for repositories.

## Installation

### 1. Install the package

The recommended way to install Trustable score Django application is to use
[poetry](https://python-poetry.org/).
This package manager will install the tool and all its dependencies.
You can install `poetry` by following [this guide](https://python-poetry.org/docs/#installation).

1. Clone the repository:

    ```bash
    git clone git@github.com:Bitergia/trustable-score.git
    cd trustable-score
    ```

2. Install dependencies and tool:

    ```bash
    poetry update
    poetry install
    ```

### 2. Install the application

Add the `trustable_score` app to your Django project. You can do this by adding
the following line to your `settings.py` file:

```python
INSTALLED_APPS = [
    # ...
    'trustable_score',
    # ...
]
```

### 3. Add the URLs

Add the following line to your `urls.py` file:

```python
from trustable_score.urls import urlpatterns as trustable_score_urls

urlpatterns = trustable_score_urls + [
    # ... your URL conf ...
]
```

## Usage

This application provides a simple API to calculate and provide scores for repositories.

The API is available at `/repository/<id>/trustable/score/<id>`. The API will return
a JSON object with the score for the repository.
