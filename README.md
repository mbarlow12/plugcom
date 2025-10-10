# plugcom

A minimal example of using a `uv` workspace to register subcommands via a plugin interface (using `pluggy`)

## Structure

The workspace members are placed under the `bin/` directory and configured as such in `pyproject.toml`.

### `plugcom-core`

Defines the base command `plg` and the plugin hooks (`hookspecs.py`). The `PlugcomGroup` is a `click.Group` that uses `pluggy`
features to call the hook functions and add commands.

We can add commands the typical way (e.g. `click.Group:add_command`) or via internal hook implementations (see `cli/run.py`).

The plugin interface is exposed through a setuptools entrypoint called "plugcom".

### plugcom-doit

The "external" plugin.

Hooks into the `plugcom-core` plugin interface with the following table in `pyproject.toml`

```toml
[project.entry-points.plugcom]
doit = "plugcom.doit"
```

The `plugcom.doit` module implements the `@plugcom_add_command` hookspec with a new `doit` subcommand.

#### Namespaces

Each package also defines a namespaced module beginning with `plugcom`. Though not necessary for this specific use case, it makes for nice imports:

- `from plugcom.core.cli import run`
- `from plugcom.doit ...`

## Installation

```bash
git clone https://github.com/mbarlow12/plugcom.git
uv sync
```

## Usage

`uv run plg --help`

## Adding new subcommands

### Via a new package (minimal)

1. `uv init --package --name [name] ./bin/[package directory]`

- eg `uv init --package --name grug ./bin/plugcom-grug` (note that it's not necessary to prefix the directory with `plugcom-`)

2. select a module to add the `hookimpl` function(s) (we'll use the base `__init__.py` here)
3. add the following to the new package's `pyproject.toml`
  `bin/plugcom-grug/pyproject.toml`

  ```toml
  [project.entry-points.plugcom]
  grug = "plugcom_grug" # we're skipping with namespaced module name here
  ```

4. add `plugcom-core` as a dependency on `plugcom-grug` (`uv add --package plugcom-grug plugcom-core`)
5. in `src/plugcom_grug/__init__.py`

  ```python
  from plugcom.core import hookimpl

  @hookimpl
  def plugcom_add_command(cmd_dict):
    @click.command()
    # add click.option(), click.argument(), etc...
    # can also register entirely new click.Groups if desired
    def grug():
      ...
    # add your command to the command dictionary
    cmd_dict["grug"] = grug

    # NOTE: another viable option is to have hookimls simply return the command
    # then the manager (in `plugcom-core`) can extract the command name.
  ```

6. add the new plugin as a top-level dependency
  `uv add plugcom-core`
7. run `uv run plg --help` to see the new subcommand
